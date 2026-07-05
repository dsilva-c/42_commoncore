"""
Different Types of Problems
Exercise 1: ft_different_errors

This module demonstrates handling different types of exceptions
that can occur in garden operations.
"""

from typing import Union


def garden_operations() -> None:
    """
    Demonstrates various types of errors that can occur
    in garden management operations.
    """
    pass  # Used as placeholder for individual demonstrations


def test_error_types() -> None:
    """
    Tests and demonstrates different types of Python exceptions
    in the context of garden operations.
    """
    print("=== Garden Error Types Demo ===")
    print()

    # Test ValueError
    print("Testing ValueError...")
    try:
        # Trying to convert invalid data to integer
        _ = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int() with base 10")
    print()

    # Test ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        # Trying to calculate average with zero plants
        total_water = 100
        num_plants = 0
        _ = total_water / num_plants
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    # Test FileNotFoundError
    print("Testing FileNotFoundError...")
    try:
        # Trying to open a file that doesn't exist
        with open("missing.txt", "r") as file:
            _ = file.read()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    # Test KeyError
    print("Testing KeyError...")
    try:
        # Trying to access a key that doesn't exist in dictionary
        garden_data = {"tomato": 5, "lettuce": 3}
        _ = garden_data["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print()

    # Test catching multiple error types together
    print("Testing multiple errors together...")
    test_values: list[Union[str, int, None]] = ["abc", 0, None]

    for value in test_values:
        try:
            if value is None:
                # This will cause AttributeError
                _ = value.upper()  # type: ignore
            elif value == 0:
                # This will cause ZeroDivisionError
                _ = 100 / value  # type: ignore
            else:
                # This will cause ValueError
                _ = int(value)  # type: ignore
        except (ValueError, ZeroDivisionError, AttributeError):
            print("Caught an error, but program continues!")
            break
    print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
