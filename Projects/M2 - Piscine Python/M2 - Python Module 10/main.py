"""Module 10 — FuncMage Chronicles: Functional Programming.

Runs all five exercises in sequence:
  ex0  — Lambda Sanctum      (lambda expressions)
  ex1  — Higher Realm        (higher-order functions)
  ex2  — Memory Depths       (closures & lexical scoping)
  ex3  — Ancient Library     (functools module)
  ex4  — Master's Tower      (decorators & class methods)
"""

from ex0.lambda_spells import main as run_ex0
from ex1.higher_magic import main as run_ex1
from ex2.scope_mysteries import main as run_ex2
from ex3.functools_artifacts import main as run_ex3
from ex4.decorator_mastery import main as run_ex4


def main() -> None:
    """Run all module-10 exercises in order."""
    separator = "=" * 50

    print(separator)
    print("Exercise 0: Lambda Sanctum")
    print(separator)
    run_ex0()

    print()
    print(separator)
    print("Exercise 1: Higher Realm")
    print(separator)
    run_ex1()

    print()
    print(separator)
    print("Exercise 2: Memory Depths")
    print(separator)
    run_ex2()

    print()
    print(separator)
    print("Exercise 3: Ancient Library")
    print(separator)
    run_ex3()

    print()
    print(separator)
    print("Exercise 4: Master's Tower")
    print(separator)
    run_ex4()


if __name__ == "__main__":
    main()
