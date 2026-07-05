#!/usr/bin/env python3

"""
Exercise 2: Plant Growth Simulator
Plant class with methods to simulate growth and aging.
"""


class Plant:
    """A plant that can grow and age over time."""

    name: str
    height: int  # in centimeters
    age: int  # in days

    def grow(self) -> None:
        """Increase the plant's height by 1cm."""
        self.height += 1

    def age_one_day(self) -> None:
        """Increase the plant's age by 1 day."""
        self.age += 1

    def get_info(self) -> str:
        """Get formatted information about the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """Simulate plant growth over a week."""
    # Create a plant
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30

    # Record initial state
    initial_height = rose.height

    print("=== Day 1 ===")
    print(rose.get_info())

    # Simulate a week of growth
    for _ in range(7):
        rose.grow()
        rose.age_one_day()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")


if __name__ == "__main__":
    main()
