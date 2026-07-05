"""
alchemy/transmutation/advanced.py - Advanced transmutation spells.

Uses relative imports: from sibling module (basic.py) and parent package (potions.py).
"""

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create the Philosopher's Stone by combining lead_to_gold and healing_potion."""
    lead_result: str = lead_to_gold()
    healing_result: str = healing_potion()
    return f"Philosopher's stone created using {lead_result} and {healing_result}"


def elixir_of_life() -> str:
    """Distil the Elixir of Life."""
    return "Elixir of life: eternal youth achieved!"
