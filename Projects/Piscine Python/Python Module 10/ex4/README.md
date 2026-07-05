# ex4 — Master's Tower

## Goal

Create **decorators** — wrappers that transform the behaviour of any
callable — and contrast `@staticmethod` with regular instance methods
inside a class.

## Files

<div align="center">

| File | Role |
|------|------|
| `decorator_mastery.py` | Three decorators + `MageGuild` class + `main()` |
| `main.py` | Module-style entry-point |

</div>

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

## Concepts explained

### What `@decorator` actually desugars to

```python
@spell_timer
def fireball() -> str:
    ...
```

is exactly equivalent to writing the function first and then rebinding
its name to the decorator's result:

```python
def fireball() -> str:
    ...
fireball = spell_timer(fireball)
```

`spell_timer` is an ordinary higher-order function: it receives the
original `fireball` function object as its `func` parameter, defines a
new function `wrapper` that closes over `func` (the same closure
mechanism as ex1/ex2 — `wrapper`'s body reads `func` from
`spell_timer`'s enclosing scope), and returns `wrapper`. After the
`@spell_timer` line runs, the name `fireball` in the module points to
`wrapper`, not to the original function — calling `fireball()` now
always goes through `wrapper`, which prints the "Casting..." message,
records `time.time()`, calls the *original* function via the closed-over
`func`, prints the elapsed time, and returns whatever `func` returned.
The original function object still exists (referenced by `wrapper`'s
closure) — it's just no longer reachable under the name `fireball`
directly.

### Why `functools.wraps` matters

Without `@functools.wraps(func)` inside `spell_timer`, `wrapper` would
be a plain function literally named `wrapper`, with its own (empty)
docstring. After `fireball = spell_timer(fireball)`,
`fireball.__name__` would report `"wrapper"` and `fireball.__doc__`
would be `None` — `help(fireball)`, debuggers, and any introspection
code that inspects `__name__`/`__doc__` would see the wrapper's
identity, not the original function's. `functools.wraps(func)` is
itself a decorator (a decorator applied to `wrapper`, right where it's
defined) that copies `func.__name__`, `func.__doc__`, `func.__module__`,
and `func.__wrapped__` (a reference back to the original) onto
`wrapper` before it's returned. Every decorator in this module
(`spell_timer`, and the inner `wrapper`s built by `power_validator` and
`retry_spell`) applies `@functools.wraps(func)`, so `cast_spell.__name__`
still reports `"cast_spell"` even after being wrapped twice (once by
`power_validator`'s decorator).

### Decorator factories: an extra layer that takes configuration

`spell_timer` is a plain decorator — it directly takes the function to
wrap. `power_validator(min_power)` is a **decorator factory**: it takes
configuration (`min_power`) as arguments and *returns* the actual
decorator, which is then applied to the function. The nesting is one
level deeper than a plain decorator:

```python
def power_validator(min_power):        # factory: called with config first
    def decorator(func):               # the actual decorator
        def wrapper(*args, **kwargs):  # the actual wrapper
            ...
        return wrapper
    return decorator
```

`@power_validator(min_power=10)` above `cast_spell` evaluates in two
distinct steps: first `power_validator(min_power=10)` is called
immediately (before decoration happens), which runs the outer function
body and returns `decorator` — a closure over `min_power=10`. Then that
returned `decorator` is applied to `cast_spell`, exactly as `spell_timer`
was applied to `fireball` above: `cast_spell = decorator(cast_spell)`.
`decorator` itself defines and returns `wrapper`, which closes over
*both* `func` (the original `cast_spell`) and `min_power` (from the
factory call) — two levels of closure stacked on top of each other.
That's why `wrapper` can read `min_power` when it checks `power <
min_power`: `min_power` was captured when `power_validator(10)` ran,
long before any spell was ever cast. `retry_spell(max_attempts)`
follows the identical two-layer shape, closing over `max_attempts`
instead.

A plain decorator only ever takes one argument — the function — so it
has no way to accept configuration like `min_power` or `max_attempts`
directly; the factory layer exists solely to smuggle that configuration
into the closure the real decorator (and its wrapper) will use.

### `@staticmethod` vs. a regular instance method

`MageGuild.validate_mage_name` is declared `@staticmethod`, while
`cast_spell` is a regular instance method (with a leading `self`
parameter, additionally wrapped by `@power_validator(min_power=10)`).
When Python calls a regular instance method — `guild.cast_spell(...)`
— it implicitly passes `guild` itself as the first argument (`self`),
giving the method access to that particular instance's attributes and
other methods via `self.something`. A `@staticmethod` opts out of that
binding entirely: `validate_mage_name(name)` receives only the
arguments explicitly passed to it; there is no implicit `self` (or
`cls`) argument, and the method body has no way to read or mutate any
particular `MageGuild` instance's state, because it never receives a
reference to one. That's the right shape for
`validate_mage_name`: it's a pure string-validation function that
happens to live inside the class namespace for organizational reasons
(`MageGuild.validate_mage_name("Alex")` reads naturally as "the
guild's rule for valid names") but doesn't need or use any per-mage
data, and can be called equally well on the class itself
(`MageGuild.validate_mage_name(...)`) or on an instance without ever
constructing one.

## Running

```bash
python3 ex4/decorator_mastery.py
python3 -m ex4.main
```
