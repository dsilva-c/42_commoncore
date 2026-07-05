"""Concrete spell card — instant magical effects (one-time use)."""

from typing import Any

from ex0.Card import Card


class SpellCard(Card):
    """A spell that is consumed when played."""

    # Map effect types to human-readable template strings.
    _EFFECT_DESCRIPTIONS: dict[str, str] = {
        "damage": "Deal {cost} damage to target",
        "heal": "Restore {heal} health",
        "buff": "Grant +{cost} to a friendly creature",
        "debuff": "Apply -{cost} to an enemy creature",
    }

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    # ------------------------------------------------------------------
    # Implement abstract method from Card
    # ------------------------------------------------------------------

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Cast the spell — it is consumed on use."""
        template = self._EFFECT_DESCRIPTIONS.get(
            self.effect_type, "{effect_type} effect applied"
        )
        effect = template.format(
            cost=self.cost,
            heal=self.cost * 2,
            effect_type=self.effect_type,
        )
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect,
        }

    # ------------------------------------------------------------------
    # Override / extend concrete methods
    # ------------------------------------------------------------------

    def get_card_info(self) -> dict[str, Any]:
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info

    # ------------------------------------------------------------------
    # Spell-specific method
    # ------------------------------------------------------------------

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        """Resolve the spell effect against a list of targets."""
        target_names = [
            t.name if hasattr(t, "name") else str(t) for t in targets
        ]
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": target_names,
            "resolved": True,
        }
