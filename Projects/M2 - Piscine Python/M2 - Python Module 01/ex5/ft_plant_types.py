#!/usr/bin/env python3

"""
Exercise 5: Specialized Plant Types
Inheritance hierarchy with Flower, Tree, and Vegetable classes.
"""


class Plant:
    """Base plant class with common features."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a plant with basic attributes.

        Args:
            name: The plant's name
            height: Height in centimeters
            age: Age in days
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """A flowering plant with color."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a flower.

        Args:
            name: The flower's name
            height: Height in centimeters
            age: Age in days
            color: Flower color
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        """Make the flower bloom."""
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    """A tree with trunk diameter."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Initialize a tree.

        Args:
            name: The tree's name
            height: Height in centimeters
            age: Age in days
            trunk_diameter: Trunk diameter in centimeters
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:
        """Calculate shade production."""
        shade_area = self.trunk_diameter * 1.56  # Simplified calculation
        return f"{self.name} provides {shade_area:.0f} square meters of shade"


class Vegetable(Plant):
    """A vegetable plant with harvest information."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initialize a vegetable.

        Args:
            name: The vegetable's name
            height: Height in centimeters
            age: Age in days
            harvest_season: Season for harvesting
            nutritional_value: Key nutritional information
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_nutrition_info(self) -> str:
        """Get nutritional information."""
        return f"{self.name} is rich in {self.nutritional_value}"


def main() -> None:
    """Demonstrate specialized plant types."""
    print("=== Garden Plant Types ===")
    print()

    # Create flowers
    rose = Flower("Rose", 25, 30, "red")
    Flower("Tulip", 20, 25, "yellow")  # Second flower instance

    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, "
          f"{rose.color} color")
    print(rose.bloom())
    print()

    # Create trees
    oak = Tree("Oak", 500, 1825, 50)
    Tree("Pine", 600, 2190, 40)  # Second tree instance

    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
          f"{oak.trunk_diameter}cm diameter")
    print(oak.produce_shade())
    print()

    # Create vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    Vegetable("Carrot", 30, 75, "autumn", "beta-carotene")  # Second veg

    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, "
          f"{tomato.harvest_season} harvest")
    print(tomato.get_nutrition_info())


if __name__ == "__main__":
    main()
