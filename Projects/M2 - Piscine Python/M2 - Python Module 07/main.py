"""Module 07 — DataDeck: Master the Art of Abstract Card Architecture.

Runs all five exercises in sequence:
  ex0  — Card Foundation (ABC, Enum, type hints)
  ex1  — Deck Builder (concrete card types, deck management)
  ex2  — Ability System (multiple interfaces, multiple inheritance)
  ex3  — Game Engine (Abstract Factory + Strategy patterns)
  ex4  — Tournament Platform (advanced interface composition)
"""

from ex0.main import main as run_ex0
from ex1.main import main as run_ex1
from ex2.main import main as run_ex2
from ex3.main import main as run_ex3
from ex4.main import main as run_ex4


def main() -> None:
    """Run all module-07 exercises in order."""
    run_ex0()
    print()
    run_ex1()
    print()
    run_ex2()
    print()
    run_ex3()
    print()
    run_ex4()


if __name__ == "__main__":
    main()
