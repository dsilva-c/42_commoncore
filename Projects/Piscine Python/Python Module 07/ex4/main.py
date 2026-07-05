"""ex4 — Tournament Platform demonstration."""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    # name, cost, rarity, attack, health
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 3, 4)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
        info = card.get_rank_info()
        print(f"{card.name} (ID: {card_id}):")
        print(f"- Interfaces: {card.get_tournament_stats()['interfaces']}")
        print(f"- Rating: {info['rating']}")
        print(f"- Record: {info['record']}")

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print("Match result:", match_result)

    print("Tournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
