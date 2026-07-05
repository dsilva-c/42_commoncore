"""Deck management — stores, shuffles, and draws any Card subtype."""

import random

from ex0.Card import Card


class Deck:
    """Manages a collection of heterogeneous Card objects."""

    def __init__(self) -> None:
        self._cards: list[Card] = []

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def add_card(self, card: Card) -> None:
        """Append *card* to the deck."""
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove the first card with matching name.  Returns True if found."""
        for index, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(index)
                return True
        return False

    def shuffle(self) -> None:
        """Randomly reorder the deck in place."""
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        """Remove and return the top card; raise if the deck is empty."""
        if not self._cards:
            raise ValueError("Cannot draw from an empty deck")
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict[str, object]:
        """Return aggregate statistics about the current deck."""
        total = len(self._cards)
        avg_cost: float = (
            sum(c.cost for c in self._cards) / total if total > 0 else 0.0
        )
        creatures = sum(
            1
            for c in self._cards
            if c.get_card_info().get("type") == "Creature"
        )
        spells = sum(
            1
            for c in self._cards
            if c.get_card_info().get("type") == "Spell"
        )
        artifacts = sum(
            1
            for c in self._cards
            if c.get_card_info().get("type") == "Artifact"
        )
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
