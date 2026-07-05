"""
Raising Your Own Errors
Exercise 4: ft_raise_errors

This module demonstrates raising custom errors when validation
checks fail in plant health monitoring.
"""


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> str:
    """
    Validates plant health parameters and raises errors for invalid values.

    Args:
        plant_name: Name of the plant (must not be empty)
        water_level: Water level (must be between 1 and 10)
        sunlight_hours: Hours of sunlight (must be between 2 and 12)

    Returns:
        str: Success message if all parameters are valid

    Raises:
        ValueError: If any parameter is invalid
    """
    # Check plant name
    if not plant_name or plant_name.strip() == "":
        raise ValueError("Plant name cannot be empty!")

    # Check water level
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    # Check sunlight hours
    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """
    Demonstrates raising and catching validation errors
    for plant health parameters.
    """
    print("=== Garden Plant Health Checker ===")
    print()

    # Test with good values
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test with empty plant name
    print("Testing empty plant name...")
    try:
        result = check_plant_health("", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test with bad water level
    print("Testing bad water level...")
    try:
        result = check_plant_health("lettuce", 15, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test with bad sunlight hours
    print("Testing bad sunlight hours...")
    try:
        result = check_plant_health("carrots", 5, 0)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
