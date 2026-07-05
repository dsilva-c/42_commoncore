#!/usr/bin/env python3
"""
Main Test Suite for Module 04 - The Cyber Archives
File I/O, Streams & Exception Handling

This script tests all exercises in sequence, demonstrating
Python's file operations, I/O streams, and exception handling.
"""

import sys
import os
import io
import stat

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
for ex in ["ex0", "ex1", "ex2", "ex3", "ex4"]:
    sys.path.insert(0, os.path.join(MODULE_DIR, ex))

from ft_ancient_text import recover_ancient_text
from ft_archive_creation import create_archive
from ft_stream_management import manage_streams
from ft_vault_security import secure_extraction, secure_preservation, vault_security_protocol
from ft_crisis_response import crisis_handler, run_crisis_response


def print_separator(title: str = "") -> None:
    """Print a visual separator with optional title."""
    print("\n" + "=" * 70)
    if title:
        print(f"  {title}")
        print("=" * 70)
    print()


def main() -> None:
    """Execute all exercise tests in sequence."""
    print("\n" + "=" * 70)
    print("  MODULE 04 - THE CYBER ARCHIVES")
    print("  File I/O, Streams & Exception Handling")
    print("  Context Managers, Exceptions & Standard Streams")
    print("=" * 70)

    # ------------------------------------------------------------------ ex0
    print_separator("Exercise 0: Ancient Text Recovery")

    print("--- Test 1: Existing file ---")
    recover_ancient_text("ancient_fragment.txt")
    print()

    print("--- Test 2: Another existing file ---")
    recover_ancient_text("classified_data.txt")
    print()

    print("--- Test 3: Non-existent file (FileNotFoundError expected) ---")
    try:
        recover_ancient_text("ghost_archive.txt")
    except FileNotFoundError as e:
        print(f"FileNotFoundError caught: {e}")

    # ------------------------------------------------------------------ ex1
    print_separator("Exercise 1: Archive Creation")

    print("--- Test 1: Create new_discovery.txt ---")
    create_archive("new_discovery.txt")
    print()

    print("--- Test 2: Verify written content ---")
    with open("new_discovery.txt", "r") as f:
        print(f.read())

    print("--- Test 3: Create a second archive ---")
    create_archive("test_archive.txt")
    print()

    if os.path.exists("test_archive.txt"):
        os.remove("test_archive.txt")
        print("test_archive.txt removed after test.")

    # ------------------------------------------------------------------ ex2
    print_separator("Exercise 2: Stream Management")
    print("(stdin mocked for automated testing)")
    print()

    mock_input = "A42\nAll systems operational\n"
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(mock_input)
    try:
        manage_streams()
    finally:
        sys.stdin = original_stdin

    # ------------------------------------------------------------------ ex3
    print_separator("Exercise 3: Vault Security")

    print("--- Test 1: Full vault security protocol ---")
    vault_security_protocol()
    print()

    print("--- Test 2: Standalone secure_extraction ---")
    secure_extraction("standard_archive.txt")
    print()

    print("--- Test 3: Standalone secure_preservation and verify ---")
    secure_preservation("test_vault.txt", "[TEST] Standalone preservation test")
    print()
    print("Verifying written content:")
    secure_extraction("test_vault.txt")
    print()

    print("--- Test 4: secure_extraction on missing file (FileNotFoundError expected) ---")
    try:
        secure_extraction("phantom_vault.txt")
    except FileNotFoundError as e:
        print(f"FileNotFoundError caught: {e}")

    if os.path.exists("test_vault.txt"):
        os.remove("test_vault.txt")
        print("\ntest_vault.txt removed after test.")

    # ------------------------------------------------------------------ ex4
    print_separator("Exercise 4: Crisis Response")

    print("--- Test 1: Full crisis response simulation ---")
    run_crisis_response()
    print()

    print("--- Test 2: Existing file (standard_archive.txt) ---")
    crisis_handler("standard_archive.txt")
    print()

    print("--- Test 3: Missing file ---")
    crisis_handler("totally_missing.txt")
    print()

    print("--- Test 4: Permission denied ---")
    locked_file = "locked_vault.txt"
    with open(locked_file, "w") as f:
        f.write("This data is under lock and key.\n")
    os.chmod(locked_file, 0o000)
    crisis_handler(locked_file)
    os.chmod(locked_file, stat.S_IRUSR | stat.S_IWUSR)
    os.remove(locked_file)
    print(f"\n{locked_file} removed after test.")

    # ---------------------------------------------------------------- done
    print_separator("TEST SUITE COMPLETED")
    print("All exercises have been tested successfully!")
    print("\nKey Concepts Demonstrated:")
    print("  - File reading with open() and FileNotFoundError handling (ex0)")
    print("  - File writing and content creation with open() (ex1)")
    print("  - stdin / stdout / stderr stream management (ex2)")
    print("  - Context managers ('with' statement) for safe I/O (ex3)")
    print("  - Comprehensive exception handling with try/except (ex4)")
    print()


if __name__ == "__main__":
    main()
