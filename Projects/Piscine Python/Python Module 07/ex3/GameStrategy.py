"""Abstract strategy interface.

Defines the contract for all game strategies.
"""

from abc import ABC, abstractmethod
from typing import Any


class GameStrategy(ABC):
    """Abstract base class for turn-execution strategies."""

    @abstractmethod
    def execute_turn(
        self, hand: list[Any], battlefield: list[Any]
    ) -> dict[str, Any]:
        """Execute a turn given the current hand and battlefield state."""

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the human-readable name of this strategy."""

    @abstractmethod
    def prioritize_targets(
        self, available_targets: list[Any]
    ) -> list[Any]:
        """Return *available_targets* sorted by strategic priority."""
