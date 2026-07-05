import random


ACHIEVEMENTS = [
    "First Steps",
    "Sharp Mind",
    "Survivor",
    "Treasure Hunter",
    "Collector Supreme",
    "World Savior",
    "Boss Slayer",
    "Speed Runner",
    "Strategist",
    "Crafting Genius",
    "Untouchable",
    "Master Explorer",
    "Hidden Path Finder",
    "Unstoppable",
]


def gen_player_achievements() -> set[str]:
    """Generate a randomized achievement set for one player."""
    count = random.randint(4, 9)
    picks = random.sample(ACHIEVEMENTS, count)
    return set(picks)


def ft_achievement_tracker() -> None:
    """Track and analyze player achievements using sets."""
    print("=== Achievement Tracker System ===")

    players = ["Alice", "Bob", "Charlie", "Dylan"]
    player_sets: dict[str, set[str]] = {
        name: gen_player_achievements() for name in players
    }

    for name in players:
        print(f"Player {name}: {player_sets[name]}")

    all_distinct: set[str] = set()
    for achievements in player_sets.values():
        all_distinct = all_distinct.union(achievements)
    print(f"All distinct achievements: {all_distinct}")

    common_all = all_distinct
    for achievements in player_sets.values():
        common_all = common_all.intersection(achievements)
    print(f"Common achievements: {common_all}")

    for name in players:
        others: set[str] = set()
        for other_name in players:
            if other_name != name:
                others = others.union(player_sets[other_name])
        only_mine = player_sets[name].difference(others)
        print(f"Only {name} has: {only_mine}")

    for name in players:
        missing = all_distinct.difference(player_sets[name])
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    ft_achievement_tracker()
