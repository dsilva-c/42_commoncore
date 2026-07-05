# ex2 — Ability System

## Goal

Design multiple abstract interfaces (`Combatable`, `Magical`) and implement
`EliteCard`, which inherits from **all three** hierarchies simultaneously via
Python's multiple inheritance.

## Files

| File | Role |
|------|------|
| `Combatable.py` | Abstract combat interface |
| `Magical.py` | Abstract magic interface |
| `EliteCard.py` | Multiple-inheritance implementation |
| `main.py` | Demonstration entry-point |

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
