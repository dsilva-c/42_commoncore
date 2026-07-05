"""
alchemy/grimoire/spellbook.py - Records spells and their effects.

Uses a *late import* (import inside the function) to avoid any potential
circular dependency between spellbook and validator.
"""


def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Record a spell after validating its ingredients.

    Uses a late import of validate_ingredients to demonstrate how circular
    dependencies can be broken at the function level.

    Returns a confirmation string indicating whether the spell was recorded
    or rejected.
    """
    # Late import - avoids circular dependency at module load time
    from .validator import validate_ingredients  # noqa: PLC0415

    validation_result: str = validate_ingredients(ingredients)
    if "- VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
