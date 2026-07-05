# ex1 — Higher Realm

## Goal

Understand **higher-order functions** — functions that accept other
functions as arguments or return them as results — demonstrating that
Python treats functions as first-class citizens.

## Files

<div align="center">

| File | Role |
|------|------|
| `higher_magic.py` | Four HOF factories + `main()` |
| `main.py` | Module-style entry-point |

</div>

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

## Concepts explained

### What a higher-order function actually is

A function is "higher-order" if it does at least one of: (1) accept
another function as an argument, or (2) return a function as its
result. Nothing special is required of Python to allow this beyond one
property: functions must be **first-class objects** — values that can
be assigned to a name, stored in a data structure, passed as an
argument, and returned from another function, exactly like an `int` or
a `str`. In Python, a `def` statement (or a `lambda`) simply binds a
function *object* to a name in the current scope; the object itself
has no special privileges tied to that name. That's why
`spell_combiner(spell1, spell2)` can accept `fireball` and `heal` as
plain arguments — from the function's point of view, `spell1` is just
a local variable that happens to be bound to a callable object — and
why `spell_combiner` can build and `return combined`, handing a brand
new function object back to the caller. `callable(x)` is the runtime
check for "is this object one of those things I can put `()` after" —
it returns `True` for functions, lambdas, classes, and any object
implementing `__call__`.

### Tracing a closure: `power_amplifier`

```python
mega_fireball = power_amplifier(fireball, 3)
```

Walk through exactly what happens, in order:

1. `power_amplifier(fireball, 3)` is called. Inside its local scope,
   `base_spell` is bound to the `fireball` function object and
   `multiplier` is bound to `3`.
2. The `def amplified(...):` statement executes. This does **not** run
   the body of `amplified` — it constructs a new function object and
   binds it to the local name `amplified`. Critically, Python notices
   that the body of `amplified` references `base_spell` and
   `multiplier`, names that live in the *enclosing* scope
   (`power_amplifier`'s frame) rather than `amplified`'s own local
   scope or the module's global scope. It attaches a **closure**: a
   reference to that enclosing frame's cells for `base_spell` and
   `multiplier`, bundled into the function object as `amplified.__closure__`.
3. `power_amplifier` returns `amplified` (the function object, closure
   attached) and its own stack frame is popped. Ordinarily a function's
   locals disappear when it returns — but `base_spell` and `multiplier`
   don't disappear here, because the returned function object is still
   holding a live reference to the cells that hold them. This is what a
   closure *is*: not the value of `base_spell` copied out, but a
   continued reference to the variable itself, kept alive past the
   normal end of its scope.
4. The caller binds the returned function object to `mega_fireball`.
   No spell has been cast yet — nothing inside `amplified`'s body has
   executed.
5. Only when `mega_fireball("Dragon", 10)` is later called does the
   body of `amplified` actually run: `power * multiplier` evaluates to
   `10 * 3 = 30` (reading `multiplier` from the closure), and
   `base_spell("Dragon", 30)` calls the original `fireball` (also read
   from the closure) with the amplified value.

The same mechanism produces `combined` in `spell_combiner` (closing
over `spell1`/`spell2`), `cast` in `conditional_caster` (closing over
`condition`/`spell`), and `sequence` in `spell_sequence` (closing over
`spells`). In every case, the outer function's parameters are read
*later*, from inside the inner function, well after the outer call has
returned — that's only possible because they're captured by reference
via the closure, not passed by value at definition time.

## Running

```bash
python3 ex1/higher_magic.py
python3 -m ex1.main
```
