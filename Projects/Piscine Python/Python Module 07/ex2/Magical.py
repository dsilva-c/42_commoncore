"""Abstract magic interface."""

from abc import ABC, abstractmethod
from typing import Any


class Magical(ABC):
    """Interface for cards that can cast spells and channel mana."""

    @abstractmethod
    def cast_spell(
        self, spell_name: str, targets: list[Any]
    ) -> dict[str, Any]:
        """Cast a named spell at the given targets."""

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]:
        """Channel additional mana and return the updated mana state."""

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]:
        """Return a snapshot of the card's magical statistics."""
