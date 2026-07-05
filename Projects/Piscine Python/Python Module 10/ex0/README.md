# ex0 — Lambda Sanctum

## Goal

Master **anonymous functions** by using `lambda`, `map()`, `filter()`,
and `sorted()` to transform and query data — without ever reaching for
`def` for simple operations.

## Files

<div align="center">

| File | Role |
|------|------|
| `lambda_spells.py` | Four lambda-driven utility functions + `main()` |
| `main.py` | Module-style entry-point |

</div>

## Function design

```
artifact_sorter(artifacts)         → list[dict]   sorted by 'power' desc
power_filter(mages, min_power)     → list[dict]   filter power >= threshold
spell_transformer(spells)          → list[str]    wrap each name in "* … *"
mage_stats(mages)                  → dict          max / min / avg power
```

## Key concepts

- **`lambda`** — inline, anonymous function expression.
- **`sorted(key=lambda …)`** — custom sort criterion without a named helper.
- **`filter(lambda …)`** — lazy predicate filter; converted to `list`.
- **`map(lambda …)`** — lazy element transformation; converted to `list`.
- **`max/min/sum` with lambdas** — aggregate statistics in one expression.

## Concepts explained

### `lambda` vs. `def`

A `lambda` is an *expression* that evaluates to a function object — it
is not a statement. That single restriction (body must be one
expression, no `if`/`for`/`assignment` statements inside it) is what
makes it "anonymous": you can write it inline, at the exact spot a
function value is needed, without binding it to a name first. Compare:

```python
def key_fn(a):
    return a['power']

sorted(artifacts, key=key_fn)
# vs.
sorted(artifacts, key=lambda a: a['power'])
```

Both produce an equivalent callable. `lambda a: a['power']` desugars
to "take one argument `a`, evaluate the expression `a['power']`,
return it" — the `return` is implicit and mandatory (a lambda always
returns the value of its one expression; it cannot return early or
return nothing). `def` supports arbitrary statements, multiple
`return`s, loops, and a `__name__` other than `"<lambda>"`; `lambda`
trades all of that away for the ability to be written where it's used.
In `lambda_spells.py`, none of the four functions need loops or
branches inside the per-element logic, so a full `def` would just add
ceremony around a one-line idea.

### Why `sorted(key=...)` takes a function, not a comparison

`artifact_sorter` calls `sorted(artifacts, key=lambda a: a['power'],
reverse=True)`. `sorted` does not ask the key function to *do* the
sorting — it asks it to compute, for each element, a **sort key**: a
value that can be compared with `<` between elements. `sorted` then
runs its own comparison sort using those extracted keys. This is why
`key=lambda a: a['power']` is enough: the lambda's only job is
"given one artifact, tell me the number to compare it by." The
alternative — passing a two-argument comparison function that returns
-1/0/1 — is what old `cmp`-style sorting required and is strictly more
work for the same result; `key=` is preferred because it only computes
each element's key once (O(n) key extractions) rather than
recomputing a comparison on every pairwise check.

### Lazy iterators: `filter` and `map` don't build lists

`power_filter` and `spell_transformer` both wrap their `filter`/`map`
call in `list(...)`. That's not stylistic — `filter(lambda m: m['power']
>= min_power, mages)` on its own returns a `filter` object, an
**iterator** that hasn't actually inspected a single mage yet. Iterators
are lazy: they compute the next value only when something asks for it
(via `next()`, implicitly through a `for` loop, or by exhausting it
into a container). `map(lambda s: f"* {s} *", spells)` behaves the same
way — a `map` object, not a list of strings.

This laziness matters for two reasons:

- **You can only walk a `filter`/`map` object once.** After it's been
  consumed (e.g. by `list()`), asking for its contents again yields
  nothing — there's no data cached inside it, just a pointer to "what
  to compute next."
- **`filter`/`map` objects don't support indexing or `len()`.**
  `power_filter(...)[0]` or `len(spell_transformer(...))` would raise
  `TypeError` unless `list()` (or `tuple()`, or a `for` loop) has
  materialized the results first. Wrapping in `list()` forces every
  element through the lambda immediately and stores the results, which
  is what lets the rest of the codebase (and `main()`'s f-strings) index
  and measure them normally.

`mage_stats` uses this same pattern for `powers = list(map(lambda m:
m['power'], mages))`, then feeds the *materialized* list into `max`,
`min`, and `sum` — all of which need to walk the sequence (`sum`) or
would otherwise re-trigger the lambda on every pass if `powers` were
still a lazy `map` object reused three times.

## Running

```bash
python3 ex0/lambda_spells.py      # direct
python3 -m ex0.main               # module
```
