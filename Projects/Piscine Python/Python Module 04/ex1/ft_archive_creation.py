#!/usr/bin/env python3
"""
Exercise 1: Archive Creation
Establish new data preservation protocols by writing to storage vaults.
"""


def create_archive(filename: str) -> None:
    """
    Create a new archive entry and inscribe preservation data.

    Args:
        filename: Name of the new archive file to create.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")
    print("Storage unit created successfully...")

    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    file_handle = open(filename, 'w')
    print("Inscribing preservation data...")
    for entry in entries:
        file_handle.write(entry + '\n')
        print(entry)
    file_handle.close()

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    create_archive("new_discovery.txt")
