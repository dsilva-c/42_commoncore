"""
Making Your Own Error Types
Exercise 2: ft_custom_errors

This module demonstrates creating custom exception classes
for garden-specific error handling.
"""


class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for water-related problems."""
    pass


def check_plant_status(plant_name: str, status: str) -> None:
    """
    Checks plant status and raises PlantError if issues detected.

    Args:
        plant_name: Name of the plant
        status: Current status of the plant

    Raises:
        PlantError: If plant has issues
    """
    if status == "wilting":
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_level(level: int) -> None:
    """
    Checks water tank level and raises WaterError if insufficient.

    Args:
        level: Current water level

    Raises:
        WaterError: If water level is too low
    """
    if level < 20:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """
    Demonstrates the use of custom exception types
    for garden management.
    """
    print("=== Custom Garden Errors Demo ===")
    print()

    # Test PlantError
    print("Testing PlantError...")
    try:
        check_plant_status("tomato", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    # Test WaterError
    print("Testing WaterError...")
    try:
        check_water_level(10)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    # Test catching all garden errors together
    print("Testing catching all garden errors...")
    errors_to_test = [
        lambda: check_plant_status("tomato", "wilting"),
        lambda: check_water_level(5)
    ]

    for error_func in errors_to_test:
        try:
            error_func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
