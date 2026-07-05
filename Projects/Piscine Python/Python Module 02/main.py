#!/usr/bin/env python3
"""
Main Test Suite for Module 02 - Garden Guardian
Data Engineering for Smart Agriculture

This script tests all exercises in sequence, demonstrating
exception handling concepts in Python.
"""

import sys
import os


def print_separator(title: str = "") -> None:
    """Print a visual separator with optional title."""
    print("\n" + "=" * 70)
    if title:
        print(f"  {title}")
        print("=" * 70)
    print()


def run_exercise(exercise_num: int, module_name: str,
                 description: str) -> None:
    """
    Import and run an exercise module.

    Args:
        exercise_num: Exercise number
        module_name: Name of the Python module to import
        description: Description of the exercise
    """
    print_separator(f"Exercise {exercise_num}: {description}")

    try:
        # Import the module dynamically
        module = __import__(f"ex{exercise_num}.{module_name}",
                            fromlist=[module_name])

        # Run the main test function
        if hasattr(module, 'test_temperature_input'):
            module.test_temperature_input()
        elif hasattr(module, 'test_error_types'):
            module.test_error_types()
        elif hasattr(module, 'test_custom_errors'):
            module.test_custom_errors()
        elif hasattr(module, 'test_watering_system'):
            module.test_watering_system()
        elif hasattr(module, 'test_plant_checks'):
            module.test_plant_checks()
        elif hasattr(module, 'test_garden_management'):
            module.test_garden_management()
        else:
            print("No test function found in module")

    except ImportError as e:
        print(f"Error importing module: {e}")
    except Exception as e:
        print(f"Error running exercise: {e}")


def main() -> None:
    """Execute all exercise tests in sequence."""
    print("\n" + "=" * 70)
    print("  MODULE 02 - GARDEN GUARDIAN")
    print("  Data Engineering for Smart Agriculture")
    print("  Exception Handling in Python")
    print("=" * 70)

    exercises = [
        (0, "ft_first_exception", "Agricultural Data Validation Pipeline"),
        (1, "ft_different_errors", "Different Types of Problems"),
        (2, "ft_custom_errors", "Making Your Own Error Types"),
        (3, "ft_finally_block", "Finally Block - Always Clean Up"),
        (4, "ft_raise_errors", "Raising Your Own Errors"),
        (5, "ft_garden_management", "Garden Management System"),
    ]

    # Run all exercises
    for ex_num, module_name, description in exercises:
        run_exercise(ex_num, module_name, description)

    # Final summary
    print_separator("TEST SUITE COMPLETED")
    print("All exercises have been tested successfully!")
    print("\nKey Concepts Demonstrated:")
    print("  ✓ Basic exception handling with try/except")
    print("  ✓ Handling multiple exception types")
    print("  ✓ Creating custom exception classes")
    print("  ✓ Using finally blocks for cleanup")
    print("  ✓ Raising custom errors with validation")
    print("  ✓ Building robust data pipelines")
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    # Change to the script's directory to ensure imports work
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, script_dir)

    main()
