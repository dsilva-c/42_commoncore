"""Concrete fantasy card factory — produces dragons, goblins, and magic."""

import random
from typing import Any

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Creates fantasy-themed cards.

    Includes dragons, goblins, and elemental spells.
    """

    # ------------------------------------------------------------------
    # Static card templates
    # ------------------------------------------------------------------

    _CREATURES: dict[str, tuple[str, int, str, int, int]] = {
        "dragon": ("Fire Dragon", 5, "Legendary", 7, 5),
        "fire dragon": ("Fire Dragon", 5, "Legendary", 7, 5),
        "goblin": ("Goblin Warrior", 2, "Common", 2, 1),
        "goblin warrior": ("Goblin Warrior", 2, "Common", 2, 1),
        "ice wizard": ("Ice Wizard", 4, "Rare", 3, 4),
        "lightning elemental": ("Lightning Elemental", 3, "Uncommon", 4, 2),
    }

    _SPELLS: dict[str, tuple[str, int, str, str]] = {
        "fireball": ("Fireball", 4, "Uncommon", "damage"),
        "lightning_bolt": ("Lightning Bolt", 3, "Common", "damage"),
        "lightning bolt": ("Lightning Bolt", 3, "Common", "damage"),
        "healing potion": ("Healing Potion", 2, "Common", "heal"),
        "shield spell": ("Shield Spell", 1, "Common", "buff"),
    }

    _ARTIFACTS: dict[str, tuple[str, int, str, int, str]] = {
        "mana_ring": (
            "Ring of Wisdom",
            4,
            "Rare",
            4,
            "Permanent: Draw an extra card each turn",
        ),
        "mana ring": (
            "Ring of Wisdom",
            4,
            "Rare",
            4,
            "Permanent: Draw an extra card each turn",
        ),
        "mana_crystal": (
            "Mana Crystal",
            2,
            "Common",
            5,
            "Permanent: +1 mana per turn",
        ),
    }

    # ------------------------------------------------------------------
    # CardFactory abstract methods
    # ------------------------------------------------------------------

    def create_creature(
        self, name_or_power: str | int | None = None
    ) -> Card:
        if isinstance(name_or_power, str):
            tpl = self._CREATURES.get(name_or_power.lower())
            if tpl:
                return CreatureCard(*tpl)
        if isinstance(name_or_power, int):
            power = max(1, name_or_power)
            return CreatureCard(
                f"Power Creature ({power})", power, "Common", power, power
            )
        # None → random
        key = random.choice(list(self._CREATURES.keys()))
        return CreatureCard(*self._CREATURES[key])

    def create_spell(
        self, name_or_power: str | int | None = None
    ) -> Card:
        if isinstance(name_or_power, str):
            tpl = self._SPELLS.get(name_or_power.lower())
            if tpl:
                return SpellCard(*tpl)
        if isinstance(name_or_power, int):
            power = max(1, name_or_power)
            return SpellCard(
                f"Power Spell ({power})", power, "Common", "damage"
            )
        key = random.choice(list(self._SPELLS.keys()))
        return SpellCard(*self._SPELLS[key])

    def create_artifact(
        self, name_or_power: str | int | None = None
    ) -> Card:
        if isinstance(name_or_power, str):
            tpl = self._ARTIFACTS.get(name_or_power.lower())
            if tpl:
                return ArtifactCard(*tpl)
        if isinstance(name_or_power, int):
            power = max(1, name_or_power)
            return ArtifactCard(
                f"Power Artifact ({power})",
                power,
                "Common",
                power,
                "Permanent: +1 effect",
            )
        key = random.choice(list(self._ARTIFACTS.keys()))
        return ArtifactCard(*self._ARTIFACTS[key])

    def create_themed_deck(self, size: int) -> dict[str, list[Any]]:
        """Create a balanced themed deck.

        For an aggressive deck the default split is:
        2 creatures + 1 spell (per 3-card group), scaled to *size*.
        """
        creatures: list[Any] = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
        ]
        spells: list[Any] = [
            self.create_spell("lightning_bolt"),
        ]
        artifacts: list[Any] = []

        # If size > 3 fill remaining slots proportionally
        current = len(creatures) + len(spells) + len(artifacts)
        keys = ["dragon", "goblin", "fireball", "mana_ring"]
        i = 0
        while current < size:
            key = keys[i % len(keys)]
            if key in self._CREATURES:
                creatures.append(self.create_creature(key))
            elif key in self._SPELLS:
                spells.append(self.create_spell(key))
            elif key in self._ARTIFACTS:
                artifacts.append(self.create_artifact(key))
            current += 1
            i += 1

        return {
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
        }

    def get_supported_types(self) -> dict[str, list[str]]:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
