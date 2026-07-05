# ex3 — Game Engine

## Goal

Combine the **Abstract Factory** pattern (`CardFactory`) with the **Strategy**
pattern (`GameStrategy`) to produce a flexible, pluggable game-turn simulator.

## Files

<div align="center">

| File | Role |
|------|------|
| `GameStrategy.py` | Abstract strategy interface |
| `CardFactory.py` | Abstract factory interface |
| `AggressiveStrategy.py` | Concrete turn strategy |
| `FantasyCardFactory.py` | Concrete fantasy card factory |
| `GameEngine.py` | Orchestrator that binds factory + strategy |
| `main.py` | Demonstration entry-point |

</div>

## Class design

```
GameStrategy (ABC)
├── execute_turn(hand, battlefield) → dict  ← abstract
├── get_strategy_name() → str               ← abstract
└── prioritize_targets(targets) → list      ← abstract

AggressiveStrategy(GameStrategy)
└── Plays cheapest cards first; damage = ⌈cost × 1.5⌉ per card

CardFactory (ABC)
├── create_creature(name_or_power) → Card   ← abstract
├── create_spell(name_or_power) → Card      ← abstract
├── create_artifact(name_or_power) → Card   ← abstract
├── create_themed_deck(size) → dict         ← abstract
└── get_supported_types() → dict            ← abstract

FantasyCardFactory(CardFactory)
└── Dragons, Goblins, elemental spells, magical artifacts

GameEngine
├── configure_engine(factory, strategy) → None
├── simulate_turn() → dict
└── get_engine_status() → dict
```

## Running

```bash
# from repository root
python3 -m ex3.main
```

## Pylance notes

- `CardFactory.create_creature` signature uses `str | int | None` — Pylance
  enforces that only those three types are passed (Python ≥ 3.10 union syntax).
- `GameEngine` stores `Optional[CardFactory]` and `Optional[GameStrategy]`.
  Pylance narrows the type inside `simulate_turn()` via the `is None` guard,
  so no `# type: ignore` suppressions are needed.
- Swapping `FantasyCardFactory` for a future `SciFiCardFactory` (same abstract
  interface) requires **zero** changes to `GameEngine` — Pylance will confirm
  structural compatibility at the `configure_engine()` call site.
- `AggressiveStrategy.execute_turn` returns a typed `dict[str, Any]` that
  matches the abstract signature; returning an incompatible type would produce
  an `override` mismatch warning from Pylance.
