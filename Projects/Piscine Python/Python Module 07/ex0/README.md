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
