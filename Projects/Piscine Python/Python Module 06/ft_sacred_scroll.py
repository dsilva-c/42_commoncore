#!/usr/bin/env python3
"""
ft_sacred_scroll.py - Part I: The Sacred Scroll

Demonstrates how __init__.py controls the package interface:
  - Direct module access  (alchemy.elements.function)
  - Package-level access  (alchemy.function)
"""

import alchemy
import alchemy.elements


def main() -> None:
    """Run the Sacred Scroll demonstration."""
    print("=== Sacred Scroll Mastery ===")

    # ── Direct module access ──────────────────────────────────────────────
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire():  {alchemy.elements.create_fire()}")
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}"
    )
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}"
    )
    print(f"alchemy.elements.create_air():   {alchemy.elements.create_air()}")

    # ── Package-level access (controlled by __init__.py) ─────────────────
    print("Testing package-level access (controlled by __init__.py):")

    print(f"alchemy.create_fire():  {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        result = alchemy.create_earth()  # type: ignore[attr-defined]
        print(f"alchemy.create_earth(): {result}")
    except AttributeError as e:
        print(f"alchemy.create_earth(): AttributeError - not exposed ({e})")

    try:
        result = alchemy.create_air()  # type: ignore[attr-defined]
        print(f"alchemy.create_air(): {result}")
    except AttributeError as e:
        print(f"alchemy.create_air(): AttributeError - not exposed ({e})")

    # ── Package metadata ──────────────────────────────────────────────────
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
