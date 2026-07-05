"""ex1 — Higher Realm: higher-order functions.

File to submit: higher_magic.py
Authorized:    callable(), print()

Functions that accept or return other functions — demonstrating
first-class citizenship of functions in Python.
"""

from collections.abc import Callable


Spell = Callable[[str, int], str]


def spell_combiner(
    spell1: Spell,
    spell2: Spell,
) -> Callable[[str, int], tuple[str, str]]:
    """Combine two spells into one that calls both with the same arguments.

    Args:
        spell1: first callable spell.
        spell2: second callable spell.

    Returns:
        A new callable that returns a tuple (result1, result2).
    """
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(
    base_spell: Spell,
    multiplier: int,
) -> Spell:
    """Amplify spell power before casting the base spell.

    Args:
        base_spell: callable that returns a number.
        multiplier: factor to multiply the result by.

    Returns:
        A new callable that multiplies the power argument before casting.
    """
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Spell,
) -> Spell:
    """Cast a spell only when the condition evaluates to True.

    Args:
        condition: callable that returns a bool.
        spell:     callable to execute when condition is True.

    Returns:
        A new callable that returns the spell result or "Spell fizzled".
    """
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(
    spells: list[Spell],
) -> Callable[[str, int], list[str]]:
    """Create a function that casts all spells in order.

    Args:
        spells: list of callables.

    Returns:
        A new callable that returns a list of each spell's result.
    """
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    """Demonstrate higher-order functions with sample spells."""
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    def frost(target: str, power: int) -> str:
        return f"Frost chills {target} for {power} damage"

    def is_powerful(target: str, power: int) -> bool:
        return power >= 20

    # spell_combiner
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    # power_amplifier
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original = fireball("Dragon", 10)
    amplified = mega_fireball("Dragon", 10)
    print(f"Original: {original}")
    print(f"Amplified: {amplified}")

    # conditional_caster
    print("\nTesting conditional caster...")
    conditional_fireball = conditional_caster(is_powerful, fireball)
    print(f"Power 25: {conditional_fireball('Ogre', 25)}")
    print(f"Power 10: {conditional_fireball('Ogre', 10)}")

    # spell_sequence
    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal, frost])
    results = seq("Goblin", 12)
    for r in results:
        print(f"  {r}")


if __name__ == "__main__":
    main()
