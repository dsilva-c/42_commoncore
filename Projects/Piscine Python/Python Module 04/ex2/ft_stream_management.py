#!/usr/bin/env python3
"""
Exercise 2: Stream Management
Master the three data channels: stdin, stdout, and stderr.
"""

import sys


def manage_streams() -> None:
    """
    Access the three sacred data channels of the Archives.

    Collects archivist identification and status,
    then routes messages to the appropriate streams.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id: str = input(
        "Input Stream active. Enter archivist ID: "
    )
    if not sys.stdin.isatty():
        print()
    status_report: str = input(
        "Input Stream active. Enter status report: "
    )
    if not sys.stdin.isatty():
        print()

    sys.stdout.write(
        f"[STANDARD] Archive status from {archivist_id}: "
        f"{status_report}\n"
    )
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    manage_streams()
