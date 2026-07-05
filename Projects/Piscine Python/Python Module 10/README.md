# FuncMage Chronicles — Master the Ancient Arts of Functional Programming

Python Piscine · Module 10

## 📋 Overview

Explores functional programming in Python 3.10+ through five themed
exercises: anonymous functions, higher-order functions, closures, the
`functools` module, and decorators. Each exercise isolates one concept
and builds toward treating functions as first-class values — objects
that can be stored, passed, combined, and returned just like any other
data.

## 🎯 Learning Objectives

- Write anonymous single-expression functions with `lambda` and use them
  with `sorted`, `filter`, `map`, `max`, and `min`.
- Recognize and build higher-order functions — functions that accept
  other functions as arguments or return new functions.
- Understand closures, lexical (static) scoping, and the difference
  between *reading* and *reassigning* a variable in an enclosing scope
  (`nonlocal` vs. plain access).
- Use `functools.reduce`, `functools.partial`, `functools.lru_cache`, and
  `functools.singledispatch` to solve problems idiomatically instead of
  writing manual loops or type-checking chains.
- Write decorators (plain and parameterized/"factory" style), preserve
  wrapped-function metadata with `functools.wraps`, and combine
  decorators with classes and `@staticmethod`.

## 📁 Project Structure

```
.
├── __init__.py
├── main.py
├── pyrightconfig.json
├── requirements.txt
├── tools/
│   └── data_generator.py
├── ex0/
│   ├── __init__.py
│   ├── lambda_spells.py
│   ├── main.py
│   └── README.md
├── ex1/
│   ├── __init__.py
│   ├── higher_magic.py
│   ├── main.py
│   └── README.md
├── ex2/
│   ├── __init__.py
│   ├── scope_mysteries.py
│   ├── main.py
│   └── README.md
├── ex3/
│   ├── __init__.py
│   ├── functools_artifacts.py
│   ├── main.py
│   └── README.md
└── ex4/
    ├── __init__.py
    ├── decorator_mastery.py
    ├── main.py
    └── README.md
```

## 🚀 Usage

Execute from the **module root** (no virtual environment needed — only
standard library modules are used):

```bash
# All exercises at once
python3 main.py

# Individual exercises
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py

# Module-style execution
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main

# Data generator helper
python3 tools/data_generator.py
```

## 📚 Exercises

### ex0 — Lambda Sanctum (`lambda_spells.py`)

Master anonymous functions by using `lambda`, `map()`, `filter()`, and
`sorted()` to transform and query data, without reaching for `def` on
simple per-element operations.

- `artifact_sorter(artifacts)` — `sorted(key=lambda a: a['power'],
  reverse=True)`, artifacts ranked strongest first.
- `power_filter(mages, min_power)` — `filter(lambda m: m['power'] >=
  min_power, mages)`, materialized with `list()`.
- `spell_transformer(spells)` — `map(lambda s: f"* {s} *", spells)`.
- `mage_stats(mages)` — extracts powers via `map`, then computes
  `max`/`min`/`avg` (rounded to 2 decimals) using lambdas.
- Key concepts: `lambda`, `sorted(key=...)`, lazy `filter`/`map`
  iterators, aggregate stats with `max`/`min`/`sum`.

### ex1 — Higher Realm (`higher_magic.py`)

Understand higher-order functions: functions that accept other
functions as arguments or return them as results, demonstrating that
Python treats functions as first-class citizens. All spells follow the
contract `spell(target: str, power: int) -> str`.

- `spell_combiner(spell1, spell2)` — returns a closure that calls both
  spells and returns a `tuple` of both results.
- `power_amplifier(base_spell, multiplier)` — returns a closure that
  multiplies `power` before delegating to `base_spell`.
- `conditional_caster(condition, spell)` — returns a closure that casts
  only if `condition(target, power)` is `True`, else `"Spell fizzled"`.
- `spell_sequence(spells)` — returns a closure that runs a list of
  callables in order and returns a `list` of their results.
- Key concepts: first-class functions, closures, `callable(x)`,
  `Callable` type hints.

### ex2 — Memory Depths (`scope_mysteries.py`)

Understand lexical scoping and closures: how an inner function
remembers variables from the scope where it was defined, even after
that scope has finished executing.

- `mage_counter()` — returns a `counter()` closure; uses `nonlocal
  count` to increment on every call. Two independent calls to
  `mage_counter()` produce two independent counters.
- `spell_accumulator(initial_power)` — returns an `accumulate(amount)`
  closure that grows a running total via `nonlocal total`.
- `enchantment_factory(enchantment_type)` — returns an `enchant(item)`
  closure that only *reads* `enchantment_type` (no `nonlocal` needed).
- `memory_vault()` — returns `{'store': fn, 'recall': fn}`; both
  closures share one private `_vault` dict, encapsulating state without
  a class.
- Key concepts: closures, lexical scoping, `nonlocal`, state without
  `global`.

### ex3 — Ancient Library (`functools_artifacts.py`)

Explore the `functools` module — `reduce`, `partial`, `lru_cache`, and
`singledispatch`.

- `spell_reducer(spells, operation)` — folds a list of ints with
  `functools.reduce` using `operator.add`/`operator.mul` (or lambda
  comparisons for `max`/`min`); returns `0` for an empty list; raises
  `ValueError` for an unknown operation.
- `partial_enchanter(base_enchantment)` — returns a `dict` of three
  `functools.partial` objects, each with `power=50` and one element
  (`fire`/`ice`/`lightning`) pre-filled, leaving only `target` to supply.
- `memoized_fibonacci(n)` — recursive Fibonacci decorated with
  `@functools.lru_cache(maxsize=None)`, turning an O(2ⁿ) call tree into
  O(n) unique computations; verifiable via `.cache_info()`.
- `spell_dispatcher()` — a `@functools.singledispatch` base function
  with `int`, `str`, and `list` implementations registered via
  `@cast.register(...)`; unregistered types fall back to the base case.
- Key concepts: `functools.reduce`, the `operator` module, `partial`
  application, memoization, type-based dispatch.

### ex4 — Master's Tower (`decorator_mastery.py`)

Create decorators — wrappers that transform the behaviour of any
callable — and contrast `@staticmethod` with a regular instance method.

- `spell_timer(func)` — a plain decorator; times and prints execution
  around any function, preserving metadata with `@functools.wraps`.
- `power_validator(min_power)` — a decorator *factory*; the returned
  wrapper reads `power` from `kwargs` or the first positional `int`, and
  blocks the call if `power < min_power`.
- `retry_spell(max_attempts)` — a decorator factory; retries the
  wrapped call on any `Exception`, up to `max_attempts` times.
- `MageGuild.validate_mage_name` — `@staticmethod`, validates a name
  with no `self` needed.
- `MageGuild.cast_spell` — instance method decorated with
  `@power_validator(min_power=10)`, showing decorators composing with
  classes.
- Key concepts: decorators, `functools.wraps`, decorator factories,
  `@staticmethod` vs. instance methods.

## 🧠 Key Concepts

- **Closures** — an inner function that captures ("remembers") free
  variables from the scope in which it was defined, even after that
  scope has returned. Each call to a closure-producing factory (e.g.
  `mage_counter()`) creates a fresh, independent set of captured
  variables.
- **`nonlocal` vs. reading an outer variable** — assigning to a name
  inside a nested function makes it local by default; `nonlocal` tells
  Python to instead rebind the name in the nearest enclosing (non-global)
  scope. It is only required for *reassignment* (`count += 1`), never
  for plain reads (`enchantment_type` in `enchantment_factory`) or for
  mutating an object in place (`_vault[key] = value` in `memory_vault`
  mutates the dict, it doesn't rebind the name `_vault`).
- **Why `nonlocal` is allowed but `global` is not** — `global` exposes
  state to the entire module; `nonlocal` scopes the mutable state to the
  enclosing function only, keeping it private and encapsulated.
- **`functools` toolbox** — `reduce` folds a sequence with a binary
  function; `partial` pre-fills arguments of an existing callable;
  `lru_cache` memoizes results keyed by arguments; `singledispatch`
  dispatches to different implementations based on the type of the
  first argument.
- **Decorator mechanics** — a decorator is a function that takes a
  callable, wraps it in additional behaviour, and returns the wrapper.
  A decorator *factory* (`power_validator(10)`) is called first with
  configuration and returns the actual decorator, which is then applied
  to the function. `functools.wraps` copies `__name__`, `__doc__`, and
  other metadata from the original function onto the wrapper so
  introspection tools don't see `"wrapper"` instead of the real name.
- **Type hints for functions** — `Callable` is imported from
  `collections.abc` (the canonical location since Python 3.9+), not
  from `typing`; the lowercase `callable` built-in is a runtime check,
  not a type hint. Built-in generic aliases (`list[dict]`, `dict[str,
  Any]`, `tuple[...]`, `int | None`) are used directly since the module
  targets Python 3.10+, avoiding `from __future__ import annotations` or
  `typing.List`/`Optional`.
- **Type checking with Pylance** — annotations follow PEP 484/526 and
  are verified with Pylance (VS Code's Python language server, powered
  by Pyright). The [pyrightconfig.json](pyrightconfig.json) targets
  Python 3.10 so the built-in generic syntax above is available without
  extra imports.

## 🧪 Testing

Each `exN/<file>.py` includes its own `main()` that exercises every
function with representative input and prints the result, so running
the file directly or via `python3 main.py` from the module root doubles
as a manual correctness check. Key behaviours to verify by inspection
or in a REPL:

- ex0: sort order, filter threshold, transformed strings, and the
  max/min/avg values in `mage_stats`.
- ex1: that `spell_combiner` returns a tuple, `power_amplifier` scales
  power correctly, `conditional_caster` fizzles on a `False` condition.
- ex2: that two independent calls to `mage_counter()` produce
  independent counts (e.g. `1, 2` and `1`), and that `memory_vault`
  returns `"Memory not found"` for a missing key.
- ex3: `spell_reducer([], 'add') == 0`, an unknown operation raises
  `ValueError`, `memoized_fibonacci.cache_info()` shows cache hits after
  repeated calls, and `spell_dispatcher()` falls back to the base case
  for unregistered types (e.g. `float`).
- ex4: `spell_timer` prints elapsed time, `power_validator` blocks a
  call below the threshold, `retry_spell` prints "retrying" only on
  attempts before the last, and `MageGuild.validate_mage_name` rejects
  short or non-alphabetic names.

## ✅ Code Style & Requirements

- Python 3.10+ syntax throughout (`list[T]`, `dict[K, V]`, `int | None`
  unions) — no `typing.List`/`Dict`/`Optional`.
- `Callable` type hints come from `collections.abc`; `Any` still comes
  from `typing`.
- No `eval()`, `exec()`, or module-level `global` state.
- No external packages — stdlib only.

| Module | Purpose |
|--------|---------|
| `functools` | `reduce`, `partial`, `lru_cache`, `singledispatch`, `wraps` |
| `collections.abc` | `Callable` type hints |
| `typing` | `Any` type hints |
| `operator` | `add`, `mul` for functional operations |
| `itertools` | advanced iteration patterns |
| `time` | timing in the `spell_timer` decorator |

## 🛡️ Defense Notes

- **`retry_spell` prints "retrying" only `max_attempts - 1` times**: the
  final attempt either succeeds (no retry needed) or raises, so a
  "retrying" message is only logged between attempts, never after the
  last one — printing "retrying (attempt 3/3)" would be misleading
  since there is no fourth attempt coming.
- **`spell_reducer([])` returns `0`**: `0` is the additive identity for
  `functools.reduce` over a sum — reducing an empty sequence with no
  explicit initial value would raise `TypeError`, so an initial value of
  `0` is supplied to make the empty-list case well-defined and consistent
  with math conventions.
- **`enchantment_factory` needs no `nonlocal`**: it only *reads* the
  enclosing variable inside the closure (never reassigns it), and
  `nonlocal` is only required when a nested function rebinds an outer
  variable, not when it merely reads it. The same reasoning applies to
  `memory_vault`'s `store` function: `_vault[key] = value` mutates the
  dict object in place, it doesn't rebind the name `_vault`, so no
  `nonlocal` is needed there either.
- **Decorator application order for `@power_validator(10)`**: Python
  evaluates `power_validator(10)` first, which returns the actual
  `decorator`; that `decorator` is then applied to the function
  immediately below it (`cast_spell = power_validator(10)(cast_spell)`).
  So the expression is evaluated top-to-bottom but *applied*
  bottom-to-top; with stacked decorators, the one closest to the
  function runs innermost. Concretely, for `@power_validator(min_power=10)`
  on `cast_spell`: (1) `power_validator(10)` runs and returns
  `decorator`; (2) `decorator(cast_spell)` runs and returns `wrapper`;
  (3) `MageGuild.cast_spell` now points to `wrapper`; (4) calling
  `guild.cast_spell("Lightning", 15)` runs `wrapper`, which checks
  `15 >= 10` and only then calls the original `cast_spell`.
- **Why `functools.wraps` matters**: without it, a decorated function's
  `__name__` and `__doc__` would report the wrapper's own metadata
  (e.g. `"wrapper"`) instead of the original function's, breaking
  introspection and tools like `help()`.
- **Why `nonlocal` is allowed but `global` is forbidden**: `global`
  makes state accessible to the entire module, breaking encapsulation;
  `nonlocal` is scoped to the enclosing function, keeping the state
  private to the closure that owns it.

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
