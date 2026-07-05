"""Concrete artifact card — permanent game modifiers."""

from typing import Any

from ex0.Card import Card


class ArtifactCard(Card):
    """An artifact that remains in play until destroyed."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    # ------------------------------------------------------------------
    # Implement abstract method from Card
    # ------------------------------------------------------------------

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Deploy the artifact to the battlefield."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    # ------------------------------------------------------------------
    # Override / extend concrete methods
    # ------------------------------------------------------------------

    def get_card_info(self) -> dict[str, Any]:
        info = super().get_card_info()
        info["type"] = "Artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info

    # ------------------------------------------------------------------
    # Artifact-specific method
    # ------------------------------------------------------------------

    def activate_ability(self) -> dict[str, Any]:
        """Trigger the artifact's ongoing ability."""
        return {
            "artifact": self.name,
            "ability": self.effect,
            "durability_remaining": self.durability,
            "activated": True,
        }
