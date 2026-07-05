"""Thin re-export shim — allows ``from generator import MazeGenerator``."""

from mazegen.generator import MazeGenerator  # noqa: F401

__all__ = ["MazeGenerator"]
