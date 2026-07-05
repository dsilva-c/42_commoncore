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

## Running

```bash
python3 ex3/functools_artifacts.py
python3 -m ex3.main
```
