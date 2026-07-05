"""Concrete creature card implementation."""

from typing import Any

from ex0.Card import Card


class CreatureCard(Card):
    """A creature card that can be summoned to the battlefield."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        if attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if health <= 0:
            raise ValueError("Health must be a positive integer")
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    # ------------------------------------------------------------------
    # Implement abstract method from Card
    # ------------------------------------------------------------------

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Summon the creature to the battlefield."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    # ------------------------------------------------------------------
    # Override / extend concrete methods
    # ------------------------------------------------------------------

    def get_card_info(self) -> dict[str, Any]:
        """Return creature details including attack and health."""
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    # ------------------------------------------------------------------
    # Creature-specific method
    # ------------------------------------------------------------------

    def attack_target(self, target: Any) -> dict[str, Any]:
        """Attack another card or player target."""
        target_name: str = (
            target.name if hasattr(target, "name") else str(target)
        )
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
