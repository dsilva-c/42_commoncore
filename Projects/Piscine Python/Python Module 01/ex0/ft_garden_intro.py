#!/usr/bin/env python3

"""
Exercise 0: Planting Your First Seed
Basic Python program execution demonstrating the entry point pattern.
"""


def main() -> None:
    """Main function displaying plant information."""
    # Store plant information in variables
    plant_name: str = "Rose"
    plant_height: int = 25  # in centimeters
    plant_age: int = 30  # in days

    # Display the plant information
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name}")
    print(f"Height: {plant_height}cm")
    print(f"Age: {plant_age} days")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
