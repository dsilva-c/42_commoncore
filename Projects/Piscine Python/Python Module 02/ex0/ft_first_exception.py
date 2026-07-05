"""
Agricultural Data Validation Pipeline
Exercise 0: ft_first_exception

This module demonstrates basic exception handling for validating
temperature sensor data in agricultural monitoring systems.
"""


def check_temperature(temp_str: str) -> float:
    """
    Validates and returns temperature reading from sensor data.

    Args:
        temp_str: String representation of temperature value

    Returns:
        float: Validated temperature value

    Raises:
        ValueError: If input is not a valid number or out of range
    """
    try:
        # Try to convert the string to a number
        temperature = float(temp_str)

        # Check if temperature is within reasonable range (0-40°C)
        if temperature < 0:
            raise ValueError(
                f"{temperature}°C is too cold for plants (min 0°C)"
            )
        elif temperature > 40:
            raise ValueError(
                f"{temperature}°C is too hot for plants (max 40°C)"
            )

        return temperature

    except ValueError as e:
        # Check if it's our custom error or a conversion error
        if "too cold" in str(e) or "too hot" in str(e):
            raise  # Re-raise our custom error
        else:
            raise ValueError(f"'{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    """
    Demonstrates temperature validation with various inputs.
    Tests normal cases and error scenarios.
    """
    print("=== Garden Temperature Checker ===")
    print()

    test_cases = ["25", "abc", "100", "-50"]

    for temp in test_cases:
        print(f"Testing temperature: {temp}")
        try:
            validated_temp = check_temperature(temp)
            print(f"Temperature {validated_temp}°C is perfect for plants!")
        except ValueError as e:
            print(f"Error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
