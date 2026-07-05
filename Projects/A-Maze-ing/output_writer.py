"""Output file writer for the A-Maze-ing project.

Writes the maze to a text file in the format specified by the subject:

1. One hex digit per cell, row by row, **one row per line**.
2. An **empty separator line**.
3. The entry coordinates ``x,y``.
4. The exit coordinates ``x,y``.
5. The shortest path as a string of direction letters ``N/E/S/W``.
6. Every line ends with ``\\n``.

Example output (4×3 maze)::

    f69f
    3003
    f96f

    0,0
    3,2
    EESSW
"""

from __future__ import annotations

from mazegen.maze import MazeGrid


class OutputWriter:
    """Write a :class:`~mazegen.maze.MazeGrid` to a hex-encoded text file.

    Example:
        >>> from mazegen.generator import MazeGenerator
        >>> from mazegen.solver import MazeSolver
        >>> grid = MazeGenerator(10, 10, seed=1).generate()
        >>> solver = MazeSolver(grid)
        >>> directions = solver.solve()
        >>> writer = OutputWriter()
        >>> writer.write(grid, directions, "output.txt")

    Args:
        (none at construction time; all parameters are passed to
        :meth:`write`.)
    """

    def write(
        self,
        grid: MazeGrid,
        directions: list[str],
        output_path: str,
    ) -> None:
        """Write the maze and solution to *output_path*.

        Args:
            grid: The maze grid to serialise.
            directions: Ordered list of direction letters (``'N'``, ``'E'``,
                ``'S'``, ``'W'``) representing the shortest path from entry
                to exit, as returned by
                :meth:`~mazegen.solver.MazeSolver.solve`.
            output_path: Filesystem path of the output file.  Parent
                directories must already exist.

        Raises:
            OSError: If the file cannot be opened for writing.
            ValueError: If *directions* is not a valid sequence of
                ``N/E/S/W`` letters.
        """
        self._validate_directions(directions)

        entry_x, entry_y = grid.entry
        exit_x, exit_y = grid.exit_
        path_str = "".join(directions)

        with open(output_path, "w", encoding="utf-8", newline="") as fh:
            # 1. Hex grid — one row per line
            for row in grid.cells:
                fh.write("".join(cell.hex_char() for cell in row) + "\n")

            # 2. Empty separator line
            fh.write("\n")

            # 3. Entry coordinates
            fh.write(f"{entry_x},{entry_y}\n")

            # 4. Exit coordinates
            fh.write(f"{exit_x},{exit_y}\n")

            # 5. Path direction string
            fh.write(path_str + "\n")

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _validate_directions(directions: list[str]) -> None:
        """Raise ValueError if *directions* contains invalid characters.

        Args:
            directions: The list of direction strings to validate.

        Raises:
            ValueError: If any element is not ``'N'``, ``'E'``, ``'S'``,
                or ``'W'``.
        """
        valid = frozenset("NESW")
        for letter in directions:
            if letter not in valid:
                raise ValueError(
                    f"Invalid direction '{letter}' in path. "
                    f"Expected one of: N, E, S, W."
                )
