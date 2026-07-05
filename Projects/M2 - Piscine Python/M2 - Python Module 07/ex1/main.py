"""ex1 — Deck Builder demonstration."""

from typing import Any

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(
        ArtifactCard(
            "Mana Crystal", 2, "Common", 5, "Permanent: +1 mana per turn"
        )
    )

    print("Deck stats:", deck.get_deck_stats())

    deck.shuffle()

    print("Drawing and playing cards:")
    game_state: dict[str, Any] = {}
    while True:
        try:
            card = deck.draw_card()
        except ValueError:
            break
        card_type = card.get_card_info().get("type", "Unknown")
        print(f"Drew: {card.name} ({card_type})")
        print("Play result:", card.play(game_state))

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
