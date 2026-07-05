"""ex2 — Memory Depths: lexical scoping and closures.

File to submit: scope_mysteries.py
Authorized:    nonlocal, print()

Closures maintain state from their enclosing scope — no global
variables needed.
"""

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    """Create a counting closure.

    Returns:
        A function that increments and returns an internal counter
        each time it is called (starting from 1).
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Create a power-accumulation closure seeded with initial_power.

    Args:
        initial_power: starting value of the accumulated power.

    Returns:
        A function that takes an amount, adds it to the total, and
        returns the new total.
    """
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Create an enchantment-application function for a given type.

    Args:
        enchantment_type: string prefix for the enchantment (e.g. "Flaming").

    Returns:
        A function(item_name) -> str that returns "<type> <item>".
    """
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    """Create a private key-value memory store via closures.

    Returns:
        A dict with two keys:
          'store'  — function(key, value) storing a memory.
          'recall' — function(key) returning the stored value or
                     "Memory not found".
    """
    _vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        _vault[key] = value

    def recall(key: str) -> Any:
        return _vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main() -> None:
    """Demonstrate closure-based functions."""
    # mage_counter — two independent counters to prove separate state
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    # spell_accumulator
    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    # enchantment_factory
    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    # memory_vault
    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
