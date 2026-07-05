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

## Running

```bash
python3 ex0/lambda_spells.py      # direct
python3 -m ex0.main               # module
```
