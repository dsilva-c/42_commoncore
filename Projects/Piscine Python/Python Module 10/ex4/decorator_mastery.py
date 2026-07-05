"""ex4 — Master's Tower: decorator mastery and class methods.

File to submit: decorator_mastery.py
Authorized:    functools.wraps, staticmethod, print()
"""

import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that measures and prints the execution time of a spell.

    Prints "Casting <name>..." before and
    "Spell completed in <t> seconds" after execution.

    Args:
        func: the callable to wrap.

    Returns:
        A wrapped callable preserving the original's metadata.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(
    min_power: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory that validates a power argument before casting.

    Searches *args for the first integer value and checks it is >=
    min_power.  If validation fails, returns the string
    "Insufficient power for this spell" without calling the function.

    Args:
        min_power: minimum acceptable power level.

    Returns:
        A decorator that enforces the power constraint.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Support keyword arg 'power' or the first int in positional args.
            power: int | None = kwargs.get('power')  # type: ignore[assignment]
            if power is None:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break
            if power is not None and power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory that retries a failing spell up to max_attempts times.

    Prints progress on each failure and returns a failure message if all
    attempts are exhausted.

    Args:
        max_attempts: maximum number of tries before giving up.

    Returns:
        A decorator that adds retry logic to the wrapped callable.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Guild management with static validation and decorated spell casting."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check whether a mage name is valid.

        A name is valid when it contains at least 3 characters and only
        letters or spaces.

        Args:
            name: the candidate mage name.

        Returns:
            True if valid, False otherwise.
        """
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell, validated to require at least 10 power.

        Args:
            spell_name: name of the spell to cast.
            power:      power level of the cast.

        Returns:
            Success message, or the validator's failure string.
        """
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Demonstrate decorator features."""
    # spell_timer
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    # retry_spell — all attempts fail, then a separate spell that works
    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def cursed_spell() -> str:
        raise RuntimeError("Spell is cursed")

    print(cursed_spell())

    @retry_spell(max_attempts=3)
    def waaagh() -> str:
        return "Waaaaaagh spelled !"

    print(waaagh())

    # MageGuild
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("Jo"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
