"""
alchemy/potions.py - Advanced potion recipe functions.

Each potion combines elemental ingredients into powerful brews.
"""

from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    """Brew a healing potion using fire and water elements."""
    fire_result: str = create_fire()
    water_result: str = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    """Brew a strength potion using earth and fire elements."""
    earth_result: str = create_earth()
    fire_result: str = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    """Brew an invisibility potion using air and water elements."""
    air_result: str = create_air()
    water_result: str = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    """Brew a wisdom potion using all four elements."""
    fire_result: str = create_fire()
    water_result: str = create_water()
    earth_result: str = create_earth()
    air_result: str = create_air()
    all_four_results: str = (
        f"{fire_result}, {water_result}, {earth_result}, {air_result}"
    )
    return f"Wisdom potion brewed with all elements: {all_four_results}"
