"""ex0 — Card Foundation demonstration."""

from typing import Any

from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", dragon.is_playable(6))
    game_state: dict[str, Any] = {}
    print("Play result:", dragon.play(game_state))

    class DummyTarget:
        name = "Goblin Warrior"

    print("Fire Dragon attacks Goblin Warrior:")
    print("Attack result:", dragon.attack_target(DummyTarget()))

    print("Testing insufficient mana (3 available):")
    print("Playable:", dragon.is_playable(3))

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
