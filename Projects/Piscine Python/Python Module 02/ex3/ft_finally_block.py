"""
Finally Block - Always Clean Up
Exercise 3: ft_finally_block

This module demonstrates the use of finally blocks to ensure
cleanup operations always occur, even when errors happen.
"""

from typing import List, Optional


def water_plants(plant_list: List[Optional[str]]) -> None:
    """
    Waters a list of plants with proper resource management.

    Args:
        plant_list: List of plant names to water

    Raises:
        ValueError: If a plant name is invalid (None or empty)
    """
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    finally:
        # This cleanup always happens, regardless of errors
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Demonstrates that finally blocks execute even when errors occur.
    """
    print("=== Garden Watering System ===")
    print()

    # Test normal watering
    print("Testing normal watering...")
    try:
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test with error
    print("Testing with error...")
    try:
        water_plants(["tomato", None, "lettuce"])
        print("Watering completed successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
