"""Abstract factory interface — defines the contract for all card factories."""

from abc import ABC, abstractmethod
from typing import Any

from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory that produces themed groups of cards."""

    @abstractmethod
    def create_creature(
        self, name_or_power: str | int | None = None
    ) -> Card:
        """Create and return a creature card."""

    @abstractmethod
    def create_spell(
        self, name_or_power: str | int | None = None
    ) -> Card:
        """Create and return a spell card."""

    @abstractmethod
    def create_artifact(
        self, name_or_power: str | int | None = None
    ) -> Card:
        """Create and return an artifact card."""

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, list[Any]]:
        """Create a themed deck of *size* cards distributed by type."""

    @abstractmethod
    def get_supported_types(self) -> dict[str, list[str]]:
        """Return the card-type keys supported by this factory."""
