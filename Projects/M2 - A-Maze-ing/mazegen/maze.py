"""Core data model for the A-Maze-ing project.

Provides the :class:`Cell` dataclass and :class:`MazeGrid` class used by both
the generator and the visual renderers.

Wall encoding (one hex digit per cell):

    Bit  Direction
    0    North  (LSB)
    1    East
    2    South
    3    West

A bit value of **1** means the wall is **closed** (present).
A bit value of **0** means the wall is **open** (passage exists).
"""

from __future__ import annotations

from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Direction constants
# ---------------------------------------------------------------------------

NORTH: int = 0
EAST: int = 1
SOUTH: int = 2
WEST: int = 3

#: Map from direction to its opposite
OPPOSITE: dict[int, int] = {
    NORTH: SOUTH,
    EAST: WEST,
    SOUTH: NORTH,
    WEST: EAST,
}

#: Unit vectors (dx, dy) for each direction
DELTAS: dict[int, tuple[int, int]] = {
    NORTH: (0, -1),
    EAST:  (1,  0),
    SOUTH: (0,  1),
    WEST:  (-1, 0),
}


# ---------------------------------------------------------------------------
# Cell
# ---------------------------------------------------------------------------

@dataclass
class Cell:
    """A single cell in the maze grid.

    Attributes:
        x: Column index (0-based, left to right).
        y: Row index (0-based, top to bottom).
        mask: 4-bit integer encoding which walls are closed.
            Bit 0 = North, bit 1 = East, bit 2 = South, bit 3 = West.
            A bit set to 1 means the wall is present (closed).
            The value 0xF (15) means all four walls are closed.
    """

    x: int
    y: int
    mask: int = field(default=0xF)

    def has_wall(self, direction: int) -> bool:
        """Return True if the wall in *direction* is closed.

        Args:
            direction: One of NORTH, EAST, SOUTH, WEST.

        Returns:
            True when the corresponding wall bit is set.
        """
        return bool(self.mask & (1 << direction))

    def hex_char(self) -> str:
        """Return the single hex character representing this cell's walls.

        Returns:
            An uppercase hex character in the range '0'–'F'.
        """
        return format(self.mask, 'X')

    def __repr__(self) -> str:  # pragma: no cover
        return f"Cell(x={self.x}, y={self.y}, mask=0x{self.mask:X})"


# ---------------------------------------------------------------------------
# MazeGrid
# ---------------------------------------------------------------------------

class MazeGrid:
    """A two-dimensional grid of :class:`Cell` objects representing a maze.

    All cells are initialised with every wall closed (mask = 0xF).
    Walls are removed in pairs: removing the East wall of (x, y) simultaneously
    removes the West wall of (x+1, y) to keep the grid consistent.

    Attributes:
        width: Number of columns.
        height: Number of rows.
        entry: (x, y) coordinates of the maze entry cell.
        exit_: (x, y) coordinates of the maze exit cell.
        cells: 2-D list ``cells[row][col]`` of :class:`Cell` objects.
    """

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit_: tuple[int, int],
    ) -> None:
        """Initialise a fully-walled maze grid.

        Args:
            width: Number of columns (must be >= 2).
            height: Number of rows (must be >= 2).
            entry: (x, y) coordinates of the entry cell.
            exit_: (x, y) coordinates of the exit cell.

        Raises:
            ValueError: If dimensions are invalid or entry/exit are out of
                bounds or equal to each other.
        """
        if width < 2 or height < 2:
            raise ValueError(
                f"Maze dimensions must be at least 2x2, got {width}x{height}."
            )
        self._validate_coord("entry", entry, width, height)
        self._validate_coord("exit", exit_, width, height)
        if entry == exit_:
            raise ValueError("Entry and exit coordinates must be different.")

        self.width: int = width
        self.height: int = height
        self.entry: tuple[int, int] = entry
        self.exit_: tuple[int, int] = exit_

        # Build fully-walled grid
        self.cells: list[list[Cell]] = [
            [Cell(x=c, y=r) for c in range(width)]
            for r in range(height)
        ]

    # ------------------------------------------------------------------
    # Wall manipulation
    # ------------------------------------------------------------------

    def has_wall(self, x: int, y: int, direction: int) -> bool:
        """Return True if the wall in *direction* at cell (x, y) is closed.

        Args:
            x: Column index.
            y: Row index.
            direction: One of NORTH, EAST, SOUTH, WEST.

        Returns:
            True when the wall is present.
        """
        return self.cells[y][x].has_wall(direction)

    def remove_wall(self, x: int, y: int, direction: int) -> None:
        """Open the wall between (x, y) and its neighbour in *direction*.

        The operation is symmetric: both the wall of the current cell and the
        matching wall of the adjacent cell are cleared simultaneously.

        Args:
            x: Column index of the source cell.
            y: Row index of the source cell.
            direction: Direction toward the neighbour (NORTH/EAST/SOUTH/WEST).
        """
        self.cells[y][x].mask &= ~(1 << direction)

        dx, dy = DELTAS[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < self.width and 0 <= ny < self.height:
            self.cells[ny][nx].mask &= ~(1 << OPPOSITE[direction])

    def set_wall(self, x: int, y: int, direction: int) -> None:
        """Close the wall between (x, y) and its neighbour in *direction*.

        The operation is symmetric.

        Args:
            x: Column index of the source cell.
            y: Row index of the source cell.
            direction: Direction toward the neighbour.
        """
        self.cells[y][x].mask |= (1 << direction)

        dx, dy = DELTAS[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < self.width and 0 <= ny < self.height:
            self.cells[ny][nx].mask |= (1 << OPPOSITE[direction])

    # ------------------------------------------------------------------
    # Export helpers
    # ------------------------------------------------------------------

    def to_hex_grid(self) -> list[list[str]]:
        """Return the maze as a 2-D list of single hex-digit strings.

        Returns:
            ``grid[row][col]`` where each element is a hex character '0'–'f'.
        """
        return [
            [cell.hex_char() for cell in row]
            for row in self.cells
        ]

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def is_valid(self) -> bool:
        """Check that every pair of adjacent cells has consistent wall bits.

        Mirrors the logic of the provided ``output_validator.py``.

        Returns:
            True if all neighbouring-cell wall pairs match.
        """
        for r in range(self.height):
            for c in range(self.width):
                v = self.cells[r][c].mask
                # North wall of (c,r) must equal South wall of (c,r-1)
                if r > 0 and (v & 1) != ((self.cells[r - 1][c].mask >> 2) & 1):
                    return False
                # East wall of (c,r) must equal West wall of (c+1,r)
                if (
                    c < self.width - 1
                    and (v >> 1) & 1
                    != (self.cells[r][c + 1].mask >> 3) & 1
                ):
                    return False
                # South wall of (c,r) must equal North wall of (c,r+1)
                if (
                    r < self.height - 1
                    and (v >> 2) & 1 != self.cells[r + 1][c].mask & 1
                ):
                    return False
                # West wall of (c,r) must equal East wall of (c-1,r)
                if (
                    c > 0
                    and (v >> 3) & 1
                    != (self.cells[r][c - 1].mask >> 1) & 1
                ):
                    return False
        return True

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _validate_coord(
        name: str,
        coord: tuple[int, int],
        width: int,
        height: int,
    ) -> None:
        """Raise ValueError if *coord* is outside the grid bounds.

        Args:
            name: Human-readable coordinate name for error messages.
            coord: (x, y) pair to validate.
            width: Grid width.
            height: Grid height.
        """
        x, y = coord
        if not (0 <= x < width and 0 <= y < height):
            raise ValueError(
                f"{name} coordinate {coord} is outside the "
                f"{width}x{height} grid."
            )

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"MazeGrid(width={self.width}, height={self.height}, "
            f"entry={self.entry}, exit={self.exit_})"
        )
