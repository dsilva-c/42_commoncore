"""ex3 — Game Engine demonstration."""

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {type(strategy).__name__}")
    print("Available types:", factory.get_supported_types())

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Simulating aggressive turn...")
    result = engine.simulate_turn()

    hand = result["hand"]
    hand_str = ", ".join(f"{c.name} ({c.cost})" for c in hand)
    print(f"Hand: [{hand_str}]")

    print("Turn execution:")
    print(f"Strategy: {result['strategy']}")
    print("Actions:", result["actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
