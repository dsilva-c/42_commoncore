"""ex2 — Ability System demonstration."""

from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical


def main() -> None:
    print("=== DataDeck Ability System ===")

    # Show which capabilities EliteCard provides
    card_methods = ["play", "get_card_info", "is_playable"]
    combat_methods = ["attack", "defend", "get_combat_stats"]
    magic_methods = ["cast_spell", "channel_mana", "get_magic_stats"]

    print("EliteCard capabilities:")
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    # name, cost, rarity, attack, health, mana
    warrior = EliteCard("Arcane Warrior", 5, "Rare", 5, 10, 4)

    print(f"Playing {warrior.name} (Elite Card):")

    print("Combat phase:")

    class DummyTarget:
        name = "Enemy"

    print("Attack result:", warrior.attack(DummyTarget()))
    print("Defense result:", warrior.defend(5))

    print("Magic phase:")
    print(
        "Spell cast:",
        warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"]),
    )
    print("Mana channel:", warrior.channel_mana(3))

    # Verify that EliteCard is truly an instance of all three interfaces
    assert isinstance(warrior, Combatable), "EliteCard must be Combatable"
    assert isinstance(warrior, Magical), "EliteCard must be Magical"

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
