"""Thin re-export shim — allows ``from maze import MazeGrid`` at project root.

All logic lives in :mod:`mazegen.maze` to keep the reusable library
as the single source of truth.
"""

from mazegen.maze import (  # noqa: F401
    DELTAS,
    EAST,
    NORTH,
    OPPOSITE,
    SOUTH,
    WEST,
    Cell,
    MazeGrid,
)

__all__ = [
    "Cell",
    "MazeGrid",
    "NORTH",
    "EAST",
    "SOUTH",
    "WEST",
    "OPPOSITE",
    "DELTAS",
]
