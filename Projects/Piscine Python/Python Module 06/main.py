#!/usr/bin/env python3
"""
The Alchemist's Codex - Automated Test Suite
Module 06: Mastering Python's Import Mysteries

Tests all four sacred mysteries:
  Part I   - Sacred Scroll  (__init__.py)
  Part II  - Import Transmutation (from...import)
  Part III - Pathway Debate (absolute vs relative)
  Part IV  - Breaking the Circular Curse (dependency resolution)

Usage:
    python3 main.py           # run all tests
    python3 main.py -v        # verbose output
    python3 main.py --help    # show this help
"""

import sys
from typing import List, Tuple


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

VERBOSE: bool = "-v" in sys.argv or "--verbose" in sys.argv

PASS = "  [PASS]"
FAIL = "  [FAIL]"


def check(
    description: str,
    result: str,
    expected: str,
) -> Tuple[bool, str]:
    """Compare *result* to *expected* and return (ok, message)."""
    ok = result == expected
    symbol = PASS if ok else FAIL
    msg = f"{symbol} {description}"
    if not ok or VERBOSE:
        msg += f"\n         got     : {result!r}"
        if not ok:
            msg += f"\n         expected: {expected!r}"
    return ok, msg


def section(title: str) -> None:
    """Print a section header."""
    width = 60
    print(f"\n{'─' * width}")
    print(f"  {title}")
    print(f"{'─' * width}")


# ─────────────────────────────────────────────────────────────────────────────
# Part I – Sacred Scroll
# ─────────────────────────────────────────────────────────────────────────────

def test_sacred_scroll() -> List[Tuple[bool, str]]:
    """Test __init__.py package interface control."""
    results: List[Tuple[bool, str]] = []

    import alchemy
    import alchemy.elements

    # Direct module access – all four elements exposed
    results.append(check(
        "elements.create_fire()",
        alchemy.elements.create_fire(),
        "Fire element created",
    ))
    results.append(check(
        "elements.create_water()",
        alchemy.elements.create_water(),
        "Water element created",
    ))
    results.append(check(
        "elements.create_earth()",
        alchemy.elements.create_earth(),
        "Earth element created",
    ))
    results.append(check(
        "elements.create_air()",
        alchemy.elements.create_air(),
        "Air element created",
    ))

    # Package-level access – only fire and water are exposed
    results.append(check(
        "alchemy.create_fire() exposed",
        alchemy.create_fire(),
        "Fire element created",
    ))
    results.append(check(
        "alchemy.create_water() exposed",
        alchemy.create_water(),
        "Water element created",
    ))

    # create_earth and create_air must NOT be exposed at package level
    try:
        alchemy.create_earth()  # type: ignore[attr-defined]
        results.append((
            False,
            f"{FAIL} alchemy.create_earth() should raise AttributeError",
        ))
    except AttributeError:
        results.append((
            True,
            f"{PASS} alchemy.create_earth() raises AttributeError "
            "(not exposed)",
        ))

    try:
        alchemy.create_air()  # type: ignore[attr-defined]
        results.append((
            False,
            f"{FAIL} alchemy.create_air() should raise AttributeError",
        ))
    except AttributeError:
        results.append((
            True,
            f"{PASS} alchemy.create_air() raises AttributeError "
            "(not exposed)",
        ))

    # Metadata
    results.append(check("alchemy.__version__", alchemy.__version__, "1.0.0"))
    results.append(check(
        "alchemy.__author__", alchemy.__author__, "Master Pythonicus",
    ))

    return results


# ─────────────────────────────────────────────────────────────────────────────
# Part II – Import Transmutation
# ─────────────────────────────────────────────────────────────────────────────

def test_import_transmutation() -> List[Tuple[bool, str]]:
    """Test different import styles and potion functions."""
    results: List[Tuple[bool, str]] = []

    # Method 1 – full module import
    import alchemy.elements
    results.append(check(
        "Method 1 – full module import: create_fire",
        alchemy.elements.create_fire(),
        "Fire element created",
    ))

    # Method 2 – specific function import
    from alchemy.elements import create_water
    results.append(check(
        "Method 2 – specific import: create_water",
        create_water(),
        "Water element created",
    ))

    # Method 3 – aliased import
    from alchemy.potions import healing_potion as heal
    results.append(check(
        "Method 3 – aliased import: heal()",
        heal(),
        "Healing potion brewed with Fire element created "
        "and Water element created",
    ))

    # Method 4 – multiple imports
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    results.append(check(
        "Method 4 – multiple imports: create_earth",
        create_earth(),
        "Earth element created",
    ))
    results.append(check(
        "Method 4 – multiple imports: create_fire",
        create_fire(),
        "Fire element created",
    ))
    results.append(check(
        "Method 4 – multiple imports: strength_potion",
        strength_potion(),
        "Strength potion brewed with Earth element created "
        "and Fire element created",
    ))

    # Additional potions
    from alchemy.potions import invisibility_potion, wisdom_potion
    results.append(check(
        "invisibility_potion()",
        invisibility_potion(),
        "Invisibility potion brewed with Air element created "
        "and Water element created",
    ))
    results.append(check(
        "wisdom_potion()",
        wisdom_potion(),
        "Wisdom potion brewed with all elements: Fire element created, "
        "Water element created, Earth element created, Air element created",
    ))

    return results


# ─────────────────────────────────────────────────────────────────────────────
# Part III – Pathway Debate
# ─────────────────────────────────────────────────────────────────────────────

def test_pathway_debate() -> List[Tuple[bool, str]]:
    """Test absolute vs relative imports via the transmutation package."""
    results: List[Tuple[bool, str]] = []

    # Absolute imports (basic.py)
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    results.append(check(
        "Absolute import: lead_to_gold()",
        lead_to_gold(),
        "Lead transmuted to gold using Fire element created",
    ))
    results.append(check(
        "Absolute import: stone_to_gem()",
        stone_to_gem(),
        "Stone transmuted to gem using Earth element created",
    ))

    # Relative imports (advanced.py)
    from alchemy.transmutation.advanced import (
        philosophers_stone,
        elixir_of_life,
    )
    results.append(check(
        "Relative import: philosophers_stone()",
        philosophers_stone(),
        "Philosopher's stone created using Lead transmuted to gold using "
        "Fire element created and Healing potion brewed with "
        "Fire element created and Water element created",
    ))
    results.append(check(
        "Relative import: elixir_of_life()",
        elixir_of_life(),
        "Elixir of life: eternal youth achieved!",
    ))

    # Package-level access via transmutation/__init__.py
    import alchemy.transmutation
    results.append(check(
        "Package-level: alchemy.transmutation.lead_to_gold()",
        alchemy.transmutation.lead_to_gold(),
        "Lead transmuted to gold using Fire element created",
    ))
    results.append(check(
        "Package-level: alchemy.transmutation.philosophers_stone()",
        alchemy.transmutation.philosophers_stone(),
        "Philosopher's stone created using Lead transmuted to gold using "
        "Fire element created and Healing potion brewed with "
        "Fire element created and Water element created",
    ))

    return results


# ─────────────────────────────────────────────────────────────────────────────
# Part IV – Circular Curse
# ─────────────────────────────────────────────────────────────────────────────

def test_circular_curse() -> List[Tuple[bool, str]]:
    """Test grimoire package and late-import circular-dependency solution."""
    results: List[Tuple[bool, str]] = []

    from alchemy.grimoire.validator import validate_ingredients
    from alchemy.grimoire.spellbook import record_spell

    # Validator
    results.append(check(
        "validate_ingredients('fire air') → VALID",
        validate_ingredients("fire air"),
        "fire air - VALID",
    ))
    results.append(check(
        "validate_ingredients('dragon scales') → INVALID",
        validate_ingredients("dragon scales"),
        "dragon scales - INVALID",
    ))
    results.append(check(
        "validate_ingredients('water') → VALID",
        validate_ingredients("water"),
        "water - VALID",
    ))
    results.append(check(
        "validate_ingredients('earth') → VALID",
        validate_ingredients("earth"),
        "earth - VALID",
    ))

    # Spellbook
    results.append(check(
        "record_spell('Fireball', 'fire air') → recorded",
        record_spell("Fireball", "fire air"),
        "Spell recorded: Fireball (fire air - VALID)",
    ))
    results.append(check(
        "record_spell('Dark Magic', 'shadow') → rejected",
        record_spell("Dark Magic", "shadow"),
        "Spell rejected: Dark Magic (shadow - INVALID)",
    ))
    results.append(check(
        "record_spell('Lightning', 'air') → recorded (late import)",
        record_spell("Lightning", "air"),
        "Spell recorded: Lightning (air - VALID)",
    ))

    # Grimoire package-level access
    from alchemy.grimoire import validate_ingredients as vi, record_spell as rs
    results.append(check(
        "grimoire package-level: validate_ingredients('fire')",
        vi("fire"),
        "fire - VALID",
    ))
    results.append(check(
        "grimoire package-level: record_spell('Test', 'shadow')",
        rs("Test", "shadow"),
        "Spell rejected: Test (shadow - INVALID)",
    ))

    return results


# ─────────────────────────────────────────────────────────────────────────────
# Main runner
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    """Run the full test suite and print a summary."""
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        return

    all_results: List[Tuple[bool, str]] = []
    parts = [
        ("Part I   – The Sacred Scroll", test_sacred_scroll),
        ("Part II  – Import Transmutation", test_import_transmutation),
        ("Part III – The Great Pathway Debate", test_pathway_debate),
        ("Part IV  – Breaking the Circular Curse", test_circular_curse),
    ]

    print("╔══════════════════════════════════════════════════════════╗")
    print("║  The Alchemist's Codex – Module 06 Test Suite           ║")
    print("╚══════════════════════════════════════════════════════════╝")

    for title, test_fn in parts:
        section(title)
        part_results = test_fn()
        for ok, msg in part_results:
            print(msg)
        all_results.extend(part_results)

    passed = sum(1 for ok, _ in all_results if ok)
    total = len(all_results)
    failed = total - passed

    print(f"\n{'─' * 60}")
    print(f"  RESULTS: {passed}/{total} tests passed", end="")
    if failed:
        print(f"  ({failed} failed)")
    else:
        print("  – All mysteries mastered!")
    print(f"{'─' * 60}")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
