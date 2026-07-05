"""Unit tests for mazegen.generator — authored by dsilva-c."""

from __future__ import annotations

from collections import deque

import pytest

from mazegen.generator import (
    MazeGenerator,
    MIN_WIDTH_FOR_42,
    MIN_HEIGHT_FOR_42,
)
from mazegen.maze import MazeGrid, NORTH, EAST, SOUTH, WEST, DELTAS


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def bfs_reachable(
    grid: MazeGrid,
    start: tuple[int, int],
) -> set[tuple[int, int]]:
    """Return the set of all cells reachable from *start* through passages."""
    visited: set[tuple[int, int]] = {start}
    queue: deque[tuple[int, int]] = deque([start])
    while queue:
        x, y = queue.popleft()
        for direction in (NORTH, EAST, SOUTH, WEST):
            if not grid.has_wall(x, y, direction):
                dx, dy = DELTAS[direction]
                nx, ny = x + dx, y + dy
                if not (0 <= nx < grid.width and 0 <= ny < grid.height):
                    continue
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return visited


def count_open_internal_walls(grid: MazeGrid) -> int:
    """Count open internal (non-border) wall pairs in the grid."""
    count = 0
    for y in range(grid.height):
        for x in range(grid.width):
            # Only count East and South to avoid double-counting
            if x + 1 < grid.width and not grid.has_wall(x, y, EAST):
                count += 1
            if y + 1 < grid.height and not grid.has_wall(x, y, SOUTH):
                count += 1
    return count


def has_3x3_open_area(grid: MazeGrid) -> bool:
    """Return True if any 3×3 block of cells is fully interconnected."""
    for top in range(grid.height - 2):
        for left in range(grid.width - 2):
            # All 6 East-connections and 6 South-connections within the 3×3
            all_open = True
            for row in range(top, top + 3):
                for col in range(left, left + 2):
                    if grid.has_wall(col, row, EAST):
                        all_open = False
                        break
                if not all_open:
                    break
            if all_open:
                for col in range(left, left + 3):
                    for row in range(top, top + 2):
                        if grid.has_wall(col, row, SOUTH):
                            all_open = False
                            break
                    if not all_open:
                        break
            if all_open:
                return True
    return False


# ---------------------------------------------------------------------------
# Basic dimension tests
# ---------------------------------------------------------------------------

class TestGridDimensions:

    def test_width_matches(self) -> None:
        grid = MazeGenerator(10, 8, seed=1).generate()
        assert grid.width == 10

    def test_height_matches(self) -> None:
        grid = MazeGenerator(10, 8, seed=1).generate()
        assert grid.height == 8

    def test_cells_array_shape(self) -> None:
        grid = MazeGenerator(7, 5, seed=1).generate()
        assert len(grid.cells) == 5           # rows
        assert len(grid.cells[0]) == 7        # cols

    def test_entry_and_exit_stored(self) -> None:
        gen = MazeGenerator(10, 10, seed=2)
        grid = gen.generate(entry=(0, 0), exit_=(9, 9))
        assert grid.entry == (0, 0)
        assert grid.exit_ == (9, 9)

    def test_minimum_size_2x2(self) -> None:
        grid = MazeGenerator(2, 2, seed=0).generate()
        assert grid.width == 2 and grid.height == 2

    def test_too_small_raises(self) -> None:
        with pytest.raises(ValueError):
            MazeGenerator(1, 5)

    def test_too_small_height_raises(self) -> None:
        with pytest.raises(ValueError):
            MazeGenerator(5, 1)


# ---------------------------------------------------------------------------
# Wall symmetry / is_valid()
# ---------------------------------------------------------------------------

class TestWallSymmetry:

    @pytest.mark.parametrize("seed", [0, 1, 7, 42, 999])
    def test_is_valid_passes(self, seed: int) -> None:
        grid = MazeGenerator(15, 12, seed=seed).generate()
        assert grid.is_valid(), f"is_valid() failed for seed={seed}"

    def test_is_valid_non_perfect(self) -> None:
        grid = MazeGenerator(12, 10, seed=3, perfect=False).generate()
        assert grid.is_valid()

    def test_custom_entry_exit_is_valid(self) -> None:
        grid = MazeGenerator(10, 8, seed=5).generate(
            entry=(0, 4),
            exit_=(9, 4),
        )
        assert grid.is_valid()


# ---------------------------------------------------------------------------
# Perfect maze connectivity
# ---------------------------------------------------------------------------

class TestPerfectConnectivity:

    def _non_pattern_cells(
        self,
        grid: MazeGrid,
        gen: MazeGenerator,
    ) -> set[tuple[int, int]]:
        """Return all cells that are NOT part of the 42 pattern."""
        all_cells = {
            (x, y)
            for y in range(grid.height)
            for x in range(grid.width)
        }
        return all_cells - gen.pattern_cells

    def test_all_non_pattern_cells_reachable(self) -> None:
        gen = MazeGenerator(20, 15, seed=1)
        grid = gen.generate()
        non_pattern = self._non_pattern_cells(grid, gen)
        # Pick any non-pattern cell as start (entry might be one)
        start = grid.entry
        reachable = bfs_reachable(grid, start)
        # All non-pattern cells must be reachable
        unreachable = non_pattern - reachable
        assert unreachable == set(), (
            f"{len(unreachable)} non-pattern cells are disconnected: "
            f"(showing up to 5) {list(unreachable)[:5]}"
        )

    @pytest.mark.parametrize("seed", [0, 13, 99])
    def test_connectivity_with_various_seeds(self, seed: int) -> None:
        gen = MazeGenerator(12, 12, seed=seed)
        grid = gen.generate()
        non_pattern = gen.pattern_cells
        all_cells = {
            (x, y)
            for y in range(grid.height)
            for x in range(grid.width)
        }
        non_pattern_cells = all_cells - non_pattern
        reachable = bfs_reachable(grid, grid.entry)
        unreachable = non_pattern_cells - reachable
        assert unreachable == set(), (
            f"Seed {seed}: {len(unreachable)} cells unreachable"
        )


# ---------------------------------------------------------------------------
# Seed reproducibility
# ---------------------------------------------------------------------------

class TestSeedReproducibility:

    def test_same_seed_same_maze(self) -> None:
        gen_a = MazeGenerator(15, 12, seed=77)
        gen_b = MazeGenerator(15, 12, seed=77)
        grid_a = gen_a.generate()
        grid_b = gen_b.generate()
        hex_a = [
            "".join(cell.hex_char() for cell in row)
            for row in grid_a.cells
        ]
        hex_b = [
            "".join(cell.hex_char() for cell in row)
            for row in grid_b.cells
        ]
        assert hex_a == hex_b

    def test_different_seeds_different_maze(self) -> None:
        grid_a = MazeGenerator(15, 12, seed=1).generate()
        grid_b = MazeGenerator(15, 12, seed=2).generate()
        hex_a = [
            "".join(cell.hex_char() for cell in row) for row in grid_a.cells
        ]
        hex_b = [
            "".join(cell.hex_char() for cell in row) for row in grid_b.cells
        ]
        assert hex_a != hex_b


# ---------------------------------------------------------------------------
# "42" pattern cells
# ---------------------------------------------------------------------------

class TestPattern42:

    def test_pattern_cells_all_walls_closed(self) -> None:
        gen = MazeGenerator(
            MIN_WIDTH_FOR_42 + 4,
            MIN_HEIGHT_FOR_42 + 4,
            seed=1,
        )
        grid = gen.generate()
        for (x, y) in gen.pattern_cells:
            assert grid.cells[y][x].mask == 0xF, (
                f"Pattern cell ({x},{y}) has mask {grid.cells[y][x].mask:#x}, "
                f"expected 0xF (all walls closed)"
            )

    def test_pattern_cells_non_empty_when_maze_large_enough(self) -> None:
        gen = MazeGenerator(
            MIN_WIDTH_FOR_42 + 4,
            MIN_HEIGHT_FOR_42 + 4,
            seed=1,
        )
        gen.generate()
        assert len(gen.pattern_cells) > 0

    def test_no_pattern_when_maze_too_small(self) -> None:
        # A 4×4 maze is below MIN_WIDTH_FOR_42 × MIN_HEIGHT_FOR_42
        gen = MazeGenerator(4, 4, seed=1)
        gen.generate()
        # Pattern cells should be empty (or the generator printed a warning)
        # Either way the maze must still be valid
        assert gen.pattern_cells == set()


# ---------------------------------------------------------------------------
# Non-perfect mode
# ---------------------------------------------------------------------------

class TestNonPerfect:

    def test_non_perfect_more_passages_than_perfect(self) -> None:
        perfect_grid = MazeGenerator(15, 12, seed=7, perfect=True).generate()
        non_perfect_grid = MazeGenerator(
            15, 12, seed=7, perfect=False
        ).generate()
        assert (
            count_open_internal_walls(non_perfect_grid)
            >= count_open_internal_walls(perfect_grid)
        ), "Non-perfect maze should have at least as many passages as perfect"

    def test_non_perfect_is_valid(self) -> None:
        grid = MazeGenerator(15, 12, seed=5, perfect=False).generate()
        assert grid.is_valid()

    def test_no_3x3_open_area_in_result(self) -> None:
        grid = MazeGenerator(20, 15, seed=3, perfect=False).generate()
        assert not has_3x3_open_area(grid), (
            "Non-perfect maze should have no fully-open 3×3 area"
        )


# ---------------------------------------------------------------------------
# Solution path
# ---------------------------------------------------------------------------

class TestSolutionPath:

    def test_solution_non_empty(self) -> None:
        gen = MazeGenerator(10, 8, seed=1)
        gen.generate()
        path = gen.get_solution()
        assert len(path) > 0

    def test_solution_starts_at_entry(self) -> None:
        gen = MazeGenerator(10, 8, seed=1)
        grid = gen.generate()
        path = gen.get_solution()
        assert path[0] == grid.entry

    def test_solution_ends_at_exit(self) -> None:
        gen = MazeGenerator(10, 8, seed=1)
        grid = gen.generate()
        path = gen.get_solution()
        assert path[-1] == grid.exit_

    def test_get_grid_returns_last_generated(self) -> None:
        gen = MazeGenerator(8, 6, seed=2)
        gen.generate()
        assert gen.get_grid().width == 8

    def test_get_grid_before_generate_raises(self) -> None:
        gen = MazeGenerator(8, 6, seed=2)
        with pytest.raises(RuntimeError):
            gen.get_grid()
