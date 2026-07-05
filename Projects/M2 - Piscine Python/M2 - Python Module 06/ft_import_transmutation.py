#!/usr/bin/env python3
"""
ft_import_transmutation.py - Part II: Import Transmutation

Demonstrates four different import styles:
  1. Full module import        – import alchemy.elements
  2. Specific function import  – from alchemy.elements import create_water
  3. Aliased import            – from alchemy.potions import healing_potion as heal
  4. Multiple imports          – from alchemy.elements import create_earth, create_fire
"""

# Method 1 – Full module import
import alchemy.elements

# Method 2 – Specific function import
from alchemy.elements import create_water

# Method 3 – Aliased import
from alchemy.potions import healing_potion as heal

# Method 4 – Multiple imports
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


def main() -> None:
    """Run the Import Transmutation demonstration."""
    print("=== Import Transmutation Mastery ===")

    # Method 1
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

    # Method 2
    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    # Method 3
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")

    # Method 4
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
