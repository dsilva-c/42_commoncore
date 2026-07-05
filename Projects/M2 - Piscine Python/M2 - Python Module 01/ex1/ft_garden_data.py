#!/usr/bin/env python3

"""
Exercise 1: Garden Data Organizer
Creating a Plant class to organize plant data efficiently.
"""


class Plant:
    """Blueprint for a plant with basic attributes."""

    name: str
    height: int  # in centimeters
    age: int  # in days


def main() -> None:
    """Create and display multiple plants."""
    # Create plant instances
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 25
    plant1.age = 30

    plant2 = Plant()
    plant2.name = "Sunflower"
    plant2.height = 80
    plant2.age = 45

    plant3 = Plant()
    plant3.name = "Cactus"
    plant3.height = 15
    plant3.age = 120

    # Display plant registry
    print("=== Garden Plant Registry ===")
    print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")


if __name__ == "__main__":
    main()
