"""Module 09 — Cosmic Data Observatory: Pydantic Models & Validation.

Runs all three exercises in sequence:
  ex0  — Space Station Data (basic model + field validation)
  ex1  — Alien Contact Logs (custom model_validator)
  ex2  — Space Crew Management (nested models)
"""

from ex0.space_station import main as run_ex0
from ex1.alien_contact import main as run_ex1
from ex2.space_crew import main as run_ex2


def main() -> None:
    """Run all module-09 exercises in order."""
    run_ex0()
    print()
    run_ex1()
    print()
    run_ex2()


if __name__ == "__main__":
    main()
