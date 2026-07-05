# ex3 — Ancient Library

## Goal

Explore the **`functools` module** — Python's treasure chest of
functional programming tools: `reduce`, `partial`, `lru_cache`, and
`singledispatch`.

## Files

<div align="center">

| File | Role |
|------|------|
| `functools_artifacts.py` | Four functools demonstrations + `main()` |
| `main.py` | Module-style entry-point |

</div>

## Function design

```
spell_reducer(spells, operation) → int         reduce with operator fns
partial_enchanter(base_fn)       → dict        pre-filled partial functions
memoized_fibonacci(n)            → int         lru_cache-backed recursion
spell_dispatcher()               → Callable    singledispatch type router
```

## Key concepts

- **`functools.reduce`** — fold a sequence into a single value using a
  binary function.
- **`operator` module** — ready-made functions for arithmetic ops (`add`,
  `mul`, etc.) that pair naturally with `reduce`.
- **`functools.partial`** — create a new callable from an existing one with
  some arguments pre-filled.
- **`functools.lru_cache`** — memoize function results automatically;
  eliminates redundant computation in recursive algorithms.
- **`functools.singledispatch`** — register different implementations of a
  function keyed by the type of the first argument.

## Concepts explained

### `functools.reduce`: the accumulator pattern and identity elements

`functools.reduce(function, iterable)` collapses a sequence into a
single value by repeatedly applying a binary function to a running
accumulator and the next element. `spell_reducer([10, 20, 30, 40],
'add')` with `ops['add'] = operator.add` runs:

```
acc = 10                  # reduce seeds the accumulator with the first element
acc = operator.add(acc, 20)  → 30
acc = operator.add(acc, 30)  → 60
acc = operator.add(acc, 40)  → 100
```

Four elements, three calls to the binary function — `reduce` always
makes `len(iterable) - 1` calls when no initial value is supplied,
because the first element seeds the accumulator instead of being
combined with anything. That's precisely the failure mode `spell_reducer`
guards against explicitly: `functools.reduce(op, [])` with no initial
value and no elements has nothing to seed the accumulator with, so it
raises `TypeError: reduce() of empty iterable with no initial value`.
`spell_reducer` sidesteps this with `if not spells: return 0` before
ever calling `reduce` — `0` is the **identity element** for addition
(`x + 0 == x` for any `x`), the value that "changes nothing" if it
were folded in. (Note: `spell_reducer` returns the hardcoded `0` for
*any* empty-list operation, including `'multiply'`, where the
mathematically correct identity would be `1` — worth knowing precisely
because it's a place where the general identity-element rule and the
code's actual behavior diverge.) This identity-element trick is the
standard way `reduce`-based folds define a sane result for the
empty-input edge case, the same way `sum([])` is defined to be `0` and
`math.prod([])` is defined to be `1`.

`operator.add` and `operator.mul` (from the `operator` module) are
plain functions equivalent to `lambda a, b: a + b` and `lambda a, b: a
* b` — the module exists so common operators can be passed as
first-class callables to functions like `reduce`, `sorted`, or `map`
without writing a trivial lambda wrapper each time. `'max'` and
`'min'` fall back to lambdas here because there's no zero-argument
`operator.max`/`operator.min` that reduces pairwise the way this
exercise needs (Python's built-in `max`/`min` take a whole iterable at
once, not two values to fold), so `spell_reducer` supplies
`lambda a, b: a if a > b else b` as the pairwise comparison `reduce`
needs.

### `functools.partial`: pre-filling arguments, not pre-computing results

`partial_enchanter` builds three `functools.partial` objects:

```python
functools.partial(base_enchantment, 50, 'fire')
```

`functools.partial(func, *args, **kwargs)` returns a new callable — not
the result of calling `func`, a *callable object* that remembers `func`
together with the positional/keyword arguments given so far. Calling
that partial later with the remaining arguments concatenates them onto
the pre-filled ones and finally invokes `func`. So
`enchanters['fire_enchant']("Sword")` is equivalent to calling
`enchant(50, 'fire', "Sword")` — the `50` and `'fire'` were locked in at
`partial_enchanter` time, and `"Sword"` is supplied only at call time.
This differs from a closure built with `def`: a `partial` object doesn't
need you to write a wrapping function at all — it mechanically appends
arguments for you, which is why it is the idiomatic tool for
"specialize this function by fixing some of its arguments" whenever
the specialization itself needs no custom logic.

### `functools.lru_cache`: turning exponential recursion into linear recursion

`memoized_fibonacci` is decorated with `@functools.lru_cache(maxsize=None)`.
Without memoization, naive recursive Fibonacci recomputes the same
subproblems over and over — the call tree for `fib(5)` branches into
`fib(4)` and `fib(3)`, and `fib(4)` itself branches into `fib(3)` and
`fib(2)`, so `fib(3)` gets computed twice, `fib(2)` three times, and so
on, giving roughly `O(2ⁿ)` total calls:

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) → 1
│   │   │   └── fib(0) → 0
│   │   └── fib(1) → 1
│   └── fib(2)          ← recomputed from scratch
│       ├── fib(1) → 1
│       └── fib(0) → 0
└── fib(3)              ← recomputed from scratch
    ├── fib(2)          ← recomputed again
    └── fib(1)
```

`lru_cache` wraps `memoized_fibonacci` in a dict-backed cache keyed by
its call arguments (here just `n`). The first time `memoized_fibonacci(3)`
is computed, the result is stored under key `3`; every subsequent call
with `n=3` — no matter where in the call tree it originates — returns
the cached value immediately instead of re-entering the function body.
That collapses the tree above to exactly one call per distinct `n`
from `0` to the target, i.e. `O(n)` unique computations, which is why
`memoized_fibonacci(15)` after warming the cache with smaller values
runs in linear time. `.cache_info()` (a method `lru_cache` attaches to
the decorated function) reports `hits`/`misses`/`maxsize`/`currsize`,
which is how the cache's effect is verified rather than assumed:
repeated calls with an already-seen `n` increment `hits` without
incrementing `misses`.

### `functools.singledispatch`: runtime dispatch on argument type

`spell_dispatcher` builds `cast` as a `@functools.singledispatch`
function. The undecorated `cast(value)` becomes the **base
implementation** — the fallback used when no more specific
implementation matches. `@cast.register(int)`, `@cast.register(str)`,
and `@cast.register(list)` each attach an alternate implementation to
`cast`, keyed by the *type of the first argument* — `cast.register`
inspects the type annotation (or the type passed explicitly to
`register`) and stores the function in a type registry internal to
`cast`. Calling `cast(42)` doesn't run the base body at all: at call
time, `singledispatch` looks at `type(42)` (i.e. `int`), finds the
registered `int` implementation, and dispatches to it instead — this
is why `cast(42)` prints "Damage spell" and `cast("fireball")` prints
"Enchantment" even though both go through the same name `cast`. `cast(3.14)`
has no registered `float` implementation, so it falls through to the
original base function and returns `"Unknown spell type"`. This
replaces a hand-written `if isinstance(value, int): ... elif
isinstance(value, str): ...` chain with a registry that new callers can
extend by registering additional types, without touching `cast`'s own
source.

## Running

```bash
python3 ex3/functools_artifacts.py
python3 -m ex3.main
```
