"""Root-level re-export shim for mazegen.solver.

Allows ``from solver import MazeSolver, NoPathError`` during development
without installing the package.
"""

from mazegen.solver import MazeSolver, NoPathError  # noqa: F401

__all__ = ["MazeSolver", "NoPathError"]
