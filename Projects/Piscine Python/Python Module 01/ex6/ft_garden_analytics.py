from __future__ import annotations


"""
Exercise 6: Garden Analytics Platform
Comprehensive garden management with nested classes, inheritance chains,
and different method types.
"""


class Plant:
    """Base plant class."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant."""
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        """Make the plant grow by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    @staticmethod
    def is_valid_height(height: int) -> bool:
        """
        Validate if a height value is valid.

        Args:
            height: Height to validate

        Returns:
            True if valid, False otherwise
        """
        return height >= 0


class FloweringPlant(Plant):
    """A plant that can flower."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant."""
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = True

    def __str__(self) -> str:
        """String representation."""
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"({bloom_status})")


class PrizeFlower(FloweringPlant):
    """A prize-winning flowering plant."""

    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        """Initialize a prize flower."""
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def __str__(self) -> str:
        """String representation."""
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"({bloom_status}), Prize points: {self.prize_points}")


class GardenManager:
    """Manages multiple gardens and provides analytics."""

    # Class variable to track all gardens
    _all_gardens: list['GardenManager'] = []

    class GardenStats:
        """Nested helper class for calculating garden statistics."""

        def __init__(self) -> None:
            """Initialize statistics tracker."""
            self.plants_added: int = 0
            self.total_growth: int = 0
            self.regular_plants: int = 0
            self.flowering_plants: int = 0
            self.prize_flowers: int = 0

        def add_plant(self, plant: Plant) -> None:
            """
            Track a new plant addition.

            Args:
                plant: The plant being added
            """
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_flowers += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_plants += 1
            else:
                self.regular_plants += 1

        def record_growth(self) -> None:
            """Record growth event."""
            self.total_growth += 1

    def __init__(self, owner: str) -> None:
        """
        Initialize a garden manager.

        Args:
            owner: Name of the garden owner
        """
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.stats = GardenManager.GardenStats()
        GardenManager._all_gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden.

        Args:
            plant: The plant to add
        """
        self.plants.append(plant)
        self.stats.add_plant(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self) -> None:
        """Make all plants in the garden grow."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def get_garden_score(self) -> int:
        """
        Calculate total garden score based on all plants.

        Returns:
            Total score
        """
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    def print_report(self) -> None:
        """Print a comprehensive garden report."""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, (FloweringPlant, PrizeFlower)):
                print(f"- {plant}")
            else:
                print(f"- {plant.name}: {plant.height}cm")

        print(f"\nPlants added: {self.stats.plants_added}, "
              f"Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {self.stats.regular_plants} regular, "
              f"{self.stats.flowering_plants} flowering, "
              f"{self.stats.prize_flowers} prize flowers")

    @classmethod
    def create_garden_network(cls,
                              *owner_names: str) -> list[GardenManager]:
        """
        Create multiple connected gardens.

        Args:
            owner_names: Names of garden owners

        Returns:
            List of created garden managers
        """
        gardens = [cls(name) for name in owner_names]
        return gardens  # type: ignore[return-value]

    @classmethod
    def get_total_gardens(cls) -> int:
        """
        Get the total number of gardens created.

        Returns:
            Number of gardens
        """
        return len(cls._all_gardens)


def main() -> None:
    """Demonstrate the garden analytics platform."""
    print("=== Garden Management System Demo ===")
    print()

    # Create gardens using class method
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    # Add various plants to Alice's garden
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    print()

    # Add plants to Bob's garden
    maple = Plant("Maple", 80)
    bob_garden.add_plant(maple)
    print()

    # Grow all plants in Alice's garden
    alice_garden.grow_all_plants()
    print()

    # Print report
    alice_garden.print_report()
    print()

    # Test static method
    print(f"Height validation test: {Plant.is_valid_height(25)}")

    # Show garden scores
    print(f"Garden scores - Alice: {alice_garden.get_garden_score()}, "
          f"Bob: {bob_garden.get_garden_score()}")

    # Show total gardens managed
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")


if __name__ == "__main__":
    main()
