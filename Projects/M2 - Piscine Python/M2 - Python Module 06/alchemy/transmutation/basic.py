"""
alchemy/transmutation/basic.py - Basic transmutation spells.

Uses absolute imports from the main alchemy package.
"""

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmute lead into gold using the fire element."""
    fire_result: str = create_fire()
    return f"Lead transmuted to gold using {fire_result}"


def stone_to_gem() -> str:
    """Transmute stone into gem using the earth element."""
    earth_result: str = create_earth()
    return f"Stone transmuted to gem using {earth_result}"
