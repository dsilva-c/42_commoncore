#!/usr/bin/env python3
"""
ft_pathway_debate.py - Part III: The Great Pathway Debate

Demonstrates absolute vs relative imports through the transmutation package:
  - basic.py uses absolute imports  (from alchemy.elements import ...)
  - advanced.py uses relative imports (from .basic import ...,
    from ..potions import ...)
"""

# Direct imports from sub-modules (shows absolute path clearly)
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life

# Package-level imports (via transmutation/__init__.py)
import alchemy.transmutation


def main() -> None:
    """Run the Pathway Debate demonstration."""
    print("=== Pathway Debate Mastery ===")

    # Absolute imports (basic.py)
    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    # Relative imports (advanced.py)
    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    # Package-level access via __init__.py
    print("Testing Package Access:")
    print(
        "alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}"
    )
    print(
        "alchemy.transmutation.philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}"
    )

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
