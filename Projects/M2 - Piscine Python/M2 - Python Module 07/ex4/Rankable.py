"""Abstract ranking interface."""

from abc import ABC, abstractmethod
from typing import Any


class Rankable(ABC):
    """Interface for entities that participate in ranked competition."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Return the current ELO-style numeric rating."""

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Increment the win counter by *wins* and adjust the rating."""

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Increment the loss counter by *losses* and adjust the rating."""

    @abstractmethod
    def get_rank_info(self) -> dict[str, Any]:
        """Return a snapshot of this entity's ranking information."""
