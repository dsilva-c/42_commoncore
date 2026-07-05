# ex1 — Higher Realm

## Goal

Understand **higher-order functions** — functions that accept other
functions as arguments or return them as results — demonstrating that
Python treats functions as first-class citizens.

## Files

| File | Role |
|------|------|
| `higher_magic.py` | Four HOF factories + `main()` |
| `main.py` | Module-style entry-point |

## Function design

```
spell_combiner(spell1, spell2)          → Callable  calls both, returns tuple
power_amplifier(base_spell, multiplier) → Callable  scales numeric result
conditional_caster(condition, spell)    → Callable  casts only if cond True
spell_sequence(spells)                  → Callable  runs all, returns list
```

## Key concepts

- **First-class functions** — functions can be stored, passed, and returned
  just like any other value.
- **Closure** — inner functions (`combined`, `amplified`, etc.) capture
  variables from their enclosing scope.
- **`callable(x)`** — built-in check used to verify that an object is callable.
- **`Callable[..., T]`** from `typing` — statically annotates function-typed
  parameters and return values.

## Running

```bash
python3 ex1/higher_magic.py
python3 -m ex1.main
```
