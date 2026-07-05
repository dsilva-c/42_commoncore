"""ex3 — Ancient Library: functools module treasures.

File to submit: functools_artifacts.py
Authorized:    functools, operator, print()
"""

import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the specified operation.

    Args:
        spells:    list of integer spell power values.
        operation: one of "add", "multiply", "max", "min".

    Returns:
        The single integer result of reducing all values.

    Raises:
        ValueError: if an unknown operation is provided.
    """
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b,
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation!r}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[..., Any],
) -> dict[str, Callable[..., Any]]:
    """Create specialised partial applications of base_enchantment.

    The base_enchantment is expected to accept (power, element, target).
    Each returned partial locks power=50 and its respective element.

    Args:
        base_enchantment: function(power, element, target) -> Any.

    Returns:
        Dict with keys 'fire_enchant', 'ice_enchant', 'lightning_enchant',
        each a functools.partial with power=50 and the matching element.
    """
    return {
        'fire_enchant':      functools.partial(base_enchantment, 50, 'fire'),
        'ice_enchant':       functools.partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': functools.partial(
            base_enchantment,
            50,
            'lightning',
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, using lru_cache for memoization.

    Args:
        n: position in the Fibonacci sequence (0-indexed).

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[..., Any]:
    """Create a type-dispatched spell-casting function via singledispatch.

    Returns:
        A callable that behaves differently based on argument type:
          - int  → damage spell message
          - str  → enchantment message
          - list → multi-cast summary
    """
    @functools.singledispatch
    def cast(value: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @cast.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @cast.register(list)
    def _(value: list[Any]) -> str:
        return f"Multi-cast: {len(value)} spells"

    return cast


def main() -> None:
    """Demonstrate functools tools."""
    powers = [10, 20, 30, 40]

    # spell_reducer
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")

    # partial_enchanter
    print("\nTesting partial enchanter...")

    def enchant(power: int, element: str, target: str) -> str:
        return (
            f"{element.capitalize()} enchantment (power={power}) "
            f"on {target}"
        )

    enchanters = partial_enchanter(enchant)
    print(enchanters['fire_enchant']("Sword"))
    print(enchanters['ice_enchant']("Shield"))
    print(enchanters['lightning_enchant']("Staff"))

    # memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    # spell_dispatcher
    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast([1, 2, 3]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
