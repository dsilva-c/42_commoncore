"""
alchemy/grimoire/validator.py - Validates spell ingredients.

Simple rule: ingredients containing one of the four classical elements are valid.
"""

VALID_ELEMENTS: list[str] = ["fire", "water", "earth", "air"]


def validate_ingredients(ingredients: str) -> str:
    """
    Validate spell ingredients.

    Returns "[ingredients] - VALID" if any classical element appears,
    otherwise returns "[ingredients] - INVALID".
    """
    lower: str = ingredients.lower()
    for element in VALID_ELEMENTS:
        if element in lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
