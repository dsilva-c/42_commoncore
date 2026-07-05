import random


def ft_data_alchemist() -> None:
    """Demonstrate list and dict comprehensions."""
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {players}")

    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    capitalized_only = [name for name in players if name[:1].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")

    avg = round(sum(scores[name] for name in scores) / len(scores), 2)
    print(f"Score average is {avg}")

    high_scores = {name: scores[name] for name in scores if scores[name] > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
