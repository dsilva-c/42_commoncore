# ex1 — Deck Builder

## Goal

Implement concrete card types (`SpellCard`, `ArtifactCard`) alongside a `Deck`
management class that works with any `Card` subtype via polymorphism.

## Files

<div align="center">

| File | Role |
|------|------|
| `SpellCard.py` | Instant magical effects (consumed on play) |
| `ArtifactCard.py` | Permanent game modifiers (persist on battlefield) |
| `Deck.py` | Deck management — add, remove, shuffle, draw |
| `main.py` | Demonstration entry-point |

</div>

## Class design

```
Card  (ABC, ex0)
├── SpellCard(Card)
│   ├── __init__(name, cost, rarity, effect_type)
│   ├── play(game_state) → dict
│   └── resolve_effect(targets) → dict
└── ArtifactCard(Card)
    ├── __init__(name, cost, rarity, durability, effect)
    ├── play(game_state) → dict
    └── activate_ability() → dict

Deck
├── add_card(card: Card) → None
├── remove_card(card_name: str) → bool
├── shuffle() → None
├── draw_card() → Card
└── get_deck_stats() → dict
```

## Running

```bash
# from repository root
python3 -m ex1.main
```

> Draw order is random due to `Deck.shuffle()` — output will differ each run.

## Pylance notes

- `Deck._cards` is typed as `list[Card]` — Pylance enforces that only true `Card`
  subclasses can be added via `add_card()`.
- `draw_card()` returns `Card` and raises `ValueError` when the deck is empty;
  callers handle exhaustion via exception handling instead of `None` checks.
- `get_deck_stats()` returns `dict[str, object]`; accessing specific keys requires
  a cast or narrowing — a deliberate reminder that stats are aggregate values.
- Because `SpellCard` and `ArtifactCard` fully implement the abstract `play()`
  method, Pylance will **not** flag them as abstract. Removing `play()` from
  either class will immediately surface a Pylance error.
