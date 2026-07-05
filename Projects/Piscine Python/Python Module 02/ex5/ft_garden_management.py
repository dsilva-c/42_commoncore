"""
Garden Management System
Exercise 5: ft_garden_management

This module combines all error handling techniques learned
in this project into a comprehensive garden management system.
"""

from typing import Dict


class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for water-related problems."""
    pass


class GardenManager:
    """
    A garden management system that demonstrates comprehensive
    error handling techniques.
    """

    def __init__(self) -> None:
        """Initialize the garden manager with empty plant database."""
        self.plants: Dict[str, Dict[str, int]] = {}
        self.water_tank_level: int = 100

    def add_plant(self, name: str, water_level: int = 5,
                  sunlight_hours: int = 8) -> None:
        """
        Add a plant to the garden with validation.

        Args:
            name: Plant name
            water_level: Initial water level (1-10)
            sunlight_hours: Daily sunlight hours (2-12)

        Raises:
            ValueError: If parameters are invalid
            PlantError: If plant already exists
        """
        if not name or name.strip() == "":
            raise ValueError("Plant name cannot be empty!")

        if name in self.plants:
            raise PlantError(f"Plant '{name}' already exists!")

        if not 1 <= water_level <= 10:
            raise ValueError(
                f"Water level must be between 1 and 10, got {water_level}"
            )

        if not 2 <= sunlight_hours <= 12:
            raise ValueError(
                f"Sunlight hours must be between 2 and 12, "
                f"got {sunlight_hours}"
            )

        self.plants[name] = {
            "water": water_level,
            "sunlight": sunlight_hours
        }
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """
        Water all plants in the garden with proper cleanup.

        Raises:
            WaterError: If water tank is empty
        """
        if self.water_tank_level < 10:
            raise WaterError("Not enough water in tank")

        print("Opening watering system")
        try:
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
                self.water_tank_level -= 5
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str) -> str:
        """
        Check health of a specific plant.

        Args:
            name: Name of the plant to check

        Returns:
            str: Health status message

        Raises:
            KeyError: If plant doesn't exist
            ValueError: If plant parameters are invalid
        """
        if name not in self.plants:
            raise KeyError(f"Plant '{name}' not found in garden")

        plant = self.plants[name]
        water = plant["water"]
        sun = plant["sunlight"]

        # Validate current parameters
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if water < 1:
            raise ValueError(f"Water level {water} is too low (min 1)")

        return f"{name}: healthy (water: {water}, sun: {sun})"

    def refill_water_tank(self) -> None:
        """Refill the water tank to maximum capacity."""
        self.water_tank_level = 100
        print("Water tank refilled to 100")


def test_garden_management() -> None:
    """
    Comprehensive test demonstrating all error handling techniques
    in the garden management system.
    """
    print("=== Garden Management System ===")
    print()

    garden = GardenManager()

    # Test adding plants
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 4, 6)
        garden.add_plant("", 5, 8)  # This will fail
    except ValueError as e:
        print(f"Error adding plant: {e}")
    print()

    # Test watering plants with finally block
    print("Watering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Error: {e}")
    print()

    # Test checking plant health
    print("Checking plant health...")
    try:
        status = garden.check_plant_health("tomato")
        print(status)

        # Simulate corrupted data
        garden.plants["lettuce"]["water"] = 15
        status = garden.check_plant_health("lettuce")
        print(status)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")
    except KeyError as e:
        print(f"Error: {e}")
    print()

    # Test error recovery
    print("Testing error recovery...")
    garden.water_tank_level = 5  # Set low water level
    try:
        garden.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
        garden.refill_water_tank()
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
