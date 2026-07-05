"""mazegen — Reusable maze generation library.

This package provides the core classes for generating, solving, and
inspecting mazes.  It is designed to be installed via pip and imported
independently of the A-Maze-ing project.

Quick start
-----------

.. code-block:: python

    from mazegen import MazeGenerator

    # Generate a 20×15 perfect maze with a fixed seed
    gen = MazeGenerator(20, 15, seed=42)
    grid = gen.generate()

    # Access the maze structure
    print(grid.width, grid.height)         # 20 15
    print(grid.has_wall(0, 0, 0))
    # True/False (North wall of top-left)

    # Get the short list of solution cells
    solution_cells = gen.get_solution()    # list of (x, y) tuples

    # Solve via MazeSolver
    from mazegen import MazeSolver
    solver = MazeSolver(grid)
    directions = solver.solve()            # ['N', 'E', 'S', …]

Custom parameters
-----------------

.. code-block:: python

    gen = MazeGenerator(
        width=30,
        height=20,
        seed=123,       # reproducible output; omit for random
        perfect=False,  # allow loops (extra passages added)
        algorithm="dfs" # only "dfs" supported in v1
    )
    grid = gen.generate(entry=(0, 0), exit_=(29, 19))
"""

from mazegen.generator import MazeGenerator
from mazegen.maze import (
    EAST,
    NORTH,
    OPPOSITE,
    SOUTH,
    WEST,
    Cell,
    MazeGrid,
)
from mazegen.solver import MazeSolver, NoPathError

__all__ = [
    # Main classes
    "MazeGenerator",
    "MazeGrid",
    "MazeSolver",
    "Cell",
    # Exceptions
    "NoPathError",
    # Direction constants
    "NORTH",
    "EAST",
    "SOUTH",
    "WEST",
    "OPPOSITE",
]

__version__ = "1.0.0"
__author__ = "dsilva-c, dasantos"
