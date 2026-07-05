#!/usr/bin/env python3
"""
Main Test Suite for Module 03 - Data Quest
Mastering Python Collections for Data Engineering

This script tests all exercises in sequence, demonstrating
Python's collection data structures and comprehensions.
"""

import sys
import os
import subprocess


def print_separator(title: str = "") -> None:
    """Print a visual separator with optional title."""
    print("\n" + "=" * 70)
    if title:
        print(f"  {title}")
        print("=" * 70)
    print()


def run_command(
    cmd: list[str],
    description: str,
    input_text: str | None = None
) -> None:
    """Run a subprocess command and print its output."""
    print(f"Running: {' '.join(cmd)}")
    print("-" * 50)
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            input=input_text,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"STDERR: {result.stderr}")
    except Exception as e:
        print(f"Error running {description}: {e}")


def main() -> None:
    """Execute all exercise tests in sequence."""
    print("\n" + "=" * 70)
    print("  MODULE 03 - DATA QUEST")
    print("  Mastering Python Collections for Data Engineering")
    print("  Python Collections, Generators & Comprehensions")
    print("=" * 70)

    py = sys.executable

    print_separator("Exercise 0: Command Quest")
    run_command(
        [py, "ex0/ft_command_quest.py"],
        "ft_command_quest (no args)"
    )
    run_command(
        [py, "ex0/ft_command_quest.py", "hello", "world", "42"],
        "ft_command_quest (with args)"
    )
    run_command(
        [py, "ex0/ft_command_quest.py", "Data Quest"],
        "ft_command_quest (quoted arg)"
    )

    print_separator("Exercise 1: Score Cruncher")
    run_command(
        [py, "ex1/ft_score_analytics.py",
         "1500", "2300", "1800", "2100", "1950"],
        "ft_score_analytics"
    )
    run_command(
        [py, "ex1/ft_score_analytics.py"],
        "ft_score_analytics (no args)"
    )

    print_separator("Exercise 2: Position Tracker")
    run_command(
        [py, "ex2/ft_coordinate_system.py"],
        "ft_coordinate_system",
        "1.0,2.5,3.0\n4,5,6\n"
    )

    print_separator("Exercise 3: Achievement Hunter")
    run_command(
        [py, "ex3/ft_achievement_tracker.py"],
        "ft_achievement_tracker"
    )

    print_separator("Exercise 4: Inventory Master")
    run_command(
        [py, "ex4/ft_inventory_system.py",
         "sword:1", "potion:5", "shield:2", "armor:3", "helmet:1"],
        "ft_inventory_system"
    )
    run_command(
        [py, "ex4/ft_inventory_system.py"],
        "ft_inventory_system (no args)"
    )

    print_separator("Exercise 5: Stream Wizard")
    run_command(
        [py, "ex5/ft_data_stream.py"],
        "ft_data_stream"
    )

    print_separator("Exercise 6: Data Alchemist")
    run_command(
        [py, "ex6/ft_data_alchemist.py"],
        "ft_data_alchemist"
    )

    print_separator("TEST SUITE COMPLETED")
    print("All exercises have been tested successfully!")
    print("\nKey Concepts Demonstrated:")
    print("  - Command-line argument processing (sys.argv)")
    print("  - Lists for sequential data and analytics")
    print("  - Tuples for immutable 3D coordinates")
    print("  - Sets for unique achievement collections")
    print("  - Dictionaries for inventory management")
    print("  - Generators for memory-efficient streaming")
    print("  - Comprehensions for elegant data transformation")
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, script_dir)
    main()
