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

## Concepts explained

### Programming to an interface, not an implementation

`Deck._cards` is typed `list[Card]`, and every method on `Deck` —
`add_card`, `remove_card`, `shuffle`, `draw_card`, `get_deck_stats` —
only ever calls methods that exist on `Card` itself (`.name`, `.cost`,
`.get_card_info()`). Nowhere does `Deck.py` import `CreatureCard`,
`SpellCard`, or `ArtifactCard`. Look at `get_deck_stats()`: it counts
creatures/spells/artifacts by reading `card.get_card_info().get("type")`
— a string produced by each *subclass's own* override of
`get_card_info()` — rather than by doing `isinstance(card,
CreatureCard)`. `Deck` never needs to know which concrete subclasses
exist at all.

This is the "program to an interface, not an implementation" principle:
a consumer of an abstraction (`Deck`) should depend only on the
abstraction's contract (`Card`'s public methods and attributes), never
on any one concrete class that satisfies it. Concretely, what this buys
you:

- **Open for extension, closed for modification.** Adding a fourth card
  type (say, `SkillCard`) next module requires zero changes to
  `Deck.py` — you write the new class, give it a `play()` and a
  `get_card_info()` that reports `"type": "Skill"`, and every existing
  `Deck` method already works with it because it never checked the
  concrete type.
- **Polymorphic collections.** `Deck._cards` mixes `CreatureCard`,
  `SpellCard`, and `ArtifactCard` instances in a single `list[Card]`.
  `shuffle()` and `draw_card()` operate on that list uniformly — the
  runtime dispatches `card.play(...)` to whichever subclass's override
  actually applies, without `Deck` ever branching on type.

**What would break if this principle were violated.** Imagine
`Deck.add_card` were written as:

```python
def add_card(self, card: "CreatureCard | SpellCard | ArtifactCard") -> None:
    ...
```

Now `Deck` has to `import CreatureCard, SpellCard, ArtifactCard` at the
top of the file — a hard dependency on every concrete card type that
exists *today*. Add a fifth card type tomorrow and this signature (and
every `isinstance` branch built on it) needs editing, even though
`Deck`'s actual behaviour — "store cards, shuffle them, draw them" —
hasn't conceptually changed at all. Worse, `Deck` would need one new
`elif` branch per type anywhere it inspected card kind, turning a class
that should be stable into one that changes every time the card
hierarchy grows. Depending only on `Card` avoids all of that: the
abstraction is the *only* thing `Deck` needs to know about.

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
