#!/usr/bin/env python3

"""
Exercise 4: Garden Security System
Secure plant class with data validation and encapsulation.
"""


class SecurePlant:
    """A plant with protected data and validation."""

    def __init__(self, name: str) -> None:
        """
        Initialize a secure plant.

        Args:
            name: The plant's name
        """
        self.__name: str = name
        self.__height: int = 0
        self.__age: int = 0

    def set_height(self, height: int) -> None:
        """
        Set the plant's height with validation.

        Args:
            height: New height in centimeters
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Set the plant's age with validation.

        Args:
            age: New age in days
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Get the plant's height."""
        return self.__height

    def get_age(self) -> int:
        """Get the plant's age."""
        return self.__age

    def get_name(self) -> str:
        """Get the plant's name."""
        return self.__name

    def get_info(self) -> str:
        """Get formatted information about the plant."""
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


def main() -> None:
    """Demonstrate the garden security system."""
    print("=== Garden Security System ===")

    # Create a secure plant
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.get_name()}")

    # Set valid values
    rose.set_height(25)
    rose.set_age(30)
    print()

    # Attempt invalid operation
    rose.set_height(-5)
    print()

    # Display current state
    print(f"Current plant: {rose.get_info()}")


if __name__ == "__main__":
    main()
