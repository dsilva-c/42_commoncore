#!/usr/bin/env python3
"""
Exercise 0: Ancient Text Recovery
Retrieve data from old storage units using basic file operations.
"""


def recover_ancient_text(filename: str) -> None:
    """
    Recover ancient text from a storage vault.

    Args:
        filename: Path to the storage vault file.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")
    print("Connection established...")

    file_handle = open(filename, 'r')
    content = file_handle.read()
    file_handle.close()

    print("RECOVERED DATA:")
    for line in content.strip().split('\n'):
        print(line)
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    try:
        recover_ancient_text("ancient_fragment.txt")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
