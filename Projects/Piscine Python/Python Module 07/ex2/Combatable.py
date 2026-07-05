"""Abstract combat interface."""

from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    """Interface for cards that can engage in physical combat."""

    @abstractmethod
    def attack(self, target: Any) -> dict[str, Any]:
        """Attack a target and return the combat result."""

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """Respond to an incoming attack and return the defence result."""

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]:
        """Return a snapshot of the card's combat statistics."""
