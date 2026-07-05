# ex4 — Master's Tower

## Goal

Create **decorators** — wrappers that transform the behaviour of any
callable — and contrast `@staticmethod` with regular instance methods
inside a class.

## Files

| File | Role |
|------|------|
| `decorator_mastery.py` | Three decorators + `MageGuild` class + `main()` |
| `main.py` | Module-style entry-point |

## Design

```
spell_timer(func)             → Callable   measures + prints execution time
power_validator(min_power)    → Callable   validates first int arg >= min_power
retry_spell(max_attempts)     → Callable   retries on exception up to N times

MageGuild
├── @staticmethod validate_mage_name(name) → bool
└── @power_validator(10) cast_spell(self, spell_name, power) → str
```

## Key concepts

- **Decorator** — a higher-order function that takes a callable, wraps it
  in new behaviour, and returns the enhanced version.
- **`functools.wraps`** — copies `__name__`, `__doc__`, and other metadata
  from the wrapped function to the wrapper, so introspection tools still
  show the original function's identity.
- **Decorator factory** — a function that *returns* a decorator, enabling
  parameterised decorators such as `@power_validator(min_power=10)`.
- **`@staticmethod`** — binds a method to the class rather than to an
  instance; no implicit `self` or `cls` argument.

## Running

```bash
python3 ex4/decorator_mastery.py
python3 -m ex4.main
```
