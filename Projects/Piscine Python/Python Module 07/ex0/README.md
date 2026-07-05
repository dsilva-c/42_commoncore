# ex0 — Card Foundation

## Goal

Establish the abstract base class (`Card`) that acts as the universal blueprint
for every card type in DataDeck.

## Files

<div align="center">

| File | Role |
|------|------|
| `Card.py` | Abstract base class — defines the contract |
| `CreatureCard.py` | First concrete implementation |
| `main.py` | Demonstration entry-point |

</div>

## Class design

```
Card  (ABC)
├── __init__(name, cost, rarity)
├── play(game_state) → dict          ← abstract
├── get_card_info()  → dict          ← concrete
└── is_playable(available_mana) → bool ← concrete

CreatureCard(Card)
├── __init__(name, cost, rarity, attack, health)
├── play(game_state) → dict          ← implements abstract
├── get_card_info()  → dict          ← extended
└── attack_target(target) → dict     ← creature-specific
```

## Concepts explained

### Abstract Base Classes: a contract enforced by the interpreter

`Card` inherits from `ABC` (`from abc import ABC, abstractmethod`) and
declares `play()` with the `@abstractmethod` decorator but no meaningful
body (just a docstring). This does two distinct things, one at class
*definition* time and one at instantiation time:

1. **`ABC` sets a custom metaclass** (`ABCMeta`) on `Card`. A metaclass is
   the class of a class — it controls how the class object itself is
   built. `ABCMeta` tracks, in `Card.__abstractmethods__`, the set of
   method names that were decorated with `@abstractmethod` and never
   overridden in the current class body.
2. **Every time you call `SomeClass(...)`**, `ABCMeta.__call__` checks
   whether `SomeClass.__abstractmethods__` is non-empty. If it is,
   Python raises `TypeError: Can't instantiate abstract class SomeClass
   with abstract method play` *before* `__init__` ever runs.

Try it directly:

```python
>>> from ex0.Card import Card
>>> Card("Test", 1, "Common")
TypeError: Can't instantiate abstract class Card with abstract method play
```

This is fundamentally different from a linter or type-checker complaint.
Pylance/pyright can *flag* an incomplete subclass in your editor, but
that's a static, optional check — nothing stops you from running the
code anyway. `ABCMeta` performs the check inside the interpreter itself,
at the moment `__call__` executes, so the failure is a hard runtime
error with no way to opt out short of removing `ABC` from the bases.
That's what makes an abstract base class a *contract*: `Card` documents
"any real card must know how to `play()`", and the language enforces
it, not just a style guide.

Meanwhile `get_card_info()` and `is_playable()` are ordinary concrete
methods on `Card` — they don't need per-subclass logic, so they're
implemented once and inherited by every card type (`CreatureCard` in
this exercise, plus `SpellCard`/`ArtifactCard`/`EliteCard`/
`TournamentCard` later). This is the point of `ABC` over a bare
interface: it lets a class mix "you must implement this" (`play`) with
"here's shared behaviour you get for free" (`get_card_info`,
`is_playable`) in the same hierarchy.

### `Enum` validation vs. plain strings

`Rarity(Enum)` defines exactly four members (`LEGENDARY`, `RARE`,
`UNCOMMON`, `COMMON`), each bound to a string value. `Card.__init__`
checks the incoming `rarity` argument against `{r.value for r in
Rarity}` and raises `ValueError("Invalid rarity")` immediately if it
doesn't match. Compare that to accepting a bare `str`:

```python
# Without Enum validation, this silently "succeeds":
Card("Bug", 3, "legndary")   # typo — no error, garbage rarity stored
```

An `Enum` gives you a **closed, named set of legal values** instead of
the infinite space of `str`. The validation in `Card.__init__` converts
what would otherwise be a silent data-quality bug (a stored rarity of
`"legndary"` that later fails to match anything meaningful) into a loud
`ValueError` at the exact call site where the bad value was supplied.
This is "fail fast": the error surfaces at construction time, right next
to the mistake, rather than much later when something tries to look up
`"legndary"` in a rarity-keyed table and gets a `KeyError` or a wrong
default three functions away from the actual bug. It's the same idea
`Deck.draw_card()` uses later with `ValueError` on an empty deck: raise
immediately and specifically, rather than let bad state propagate.

## Running

```bash
# from repository root
python3 -m ex0.main
```

## Pylance notes

- `Card` inherits from `ABC` — Pylance will flag any subclass that does **not**
  implement `play()` as an error ("Cannot instantiate abstract class").
- `Card` validates `rarity` against a `Rarity` enum, so invalid rarities raise
  `ValueError` early and keep the contract explicit.
- All method signatures use `dict[str, Any]` (Python 3.10+) so Pylance has full
  type information with no `Missing type parameters` warnings.
- `attack` and `health` are validated as positive `int` at construction time;
  the type narrowing is explicit so Pylance does not infer `int | unknown`.
- Passing an incompletely-implemented subclass of `Card` to any typed function
  expecting `Card` will produce a Pylance type error, demonstrating the
  enforcement value of abstract classes.
