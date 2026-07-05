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

## Concepts explained

### Lexical scoping: why the inner function can still see outer variables

Python resolves a name by looking it up through a fixed chain of
scopes determined by *where the code is written* (lexical/static
scoping), not by which function happened to call which. The chain for
a nested function is: Local → Enclosing → Global → Built-in (LEGB).
When `counter()` (inside `mage_counter`) references `count`, Python
doesn't find `count` in `counter`'s own local scope, so it looks in the
*enclosing* scope — `mage_counter`'s frame — and finds it there. That
lookup path is decided once, when `counter` is defined (i.e., which
scope's `count` it refers to is fixed by the nesting in the source
code), not re-decided each time `counter` is called.

The subtler part: `mage_counter()` returns `counter` and its own frame
is popped off the call stack. Normally that would mean `count` is gone
— local variables of a returned-from function are usually garbage
collected. But because `counter` is a **closure** over `count`, Python
keeps the *cell* holding `count` alive as long as any function object
still references it. So calling `counter_a()` later still finds a
valid `count` to read and increment, even though `mage_counter()`'s own
call already finished long ago. This is the core claim of closures:
the inner function captures the *variable* (the cell), not a frozen
snapshot of its value at the moment the closure was created.

### `nonlocal`: only needed for reassignment

Compare `counter()` and `enchant()`:

```python
def counter() -> int:
    nonlocal count
    count += 1        # rebinds the name `count` — needs nonlocal
    return count

def enchant(item_name: str) -> str:
    return f"{enchantment_type} {item_name}"   # only reads — no nonlocal
```

`count += 1` is sugar for `count = count + 1` — an assignment. By
default, Python treats *any* name that is assigned to anywhere in a
function's body as local to that function (decided at compile time, by
scanning the function body for assignment targets — before the
function ever runs). Without `nonlocal count`, the line `count += 1`
would try to create a brand-new local `count` inside `counter`, and
reading it on the right-hand side before that new local has a value
would raise `UnboundLocalError`. `nonlocal count` tells Python: don't
treat this as a new local — this assignment should rebind the `count`
that already exists in the nearest enclosing function scope.

`enchant`, by contrast, never assigns to `enchantment_type` — it only
reads it inside the f-string. A plain read climbs the LEGB chain
automatically without any declaration; `nonlocal` (like `global`) is
exclusively about telling Python where an *assignment* should land, and
is a syntax error if there's no matching enclosing binding to attach
to. `spell_accumulator`'s `accumulate` needs `nonlocal total` for the
same reason `counter` needs `nonlocal count`: `total += amount` reassigns.

`memory_vault`'s `store` is the case that looks like reassignment but
isn't: `_vault[key] = value` is a **subscript assignment**, which
calls `_vault.__setitem__(key, value)` on the existing dict object —
it mutates the object that `_vault` already points to, it never
rebinds the name `_vault` itself to a different object. Since no name
in `store`'s scope is being assigned, no `nonlocal` is needed, even
though the vault's contents visibly change between calls.

### Two calls, two independent closures

```python
counter_a = mage_counter()
counter_b = mage_counter()
```

Each call to `mage_counter()` executes the function body from scratch,
which means each call creates its *own* new local variable `count = 0`
in its *own* new stack frame. `def counter():` then runs again inside
that fresh frame, producing a brand-new function object with its own
closure pointing at *that* frame's `count` cell — not the one from any
previous call. So `counter_a` and `counter_b` are two distinct function
objects, each closing over a distinct `count` cell:

```
counter_a() → 1      # increments counter_a's own count cell
counter_a() → 2
counter_b() → 1      # counter_b's count cell, untouched by counter_a
```

There is no shared state between them, and no way for one to affect
the other — exactly the encapsulation a closure-based factory is meant
to provide, without a class or a `global` variable in sight.

## Running

```bash
python3 ex2/scope_mysteries.py
python3 -m ex2.main
```
