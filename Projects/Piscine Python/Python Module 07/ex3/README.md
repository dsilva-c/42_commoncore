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

## Concepts explained

### The Strategy pattern: making an algorithm swappable at runtime

`GameEngine` never has an `if strategy_type == "aggressive"` branch
anywhere. Instead, `configure_engine(factory, strategy)` stores whatever
`GameStrategy` instance it's given in `self._strategy`, typed
`Optional[GameStrategy]` — the abstract base, never
`AggressiveStrategy` by name. `simulate_turn()` then calls
`self._strategy.execute_turn(hand, [])` and
`self._strategy.get_strategy_name()` — both calls go through the
abstract interface only. `GameEngine` literally cannot see, at those
call sites, whether the object is an `AggressiveStrategy` or something
else; it only knows it satisfies `GameStrategy`'s contract
(`execute_turn`, `get_strategy_name`, `prioritize_targets`).

That's the Strategy pattern: **extract a family of interchangeable
algorithms behind one interface, and let the client hold a reference to
the interface, not to any specific algorithm.** The "algorithm" here is
"how a turn gets played" — `AggressiveStrategy.execute_turn` implements
one specific policy (sort `hand` by `cost` ascending, greedily spend
`self._mana_per_turn`, deal `(cost*3+1)//2` damage per card played,
i.e. `ceil(cost * 1.5)` computed with integer arithmetic to avoid
float rounding surprises). A hypothetical `DefensiveStrategy` could
implement a completely different policy — but as long as it subclasses
`GameStrategy` and implements the same three methods,
`configure_engine()` accepts it and `GameEngine.simulate_turn()`
requires zero modification to use it. The client (`GameEngine`) depends
on the abstraction; only the object actually plugged in at
`configure_engine()`-time depends on the concrete algorithm.

### The Abstract Factory pattern: not instantiating concrete classes directly

`GameEngine` also never writes `CreatureCard(...)`, `SpellCard(...)`,
or `FantasyCardFactory()` anywhere in its own code. Instead
`simulate_turn()` calls `self._factory.create_themed_deck(3)`, where
`self._factory` is typed `Optional[CardFactory]` — again the abstract
base. `FantasyCardFactory(CardFactory)` is the one place that actually
knows how to build `CreatureCard`, `SpellCard`, and `ArtifactCard`
instances (see `_CREATURES`/`_SPELLS`/`_ARTIFACTS` template dicts and
`create_creature`/`create_spell`/`create_artifact`); `GameEngine` just
asks the factory for a themed deck and gets back a `dict[str,
list[Any]]` of already-built `Card` objects.

This is the Abstract Factory pattern: **a client that needs a whole
*family* of related objects (creatures + spells + artifacts, all
sharing one theme) asks a factory object for them, rather than
instantiating each concrete class itself.** The payoff shows up when
you imagine swapping `FantasyCardFactory` for a hypothetical
`SciFiCardFactory(CardFactory)`: every method on `CardFactory` — the
whole product family — changes flavour (starships instead of dragons,
lasers instead of fireballs) simultaneously, purely by passing a
different factory into `configure_engine()`. `GameEngine.simulate_turn`
doesn't need to change at all, because it only ever calls
`create_themed_deck` through the `CardFactory` interface.

### How Strategy and Factory compose in `GameEngine`

The two patterns solve different problems and `GameEngine` uses both
independently:

- **Abstract Factory** varies *what gets created* — which concrete
  `Card` subclasses and flavour of content a themed deck contains.
- **Strategy** varies *what gets done with what already exists* — how
  the resulting hand of cards gets played this turn.

`configure_engine(factory, strategy)` accepts one of each, and
`simulate_turn()` chains them: first ask the factory for cards
(`create_themed_deck`), then ask the strategy what to do with them
(`execute_turn`). Because each dependency is swappable independently,
you get four behaviourally distinct engines (fantasy+aggressive,
fantasy+defensive, scifi+aggressive, scifi+defensive, etc.) out of two
factories × two strategies, without `GameEngine` ever branching on
either choice — it just calls through both abstractions in sequence.

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
