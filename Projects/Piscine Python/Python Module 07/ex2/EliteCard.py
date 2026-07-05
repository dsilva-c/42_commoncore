"""Elite card — multiple inheritance: Card + Combatable + Magical."""

from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """A powerful card that combines physical combat and magical abilities."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana: int,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power: int = attack
        self.health: int = health
        self.mana: int = mana
        # Defense value derived from attack power (used in defend())
        self._defense: int = max(0, attack - 2)

    # ------------------------------------------------------------------
    # Card abstract method
    # ------------------------------------------------------------------

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed with combat and magic abilities",
        }

    def get_card_info(self) -> dict[str, Any]:
        info = super().get_card_info()
        info["type"] = "Elite"
        info["attack"] = self.attack_power
        info["health"] = self.health
        info["mana"] = self.mana
        return info

    # ------------------------------------------------------------------
    # Combatable abstract methods
    # ------------------------------------------------------------------

    def attack(self, target: Any) -> dict[str, Any]:
        target_name: str = (
            target.name if hasattr(target, "name") else str(target)
        )
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        blocked = min(self._defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > taken,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {
            "attack": self.attack_power,
            "defense": self._defense,
            "health": self.health,
        }

    # ------------------------------------------------------------------
    # Magical abstract methods
    # ------------------------------------------------------------------

    def cast_spell(
        self, spell_name: str, targets: list[Any]
    ) -> dict[str, Any]:
        mana_used = len(targets) * 2
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_magic_stats(self) -> dict[str, Any]:
        return {
            "mana": self.mana,
            "spell_power": self.cost,
        }
