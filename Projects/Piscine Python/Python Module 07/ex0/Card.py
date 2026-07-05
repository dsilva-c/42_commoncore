"""Abstract base class for all DataDeck cards."""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Rarity(Enum):
    """Allowed card rarities for DataDeck cards."""

    LEGENDARY = "Legendary"
    RARE = "Rare"
    UNCOMMON = "Uncommon"
    COMMON = "Common"


class Card(ABC):
    """Universal card blueprint.

    Every card type must implement this contract.
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if rarity not in {r.value for r in Rarity}:
            raise ValueError("Invalid rarity")
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    # ------------------------------------------------------------------
    # Abstract methods — concrete subclasses MUST implement these.
    # ------------------------------------------------------------------

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Play the card and return the result of the action."""

    # ------------------------------------------------------------------
    # Concrete methods — shared behaviour available to all cards.
    # ------------------------------------------------------------------

    def get_card_info(self) -> dict[str, Any]:
        """Return a dictionary describing the card."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Return True if the card can be played with the available mana."""
        return available_mana >= self.cost
