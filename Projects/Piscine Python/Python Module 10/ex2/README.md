# ex2 — Memory Depths

## Goal

Understand **lexical scoping** and **closures**: how an inner function
remembers variables from the scope in which it was defined, even after
that scope has finished executing.

## Files

<div align="center">

| File | Role |
|------|------|
| `scope_mysteries.py` | Four closure factories + `main()` |
| `main.py` | Module-style entry-point |

</div>

## Function design

```
mage_counter()                   → Callable[[], int]       stateful counter
spell_accumulator(initial_power) → Callable[[int], int]    running total
enchantment_factory(type)        → Callable[[str], str]    apply enchantment
memory_vault()                   → dict[str, Callable]     private key-value store
```

## Key concepts

- **Closure** — an inner function that captures free variables from the
  enclosing function's local scope.
- **`nonlocal`** — declares that a name refers to a variable bound in the
  nearest enclosing non-global scope, enabling mutation.
- **State without globals** — closures provide a clean alternative to global
  variables for maintaining state between calls.
- **Lexical scoping** — Python resolves names at the location where functions
  are *defined*, not where they are *called*.

## Running

```bash
python3 ex2/scope_mysteries.py
python3 -m ex2.main
```
