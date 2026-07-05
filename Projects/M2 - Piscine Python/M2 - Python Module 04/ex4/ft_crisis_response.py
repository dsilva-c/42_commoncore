#!/usr/bin/env python3
"""
Exercise 4: Crisis Response
Handle corrupted archives and access failures with try/except blocks
combined with the 'with' statement for safe file operations.
"""


def crisis_handler(filename: str) -> None:
    """
    Manage archive access with comprehensive crisis response protocols.

    Handles FileNotFoundError, PermissionError, and unexpected anomalies
    while ensuring system stability after each incident.

    Args:
        filename: Path to the archive to attempt access.
    """
    content: str = ""
    error_type: str = ""
    error_msg: str = ""

    try:
        with open(filename, 'r') as vault:
            content = vault.read().strip()
    except FileNotFoundError:
        error_type = "not_found"
    except PermissionError:
        error_type = "permission"
    except Exception as e:
        error_type = "other"
        error_msg = str(e)

    if not error_type:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed")
    elif error_type == "not_found":
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    elif error_type == "permission":
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print(f"RESPONSE: Unexpected anomaly detected - {error_msg}")
        print("STATUS: Crisis contained, damage assessed")


def run_crisis_response() -> None:
    """
    Execute the full crisis response simulation across all test scenarios.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    crisis_handler("lost_archive.txt")

    crisis_handler("classified_vault.txt")

    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    run_crisis_response()
