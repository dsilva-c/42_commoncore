"""Concrete aggressive strategy — prioritises cheap cards and direct damage."""

from typing import Any

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Play the cheapest cards first and deal maximum direct damage."""

    def __init__(self, mana_per_turn: int = 5) -> None:
        self._mana_per_turn: int = mana_per_turn

    # ------------------------------------------------------------------
    # GameStrategy abstract methods
    # ------------------------------------------------------------------

    def execute_turn(
        self, hand: list[Any], battlefield: list[Any]
    ) -> dict[str, Any]:
        """Play the cheapest cards first within the available mana budget."""
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        remaining_mana = self._mana_per_turn
        played: list[Any] = []

        for card in sorted_hand:
            if card.cost <= remaining_mana:
                played.append(card)
                remaining_mana -= card.cost

        # Aggressive bonus: each card deals 1.5× its mana cost in damage.
        # Formula avoids float arithmetic: ceil(cost * 1.5) == (cost*3+1)//2
        damage = sum((c.cost * 3 + 1) // 2 for c in played)
        targets = self.prioritize_targets(["Enemy Player"]) if played else []

        return {
            "cards_played": [c.name for c in played],
            "mana_used": self._mana_per_turn - remaining_mana,
            "targets_attacked": targets,
            "damage_dealt": damage,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(
        self, available_targets: list[Any]
    ) -> list[Any]:
        """Return all targets — aggressive strategies attack everything."""
        return list(available_targets)
