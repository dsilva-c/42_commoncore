"""Maze generator using multiple maze carving algorithms.

Features
--------
- Deterministic output via optional seed.
- *Perfect* mode (default): exactly one path between any two cells.
- *Non-perfect* mode: extra passages added after the spanning tree is built,
  creating loops while still enforcing the no-3×3-open-area rule.
- The ``"42"`` pattern is burned into the maze before carving: a set of cells
  that match the pixel silhouette of the digits 4 and 2 are locked to all
  walls closed (0xF) and skipped by the DFS.
- A built-in BFS is included for :meth:`get_solution`, allowing the library
  to be used standalone without the project's MazeSolver.
"""

from __future__ import annotations

import random
import sys
from collections import deque
from typing import Optional

from mazegen.maze import (
    DELTAS,
    EAST,
    NORTH,
    SOUTH,
    WEST,
    MazeGrid,
)

# ---------------------------------------------------------------------------
# "42" pixel font (5 rows × 3 columns per digit, 1-column gap between digits)
# ---------------------------------------------------------------------------
# Each '1' marks a cell that will be fully walled (part of the pattern).
# Layout visualised (columns left to right, rows top to bottom):
#
#   4:  1 0 1   2:  1 1 1
#       1 0 1       0 0 1
#       1 1 1       0 1 1
#       0 0 1       1 0 0
#       0 0 1       1 1 1
#
# Composed (7 columns wide, 5 rows tall):
#   1 0 1   1 1 1
#   1 0 1   0 0 1
#   1 1 1   0 1 1
#   0 0 1   1 0 0
#   0 0 1   1 1 1

_DIGIT_4: list[list[int]] = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1],
]

_DIGIT_2: list[list[int]] = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
]

# Gap (columns) between the two digits
_DIGIT_GAP: int = 1

# Padding (cells) around the entire pattern on each side
_PATTERN_PADDING: int = 1

# Full pixel pattern: list[row] of list[col] (0 or 1)
_PATTERN: list[list[int]] = [
    row4 + [0] * _DIGIT_GAP + row2
    for row4, row2 in zip(_DIGIT_4, _DIGIT_2)
]

# Minimum maze dimensions required to embed the pattern with padding
PATTERN_ROWS: int = len(_PATTERN)
PATTERN_COLS: int = len(_PATTERN[0])
MIN_WIDTH_FOR_42: int = PATTERN_COLS + 2 * _PATTERN_PADDING + 2
MIN_HEIGHT_FOR_42: int = PATTERN_ROWS + 2 * _PATTERN_PADDING + 2


class MazeGenerator:
    """Generate a maze using the DFS Recursive Backtracker algorithm.

    The class implements the algorithm in three phases:

    1. **Initialise** a fully-walled :class:`MazeGrid`.
    2. **Burn the "42" pattern** — mark a set of cells as permanently closed.
    3. **Carve passages** using iterative DFS, skipping pattern cells.
       Disconnected regions caused by the pattern are reconnected greedily.
    4. (Non-perfect only) **Add extra passages** to create loops, then repair
       any 3×3 open areas that appear.
    5. **Open the border walls** at the entry and exit cells.
    6. **Compute the solution** path via BFS for :meth:`get_solution`.

    Args:
        width: Number of columns in the maze.
        height: Number of rows in the maze.
        seed: Optional random seed for reproducibility.
        perfect: If True (default), generate a perfect maze (spanning tree).
            If False, add random extra passages after the DFS phase.
        algorithm: Algorithm selection. Supported values: ``"dfs"``,
            ``"prims"``, ``"kruskals"``.

    Example:
        >>> gen = MazeGenerator(20, 15, seed=42)
        >>> grid = gen.generate()
        >>> print(grid.width, grid.height)
        20 15
        >>> path = gen.get_solution()
        >>> len(path) > 0
        True
    """

    def __init__(
        self,
        width: int,
        height: int,
        seed: Optional[int] = None,
        perfect: bool = True,
        algorithm: str = "dfs",
    ) -> None:
        if width < 2 or height < 2:
            raise ValueError(
                f"Maze dimensions must be at least 2×2, got {width}×{height}."
            )
        self.width: int = width
        self.height: int = height
        self.seed: Optional[int] = seed
        self.perfect: bool = perfect
        self.algorithm: str = algorithm.lower()

        self._rng: random.Random = random.Random(seed)
        self._grid: Optional[MazeGrid] = None
        self._solution: Optional[list[tuple[int, int]]] = None
        self._42_cells: set[tuple[int, int]] = set()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def generate(
        self,
        entry: tuple[int, int] = (0, 0),
        exit_: Optional[tuple[int, int]] = None,
    ) -> MazeGrid:
        """Generate and return a new maze.

        Args:
            entry: (x, y) coordinates of the entry cell. Defaults to (0, 0).
            exit_: (x, y) coordinates of the exit cell.
                Defaults to (width-1, height-1).

        Returns:
            A fully generated :class:`MazeGrid`.

        Raises:
            ValueError: If entry or exit coordinates are invalid.
            RuntimeError: If the generated maze fails wall-symmetry validation.
        """
        if exit_ is None:
            exit_ = (self.width - 1, self.height - 1)

        grid = MazeGrid(self.width, self.height, entry, exit_)

        # Phase 1: Burn the "42" pattern (or warn if maze is too small)
        self._42_cells = self._place_42_pattern(grid)

        # Phase 2: Carve passages with chosen algorithm
        if self.algorithm == "dfs":
            self._carve_dfs(grid, self._42_cells)
        elif self.algorithm == "prims":
            self._carve_prims(grid, self._42_cells)
        elif self.algorithm == "kruskals":
            self._carve_kruskals(grid, self._42_cells)
        else:
            raise ValueError(
                f"Unsupported algorithm '{self.algorithm}'. "
                "Use 'dfs', 'prims', or 'kruskals'."
            )

        # Phase 3: Non-perfect mode — add random extra passages
        if not self.perfect:
            self._add_extra_passages(grid, self._42_cells)

        # Phase 4: Fix any 3×3 open areas
        self._fix_3x3_open_areas(grid, self._42_cells)

        # Phase 4b: Enforce perfect maze (tree) if requested
        if self.perfect:
            self._ensure_perfect_tree(grid, self._42_cells)

        # Phase 5: Open borders at entry and exit
        self._open_border(grid, entry)
        self._open_border(grid, exit_)

        # Phase 6: Validate
        if not grid.is_valid():
            raise RuntimeError(
                "Maze generation produced inconsistent wall data. "
                "Please report this as a bug."
            )

        self._grid = grid
        # Pre-compute solution
        self._solution = self._bfs_path(grid)

        return grid

    def get_grid(self) -> MazeGrid:
        """Return the last generated :class:`MazeGrid`.

        Returns:
            The most recently generated grid.

        Raises:
            RuntimeError: If :meth:`generate` has not been called yet.
        """
        if self._grid is None:
            raise RuntimeError("Call generate() before get_grid().")
        return self._grid

    def get_solution(self) -> list[tuple[int, int]]:
        """Return the solution path as a list of (x, y) cell coordinates.

        The path runs from the entry to the exit cell and is computed by BFS
        (guaranteed shortest path).

        Returns:
            Ordered list of (x, y) tuples from entry to exit.
            Returns an empty list if no path exists.

        Raises:
            RuntimeError: If :meth:`generate` has not been called yet.
        """
        if self._solution is None:
            raise RuntimeError("Call generate() before get_solution().")
        return list(self._solution)

    @property
    def pattern_cells(self) -> set[tuple[int, int]]:
        """Return the set of cells occupied by the embedded "42" pattern.

        Cells in this set have all four walls permanently closed (mask=0xF)
        and are skipped by the DFS carver.  The set is empty when the maze is
        too small to embed the pattern.

        Returns:
            A copy of the pattern cell coordinates as (x, y) tuples.
        """
        return set(self._42_cells)

    # ------------------------------------------------------------------
    # "42" Pattern
    # ------------------------------------------------------------------

    def _place_42_pattern(self, grid: MazeGrid) -> set[tuple[int, int]]:
        """Embed the '42' pixel pattern into the grid.

        Pattern cells are set to 0xF (all walls closed) and returned as a set
        so the DFS can skip them.  If the maze is too small to fit the pattern
        (including padding), a message is printed to stderr and an empty set is
        returned.

        Args:
            grid: The grid to modify.

        Returns:
            Set of (x, y) coordinates of pattern cells.
        """
        if (
            grid.width < MIN_WIDTH_FOR_42
            or grid.height < MIN_HEIGHT_FOR_42
        ):
            print(
                f"[42 pattern] Maze {grid.width}×{grid.height} is too small "
                f"to embed the '42' pattern (minimum {MIN_WIDTH_FOR_42}×"
                f"{MIN_HEIGHT_FOR_42}). Pattern omitted.",
                file=sys.stderr,
            )
            return set()

        # Centre the pattern inside the grid
        origin_x = (grid.width - PATTERN_COLS) // 2
        origin_y = (grid.height - PATTERN_ROWS) // 2

        pattern_cells: set[tuple[int, int]] = set()
        for pr, row in enumerate(_PATTERN):
            for pc, bit in enumerate(row):
                if bit:
                    gx = origin_x + pc
                    gy = origin_y + pr
                    grid.cells[gy][gx].mask = 0xF
                    pattern_cells.add((gx, gy))

        return pattern_cells

    # ------------------------------------------------------------------
    # DFS Carving
    # ------------------------------------------------------------------

    def _carve_dfs(
        self,
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> None:
        """Carve passages using the iterative DFS Recursive Backtracker.

        Skips pattern cells.  After the primary DFS, any isolated non-pattern
        regions are connected greedily by opening one wall to the nearest
        already-visited cell.

        Args:
            grid: The grid to carve.
            pattern_cells: Cells to treat as permanently blocked.
        """
        visited: set[tuple[int, int]] = set(pattern_cells)

        # Choose a random non-pattern starting cell
        start = self._random_non_pattern(grid, pattern_cells)
        self._dfs_from(grid, start, visited, pattern_cells)

        # Connect any remaining isolated non-pattern cells
        self._connect_isolated(grid, visited, pattern_cells)

    def _carve_prims(
        self,
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> None:
        """Carve passages using randomized Prim's algorithm.

        Skips pattern cells. After the primary pass, isolated regions are
        connected via the same greedy bridge used by DFS.

        Args:
            grid: The grid to carve.
            pattern_cells: Cells to treat as permanently blocked.
        """
        visited: set[tuple[int, int]] = set(pattern_cells)
        start = self._random_non_pattern(grid, pattern_cells)
        visited.add(start)

        frontier: list[tuple[int, int, int]] = []

        def add_frontier(cx: int, cy: int) -> None:
            for d in [NORTH, EAST, SOUTH, WEST]:
                dx, dy = DELTAS[d]
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < grid.width and 0 <= ny < grid.height):
                    continue
                if (nx, ny) in visited or (nx, ny) in pattern_cells:
                    continue
                frontier.append((cx, cy, d))

        add_frontier(*start)

        while frontier:
            idx = self._rng.randrange(len(frontier))
            x, y, d = frontier.pop(idx)
            dx, dy = DELTAS[d]
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited:
                continue
            grid.remove_wall(x, y, d)
            visited.add((nx, ny))
            add_frontier(nx, ny)

        # Connect any remaining isolated non-pattern cells
        self._connect_isolated(grid, visited, pattern_cells)

    def _carve_kruskals(
        self,
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> None:
        """Carve passages using randomized Kruskal's algorithm.

        Builds a spanning forest with union-find over all non-pattern cells,
        then connects any remaining isolated regions with the standard
        bridge pass to ensure full reachability.

        Args:
            grid: The grid to carve.
            pattern_cells: Cells to treat as permanently blocked.
        """
        nodes = [
            (x, y)
            for y in range(grid.height)
            for x in range(grid.width)
            if (x, y) not in pattern_cells
        ]
        if not nodes:
            return

        parent: dict[tuple[int, int], tuple[int, int]] = {
            node: node for node in nodes
        }
        rank: dict[tuple[int, int], int] = {node: 0 for node in nodes}

        def find(node: tuple[int, int]) -> tuple[int, int]:
            root = node
            while parent[root] != root:
                root = parent[root]
            while parent[node] != node:
                nxt = parent[node]
                parent[node] = root
                node = nxt
            return root

        def union(a: tuple[int, int], b: tuple[int, int]) -> bool:
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        edges: list[tuple[int, int, int]] = []
        for y in range(grid.height):
            for x in range(grid.width):
                if (x, y) in pattern_cells:
                    continue
                for d in (EAST, SOUTH):
                    dx, dy = DELTAS[d]
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < grid.width
                        and 0 <= ny < grid.height
                        and (nx, ny) not in pattern_cells
                    ):
                        edges.append((x, y, d))

        self._rng.shuffle(edges)

        for x, y, d in edges:
            dx, dy = DELTAS[d]
            nx, ny = x + dx, y + dy
            if union((x, y), (nx, ny)):
                grid.remove_wall(x, y, d)

        start = self._random_non_pattern(grid, pattern_cells)
        visited = self._reachable_cells(grid, pattern_cells, start)
        self._connect_isolated(grid, visited, pattern_cells)

    def _dfs_from(
        self,
        grid: MazeGrid,
        start: tuple[int, int],
        visited: set[tuple[int, int]],
        pattern_cells: set[tuple[int, int]],
    ) -> None:
        """Iterative DFS from *start*, updating *visited* in place.

        Args:
            grid: The grid to carve.
            start: Starting (x, y) coordinate.
            visited: Set of already-visited (or blocked) cells, updated here.
            pattern_cells: Permanently blocked cells (not carved into).
        """
        visited.add(start)
        stack: list[tuple[int, int]] = [start]

        while stack:
            x, y = stack[-1]
            dirs = [NORTH, EAST, SOUTH, WEST]
            self._rng.shuffle(dirs)

            moved = False
            for d in dirs:
                dx, dy = DELTAS[d]
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < grid.width
                    and 0 <= ny < grid.height
                    and (nx, ny) not in visited
                ):
                    grid.remove_wall(x, y, d)
                    visited.add((nx, ny))
                    stack.append((nx, ny))
                    moved = True
                    break

            if not moved:
                stack.pop()

    def _connect_isolated(
        self,
        grid: MazeGrid,
        visited: set[tuple[int, int]],
        pattern_cells: set[tuple[int, int]],
    ) -> None:
        """Connect any non-pattern cells not yet reached by the primary DFS.

        Iterates over unvisited cells and, for each one, finds a visited
        non-pattern neighbour to open a wall to, then continues the DFS.

        Args:
            grid: The grid to modify.
            visited: Set of visited cells, updated in place.
            pattern_cells: Permanently blocked cells.
        """
        all_cells = {
            (x, y)
            for y in range(grid.height)
            for x in range(grid.width)
            if (x, y) not in pattern_cells
        }
        changed = True
        while changed:
            changed = False
            unvisited = all_cells - visited
            if not unvisited:
                break
            for cell in sorted(unvisited):
                cx, cy = cell
                for d in [NORTH, EAST, SOUTH, WEST]:
                    dx, dy = DELTAS[d]
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) in visited and (nx, ny) not in pattern_cells:
                        grid.remove_wall(cx, cy, d)
                        visited.add(cell)
                        self._dfs_from(grid, cell, visited, pattern_cells)
                        changed = True
                        break
                if cell in visited:
                    break

    # ------------------------------------------------------------------
    # Non-perfect: extra passages
    # ------------------------------------------------------------------

    def _add_extra_passages(
        self,
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
        extra_ratio: float = 0.15,
    ) -> None:
        """Open a random subset of internal walls to create loops.

        The number of extra passages is proportional to the total number of
        non-pattern cells.

        Args:
            grid: The grid to modify.
            pattern_cells: Cells whose walls must not be altered.
            extra_ratio: Fraction of non-pattern cells to add as extra
                passages (default 0.15).
        """
        # Collect all closed internal walls between non-pattern cells
        candidates: list[tuple[int, int, int]] = []
        for y in range(grid.height):
            for x in range(grid.width):
                if (x, y) in pattern_cells:
                    continue
                for d in (EAST, SOUTH):
                    dx, dy = DELTAS[d]
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < grid.width
                        and 0 <= ny < grid.height
                        and (nx, ny) not in pattern_cells
                        and grid.has_wall(x, y, d)
                    ):
                        candidates.append((x, y, d))

        num_extra = max(1, int(len(candidates) * extra_ratio))
        self._rng.shuffle(candidates)
        for x, y, d in candidates[:num_extra]:
            grid.remove_wall(x, y, d)

    # ------------------------------------------------------------------
    # 3×3 open-area check and repair
    # ------------------------------------------------------------------

    def _fix_3x3_open_areas(
        self,
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> None:
        """Iteratively close walls until no 3×3 fully-open area remains.

        A 3×3 area is "fully open" when every pair of adjacent cells within
        the block shares an open passage (no wall between them).  Adding
        the South wall of the centre cell (and the matching North wall one
        row below) always breaks such a block without leaving an isolated cell.

        Args:
            grid: The grid to repair.
            pattern_cells: Cells whose walls are locked.
        """
        changed = True
        while changed:
            changed = False
            for y in range(grid.height - 2):
                for x in range(grid.width - 2):
                    if self._is_3x3_open(grid, x, y):
                        # Add wall between centre and cell directly below it
                        cx, cy = x + 1, y + 1
                        grid.set_wall(cx, cy, SOUTH)
                        changed = True

    # ------------------------------------------------------------------
    # Perfect maze enforcement
    # ------------------------------------------------------------------

    def _ensure_perfect_tree(
        self,
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> None:
        """Remove extra passages until the non-pattern graph is a tree.

        Ensures exactly one path between any two reachable non-pattern cells.
        """
        nodes = grid.width * grid.height - len(pattern_cells)
        if nodes <= 1:
            return

        edges = self._count_open_edges(grid, pattern_cells)
        if edges <= nodes - 1:
            return

        open_edges = set(self._list_open_edges(grid, pattern_cells))
        tree_edges = self._bfs_tree_edges(grid, pattern_cells)
        extra_edges = list(open_edges - tree_edges)
        self._rng.shuffle(extra_edges)

        for x, y, d in extra_edges:
            if edges <= nodes - 1:
                break
            grid.set_wall(x, y, d)
            edges -= 1

    @staticmethod
    def _count_open_edges(
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> int:
        count = 0
        for y in range(grid.height):
            for x in range(grid.width):
                if (x, y) in pattern_cells:
                    continue
                if x + 1 < grid.width and (x + 1, y) not in pattern_cells:
                    if not grid.has_wall(x, y, EAST):
                        count += 1
                if y + 1 < grid.height and (x, y + 1) not in pattern_cells:
                    if not grid.has_wall(x, y, SOUTH):
                        count += 1
        return count

    @staticmethod
    def _list_open_edges(
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> list[tuple[int, int, int]]:
        edges: list[tuple[int, int, int]] = []
        for y in range(grid.height):
            for x in range(grid.width):
                if (x, y) in pattern_cells:
                    continue
                if x + 1 < grid.width and (x + 1, y) not in pattern_cells:
                    if not grid.has_wall(x, y, EAST):
                        edges.append((x, y, EAST))
                if y + 1 < grid.height and (x, y + 1) not in pattern_cells:
                    if not grid.has_wall(x, y, SOUTH):
                        edges.append((x, y, SOUTH))
        return edges

    @staticmethod
    def _bfs_tree_edges(
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> set[tuple[int, int, int]]:
        """Return the set of open edges used by a BFS tree from entry."""
        def canonical_edge(x: int, y: int, d: int) -> tuple[int, int, int]:
            if d == EAST:
                return (x, y, EAST)
            if d == SOUTH:
                return (x, y, SOUTH)
            if d == WEST:
                return (x - 1, y, EAST)
            return (x, y - 1, SOUTH)

        start = grid.entry
        if start in pattern_cells:
            return set()

        visited: set[tuple[int, int]] = {start}
        queue: deque[tuple[int, int]] = deque([start])
        tree_edges: set[tuple[int, int, int]] = set()

        while queue:
            cx, cy = queue.popleft()
            for d in [NORTH, EAST, SOUTH, WEST]:
                if grid.has_wall(cx, cy, d):
                    continue
                dx, dy = DELTAS[d]
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < grid.width and 0 <= ny < grid.height):
                    continue
                nxt = (nx, ny)
                if nxt in pattern_cells or nxt in visited:
                    continue
                visited.add(nxt)
                queue.append(nxt)
                tree_edges.add(canonical_edge(cx, cy, d))

        return tree_edges

    @staticmethod
    def _is_fully_connected(
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> bool:
        """Return True if all non-pattern cells are reachable from entry."""
        start = grid.entry
        if start in pattern_cells:
            return False

        total = grid.width * grid.height - len(pattern_cells)
        visited: set[tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque([start])
        visited.add(start)

        while queue:
            cx, cy = queue.popleft()
            for d in [NORTH, EAST, SOUTH, WEST]:
                if grid.has_wall(cx, cy, d):
                    continue
                dx, dy = DELTAS[d]
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < grid.width and 0 <= ny < grid.height):
                    continue
                nxt = (nx, ny)
                if nxt in pattern_cells or nxt in visited:
                    continue
                visited.add(nxt)
                queue.append(nxt)

        return len(visited) == total

    @staticmethod
    def _reachable_cells(
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
        start: tuple[int, int],
    ) -> set[tuple[int, int]]:
        """Return the set of reachable non-pattern cells from start."""
        if start in pattern_cells:
            return set()

        visited: set[tuple[int, int]] = {start}
        queue: deque[tuple[int, int]] = deque([start])

        while queue:
            cx, cy = queue.popleft()
            for d in [NORTH, EAST, SOUTH, WEST]:
                if grid.has_wall(cx, cy, d):
                    continue
                dx, dy = DELTAS[d]
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < grid.width and 0 <= ny < grid.height):
                    continue
                nxt = (nx, ny)
                if nxt in pattern_cells or nxt in visited:
                    continue
                visited.add(nxt)
                queue.append(nxt)

        return visited

    @staticmethod
    def _is_3x3_open(grid: MazeGrid, x: int, y: int) -> bool:
        """Return True if the 3×3 block with top-left at (x, y) is fully open.

        Checks all horizontal (East) and vertical (South) internal passages
        for the 3×3 block.

        Args:
            grid: The grid to inspect.
            x: Column index of the top-left cell of the block.
            y: Row index of the top-left cell of the block.

        Returns:
            True when all internal passages are open.
        """
        for row in range(y, y + 3):
            for col in range(x, x + 3):
                if col < x + 2 and grid.has_wall(col, row, EAST):
                    return False
                if row < y + 2 and grid.has_wall(col, row, SOUTH):
                    return False
        return True

    # ------------------------------------------------------------------
    # Border opening
    # ------------------------------------------------------------------

    def _open_border(
        self,
        grid: MazeGrid,
        coord: tuple[int, int],
    ) -> None:
        """Open the outer border wall of the given border cell.

        Determines which cardinal side of the cell lies on the grid border and
        clears that wall bit (for a border cell there is no neighbour to update
        on the outside, so the operation is a direct bit-clear).

        Args:
            grid: The grid to modify.
            coord: (x, y) of the border cell to open.
        """
        x, y = coord
        if x == 0:
            direction = WEST
        elif x == grid.width - 1:
            direction = EAST
        elif y == 0:
            direction = NORTH
        else:
            direction = SOUTH

        grid.cells[y][x].mask &= ~(1 << direction)

    # ------------------------------------------------------------------
    # Internal BFS (for get_solution)
    # ------------------------------------------------------------------

    def _bfs_path(
        self,
        grid: MazeGrid,
    ) -> list[tuple[int, int]]:
        """Compute the shortest path from entry to exit using BFS.

        Args:
            grid: The maze grid to search.

        Returns:
            Ordered list of (x, y) tuples from entry to exit.
            Returns an empty list if no path exists.
        """
        start = grid.entry
        goal = grid.exit_
        if start == goal:
            return [start]

        prev: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
        queue: deque[tuple[int, int]] = deque([start])

        while queue:
            cx, cy = queue.popleft()
            if (cx, cy) == goal:
                break
            for d in [NORTH, EAST, SOUTH, WEST]:
                if not grid.has_wall(cx, cy, d):
                    dx, dy = DELTAS[d]
                    nx, ny = cx + dx, cy + dy
                    if not (0 <= nx < grid.width and 0 <= ny < grid.height):
                        continue
                    nxt = (nx, ny)
                    if nxt not in prev:
                        prev[nxt] = (cx, cy)
                        queue.append(nxt)

        if goal not in prev:
            return []

        # Reconstruct path
        path: list[tuple[int, int]] = []
        node: tuple[int, int] | None = goal
        while node is not None:
            path.append(node)
            node = prev[node]
        path.reverse()
        return path

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def _random_non_pattern(
        self,
        grid: MazeGrid,
        pattern_cells: set[tuple[int, int]],
    ) -> tuple[int, int]:
        """Return a random non-pattern cell coordinate.

        Args:
            grid: The grid (for dimension bounds).
            pattern_cells: Set of blocked cells to exclude.

        Returns:
            A random (x, y) tuple not in pattern_cells.

        Raises:
            RuntimeError: If no non-pattern cell exists (degenerate maze).
        """
        candidates = [
            (x, y)
            for y in range(grid.height)
            for x in range(grid.width)
            if (x, y) not in pattern_cells
        ]
        if not candidates:
            raise RuntimeError("No non-pattern cells available in the maze.")
        return self._rng.choice(candidates)
