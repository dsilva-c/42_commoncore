"""Game engine — orchestrates factory + strategy into a playable turn."""

from typing import Any, Optional

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Configures a card factory and strategy, then simulates game turns."""

    def __init__(self) -> None:
        self._factory: Optional[CardFactory] = None
        self._strategy: Optional[GameStrategy] = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Bind a *factory* and *strategy* to this engine."""
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        """Simulate one turn using the configured factory and strategy.

        Returns a dict with keys:
          - ``hand``:     list of Card objects dealt this turn
          - ``strategy``: strategy name string
          - ``actions``:  result dict from :meth:`GameStrategy.execute_turn`
        """
        if self._factory is None or self._strategy is None:
            return {}

        themed_deck = self._factory.create_themed_deck(3)
        hand: list[Any] = (
            themed_deck.get("creatures", [])
            + themed_deck.get("spells", [])
            + themed_deck.get("artifacts", [])
        )
        self._cards_created += len(hand)

        actions = self._strategy.execute_turn(hand, [])
        self._turns_simulated += 1
        self._total_damage += int(actions.get("damage_dealt", 0))

        return {
            "hand": hand,
            "strategy": self._strategy.get_strategy_name(),
            "actions": actions,
        }

    def get_engine_status(self) -> dict[str, Any]:
        """Return aggregate statistics about all simulated turns."""
        strategy_name = (
            self._strategy.get_strategy_name()
            if self._strategy is not None
            else "None"
        )
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self._total_damage,
            "cards_created": self._cards_created,
        }
