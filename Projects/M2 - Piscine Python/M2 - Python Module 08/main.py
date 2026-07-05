"""Module 08 — The Matrix: Virtual Environments & Dependency Management.

Runs all three exercises in sequence:
  ex0   — Entering the Matrix (virtual environment detection)
  ex01  — Loading Programs (package management & data analysis)
  ex02  — Accessing the Mainframe (secure .env configuration)
"""

from ex0.main import main as run_ex0
from ex01.main import main as run_ex01
from ex02.main import main as run_ex02


def main() -> None:
    """Run all module-08 exercises in order."""
    run_ex0()
    print()
    run_ex01()
    print()
    run_ex02()


if __name__ == "__main__":
    main()
