"""ex0 — Lambda Sanctum: mastering anonymous functions.

File to submit: lambda_spells.py
Authorized:    map, filter, sorted, print()

All transformations must use lambda expressions — the 'def' keyword
is forbidden for simple operations inside these functions.
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by 'power' level (descending).

    Args:
        artifacts: list of dicts with keys 'name', 'power', 'type'.

    Returns:
        New list sorted from highest to lowest power.
    """
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages whose power is greater than or equal to min_power.

    Args:
        mages:     list of dicts with keys 'name', 'power', 'element'.
        min_power: minimum power threshold (inclusive).

    Returns:
        List of mage dicts that meet or exceed the threshold.
    """
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name with "* " prefix and " *" suffix.

    Args:
        spells: list of spell name strings.

    Returns:
        List of transformed spell strings, e.g. "* fireball *".
    """
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate power statistics for a list of mages.

    Args:
        mages: list of dicts with a 'power' key.

    Returns:
        Dict with keys 'max_power' (int), 'min_power' (int),
        'avg_power' (float, rounded to 2 decimals).
    """
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers, key=lambda x: x),
        'min_power': min(powers, key=lambda x: x),
        'avg_power': round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    """Demonstrate lambda_spells functions with sample data."""
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff',   'power': 92, 'type': 'weapon'},
        {'name': 'Ice Wand',     'power': 78, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 67, 'type': 'weapon'},
    ]

    mages = [
        {'name': 'Alex',    'power': 95, 'element': 'fire'},
        {'name': 'Jordan',  'power': 60, 'element': 'ice'},
        {'name': 'Riley',   'power': 80, 'element': 'lightning'},
        {'name': 'Casey',   'power': 45, 'element': 'earth'},
        {'name': 'Morgan',  'power': 72, 'element': 'wind'},
    ]

    spells = ['fireball', 'heal', 'shield']

    # artifact_sorter
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    # power_filter
    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 70)
    print(f"Mages with power >= 70: {[m['name'] for m in strong_mages]}")

    # spell_transformer
    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(' '.join(transformed))

    # mage_stats
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max: {stats['max_power']}, "
        f"Min: {stats['min_power']}, "
        f"Avg: {stats['avg_power']}"
    )


if __name__ == "__main__":
    main()
