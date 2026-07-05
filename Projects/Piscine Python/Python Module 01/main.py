#!/usr/bin/env python3

"""
Helper file for CodeCultivation - Object-Oriented Garden Systems.

This file helps you test your exercises easily.
Just run: python3 main.py

How it works:
1. It imports your exercise files from their subdirectories
2. It runs the main() function from each exercise (if they have one)
3. If there's an error, it tells you what went wrong

Your exercise files should be in ex0/, ex1/, ex2/, etc. subdirectories!
"""


def test_exercise(exercise_num: int, exercise_name: str) -> None:
    """
    Test an individual exercise by importing and running it.

    Args:
        exercise_num: The exercise directory number (0-6)
        exercise_name: The name of the exercise file
    """
    print(f"\n{'=' * 60}")
    print(f"Testing Exercise {exercise_num}: {exercise_name}")
    print('=' * 60)

    try:
        # Import the exercise module
        module_path = f"ex{exercise_num}.{exercise_name}"
        module = __import__(module_path, fromlist=[exercise_name])

        # Check if module has a main function
        if hasattr(module, 'main'):
            module.main()
        else:
            print(f"⚠️  No main() function found in {exercise_name}.py")
            print("   This exercise may need to be run directly.")

    except ImportError as e:
        print(
            f"❌ Could not import ex{exercise_num}/{exercise_name}.py"
        )
        print(f"   Error: {e}")
        print(
            f"   Make sure the file exists in "
            f"the ex{exercise_num}/ directory"
        )

    except Exception as e:
        print(f"❌ Error running {exercise_name}: {e}")
        print("   Check your code for errors")


def main():
    """Main function - runs when you execute: python3 main.py"""
    print("🌱 CodeCultivation - Object-Oriented Garden Systems 🌱")
    print("This helper will test your exercises for you.")
    print("\nAvailable exercises:")
    print()
    print("0 - ft_garden_intro      (Planting Your First Seed)")
    print("1 - ft_garden_data       (Garden Data Organizer)")
    print("2 - ft_plant_growth      (Plant Growth Simulator)")
    print("3 - ft_plant_factory     (Plant Factory)")
    print("4 - ft_garden_security   (Garden Security System)")
    print("5 - ft_plant_types       (Specialized Plant Types)")
    print("6 - ft_garden_analytics  (Garden Analytics Platform)")
    print("a - test all exercises")
    print()

    choice = input("Enter your choice: ").strip().lower()

    exercises = [
        (0, "ft_garden_intro"),
        (1, "ft_garden_data"),
        (2, "ft_plant_growth"),
        (3, "ft_plant_factory"),
        (4, "ft_garden_security"),
        (5, "ft_plant_types"),
        (6, "ft_garden_analytics"),
    ]

    if choice == "a":
        # Test all exercises
        for num, name in exercises:
            test_exercise(num, name)
    elif choice.isdigit() and 0 <= int(choice) <= 6:
        # Test specific exercise
        num = int(choice)
        test_exercise(num, exercises[num][1])
    else:
        print("❌ Invalid choice! Please enter 0-6 or 'a'")


if __name__ == "__main__":
    main()
