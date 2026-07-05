#!/usr/bin/env python3

"""
Exercise 3: Plant Factory
Plant class with constructor for efficient initialization.
"""


class Plant:
    """A plant with streamlined initialization."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a plant with its starting values.

        Args:
            name: The plant's name
            height: Starting height in centimeters
            age: Starting age in days
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Get formatted information about the plant."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


def main() -> None:
    """Create multiple plants using the plant factory."""
    # Create plants with varying characteristics
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    # Display all created plants
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.get_info()}")

    print()
    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
