#!/usr/bin/env python3
"""
ft_circular_curse.py - Part IV: Breaking the Circular Curse

Demonstrates how to identify and avoid circular import dependencies.

The chosen solution is Method 1 – Late Import:
  spellbook.record_spell() imports validator.validate_ingredients *inside*
  the function body, so the import only runs at call time rather than at
  module load time, breaking any potential circular dependency chain.
"""

from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def main() -> None:
    """Run the Circular Curse demonstration."""
    print("=== Circular Curse Breaking ===")

    # Ingredient validation
    print("Testing ingredient validation:")
    print(
        f'validate_ingredients("fire air"): '
        f'{validate_ingredients("fire air")}'
    )
    print(
        f'validate_ingredients("dragon scales"): '
        f'{validate_ingredients("dragon scales")}'
    )

    # Spell recording with validation
    print("Testing spell recording with validation:")
    print(
        f'record_spell("Fireball", "fire air"): '
        f'{record_spell("Fireball", "fire air")}'
    )
    print(
        f'record_spell("Dark Magic", "shadow"): '
        f'{record_spell("Dark Magic", "shadow")}'
    )

    # Late import technique showcase
    print("Testing late import technique:")
    print(
        f'record_spell("Lightning", "air"): '
        f'{record_spell("Lightning", "air")}'
    )
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
