# ex2 — Ability System

## Goal

Design multiple abstract interfaces (`Combatable`, `Magical`) and implement
`EliteCard`, which inherits from **all three** hierarchies simultaneously via
Python's multiple inheritance.

## Files

<div align="center">

| File | Role |
|------|------|
| `Combatable.py` | Abstract combat interface |
| `Magical.py` | Abstract magic interface |
| `EliteCard.py` | Multiple-inheritance implementation |
| `main.py` | Demonstration entry-point |

</div>

## Class design

```
ABC
├── Combatable
│   ├── attack(target) → dict          ← abstract
│   ├── defend(incoming_damage) → dict ← abstract
│   └── get_combat_stats() → dict      ← abstract
└── Magical
    ├── cast_spell(spell_name, targets) → dict ← abstract
    ├── channel_mana(amount) → dict            ← abstract
    └── get_magic_stats() → dict               ← abstract

EliteCard(Card, Combatable, Magical)
├── Implements ALL abstract methods from Card, Combatable, Magical
└── MRO: EliteCard → Card → Combatable → Magical → ABC → object
```

## Concepts explained

### Multiple inheritance mechanics: how `EliteCard(Card, Combatable, Magical)` actually resolves a call

`class EliteCard(Card, Combatable, Magical)` gives `EliteCard` three
direct base classes. Every one of them (transitively) inherits from
`ABC`, which itself inherits from `object` — so naively this looks like
a diamond: three paths from `EliteCard` down to `object`. Python
resolves *which* implementation wins on a name clash using the **C3
linearisation algorithm**, producing the class's Method Resolution
Order (MRO), inspectable directly:

```python
>>> from ex2.EliteCard import EliteCard
>>> [c.__name__ for c in EliteCard.__mro__]
['EliteCard', 'Card', 'Combatable', 'Magical', 'ABC', 'object']
```

C3 linearisation guarantees two things: (1) a subclass always appears
before its parents, and (2) the *order bases were listed in the class
statement* is preserved in the final order — here, `Card` before
`Combatable` before `Magical`, exactly as written in `class
EliteCard(Card, Combatable, Magical)`. When you call
`elite_card.get_card_info()`, Python doesn't search "the parent" — it
walks `EliteCard.__mro__` left to right and uses the **first** class in
that list that defines `get_card_info`. `EliteCard` defines its own, so
that wins; if it didn't, `Card.get_card_info` would be used next (since
`Card` precedes `Combatable`/`Magical` in the MRO), regardless of the
fact that `Combatable`/`Magical` are also ancestors. This is why base
order in the class definition is not cosmetic — swapping it to `class
EliteCard(Combatable, Magical, Card)` would change which base wins any
future name collision.

C3 linearisation is also verified *at class definition time*, not at
first use: if the base list can't produce a consistent linear order
(a genuine diamond conflict), Python raises `TypeError: Cannot create a
consistent method resolution order` the moment the `class` statement
executes, before any instance is ever created.

### Why `Combatable` and `Magical` are two interfaces, not one

`Combatable` (`attack`, `defend`, `get_combat_stats`) and `Magical`
(`cast_spell`, `channel_mana`, `get_magic_stats`) are declared as two
separate `ABC`s rather than one `Ability` interface with all six
methods. This is **interface segregation**: no class should be forced
to depend on (or implement) methods it doesn't use. `EliteCard` happens
to need both, but the split matters for every card that *doesn't*:
a future purely-physical creature could inherit `Card, Combatable`
without being forced to stub out `cast_spell`/`channel_mana` with dummy
bodies just to satisfy a merged interface, and a pure spellcaster could
inherit `Card, Magical` without pretending to have combat stats. Had
`Combatable` and `Magical` been merged, every card wanting *either*
capability would have to implement (or fake) both, which is exactly the
kind of forced, meaningless implementation interface segregation exists
to prevent.

Because `EliteCard` inherits from both, `isinstance()` checks against
either interface independently tell you what the object can actually
do, regardless of its concrete class:

```python
>>> isinstance(elite_card, Combatable)
True
>>> isinstance(elite_card, Magical)
True
```

This matters wherever code wants to treat objects generically by
capability rather than by concrete type — e.g. a battle system could
accept `list[Combatable]` and call `.attack()` on each entry without
caring whether the underlying object is an `EliteCard`, a future
`Warrior` card, or anything else that happens to implement
`Combatable`. The `isinstance` check (or, more idiomatically, just
calling the method and letting `AttributeError`/duck typing handle it)
is how you query "does this satisfy the `Combatable` contract?" without
hardcoding a list of concrete classes — the same "depend on the
abstraction" idea from `ex1`'s `Deck`, applied to capabilities instead
of card types.

## Running

```bash
# from repository root
python3 -m ex2.main
```

## Pylance notes

- Python's **C3 linearisation** (MRO) is automatically verified at class
  definition time — a conflicting MRO raises `TypeError` immediately, no
  Pylance intervention needed.
- Pylance marks `EliteCard` as **concrete** only after every abstract method
  from every base class is implemented. Removing even one abstract method body
  turns the class abstract and surfaces a "Cannot instantiate abstract class"
  error wherever `EliteCard(...)` is called.
- Both `Combatable` and `Magical` are pure interfaces (no `__init__` of their
  own), so there is no diamond `__init__` ambiguity; Pylance will not warn
  about conflicting constructors.
- `EliteCard.__init__` calls `Card.__init__` explicitly (cooperative
  `super().__init__` is unnecessary here) — the explicit call keeps the
  Pylance "partially unknown type" hint away.
- All return types are `dict[str, Any]`; any deviation (e.g. returning
  a `list`) will produce a Pylance return-type mismatch warning.
