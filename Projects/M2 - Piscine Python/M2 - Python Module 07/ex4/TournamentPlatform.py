"""Tournament platform — registers cards, runs matches, ranks participants."""

from typing import Any

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages a ranked tournament of TournamentCard participants."""

    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches: list[dict[str, Any]] = []
        # Per-name counters for generating unique IDs
        self._id_counters: dict[str, int] = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def register_card(self, card: TournamentCard) -> str:
        """Register *card* and return its unique tournament ID."""
        base_key = card.name.split()[-1].lower()
        self._id_counters[base_key] = (
            self._id_counters.get(base_key, 0) + 1
        )
        card_id = f"{base_key}_{self._id_counters[base_key]:03d}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        """Run a match between two registered cards.

        Updates their ratings as part of the match outcome.
        """
        missing: list[str] = [
            card_id
            for card_id in (card1_id, card2_id)
            if card_id not in self._cards
        ]
        if missing:
            return {
                "error": "Unknown card id",
                "missing_ids": missing,
            }
        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        # Determine winner by attack power; ties go to card1
        if card1.attack_power >= card2.attack_power:
            winner_id, loser_id = card1_id, card2_id
            winner, loser = card1, card2
        else:
            winner_id, loser_id = card2_id, card1_id
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)

        result: dict[str, Any] = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
        self._matches.append(result)
        return result

    def get_leaderboard(self) -> list[dict[str, Any]]:
        """Return cards sorted by rating descending with rank numbers."""
        sorted_cards = sorted(
            self._cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True,
        )
        leaderboard: list[dict[str, Any]] = []
        for rank, (card_id, card) in enumerate(sorted_cards, start=1):
            leaderboard.append({
                "rank": rank,
                "id": card_id,
                "name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}",
            })
        return leaderboard

    def generate_tournament_report(self) -> dict[str, Any]:
        """Return aggregate statistics for the current tournament state."""
        total_cards = len(self._cards)
        avg_rating = (
            sum(c.calculate_rating() for c in self._cards.values())
            // total_cards
            if total_cards > 0
            else 0
        )
        return {
            "total_cards": total_cards,
            "matches_played": len(self._matches),
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
