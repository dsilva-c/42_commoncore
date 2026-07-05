"""Tournament card — combines Card, Combatable, and Rankable interfaces."""

from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

# Base rating assigned by card rarity
_RARITY_BASE_RATING: dict[str, int] = {
    "Legendary": 1200,
    "Rare": 1150,
    "Uncommon": 1100,
    "Common": 1050,
}

# Points gained/lost per tournament match
_RATING_DELTA: int = 16


class TournamentCard(Card, Combatable, Rankable):
    """A card that can compete in a ranked tournament."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power: int = attack
        self.health: int = health
        self._defense: int = max(0, attack - 2)
        # Tournament record
        self.wins: int = 0
        self.losses: int = 0
        self._base_rating: int = _RARITY_BASE_RATING.get(rarity, 1000)
        self._rating_adjustment: int = 0

    # ------------------------------------------------------------------
    # Card abstract method
    # ------------------------------------------------------------------

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters the battlefield",
        }

    def get_card_info(self) -> dict[str, Any]:
        info = super().get_card_info()
        info["type"] = "Tournament"
        info["attack"] = self.attack_power
        info["health"] = self.health
        info["rating"] = self.calculate_rating()
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
    # Rankable abstract methods
    # ------------------------------------------------------------------

    def calculate_rating(self) -> int:
        return self._base_rating + self._rating_adjustment

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self._rating_adjustment += _RATING_DELTA * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self._rating_adjustment -= _RATING_DELTA * losses

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}",
        }

    # ------------------------------------------------------------------
    # Tournament-specific method
    # ------------------------------------------------------------------

    def get_tournament_stats(self) -> dict[str, Any]:
        return {
            "card": self.name,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses,
            "interfaces": ["Card", "Combatable", "Rankable"],
        }
