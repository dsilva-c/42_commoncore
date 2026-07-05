# DataDeck — Master the Art of Abstract Card Architecture

Python Piscine · Module 07

## 📋 Overview

A modular trading-card-game engine that progressively demonstrates Python's
abstract-programming patterns: abstract base classes, multiple inheritance,
the Strategy pattern, and the Abstract Factory pattern. Built with Python
3.10+, fully type-annotated, and validated with flake8 and Pylance/pyright
in strict mode.

<div align="center">

| Exercise | Focus | Key Patterns |
|----------|-------|--------------|
| ex0 | Card Foundation | Abstract Base Class, Enum, Type Hints |
| ex1 | Deck Builder | Concrete Card Types, Deck Management |
| ex2 | Ability System | Multiple Interfaces, Multiple Inheritance |
| ex3 | Game Engine | Abstract Factory + Strategy Patterns |
| ex4 | Tournament Platform | Advanced Interface Composition |

</div>

## 🎯 Learning Objectives

- Define and enforce contracts with `ABC` and `@abstractmethod`, and
  understand why an abstract class cannot be instantiated until every
  abstract method is implemented.
- Program to an interface rather than a concrete implementation (e.g. a
  `Deck` that only ever depends on `Card`, never on `CreatureCard`,
  `SpellCard`, etc.).
- Compose multiple independent interfaces via multiple inheritance and
  reason about Python's C3-linearised Method Resolution Order (MRO).
- Distinguish when structural typing (`Protocol`) is appropriate versus
  when real, shared-behaviour inheritance (`ABC`) is the better tool.
- Apply the Strategy pattern to make an algorithm swappable at runtime
  without modifying the client that uses it.
- Apply the Abstract Factory pattern to produce families of related
  objects without the client depending on their concrete classes.
- Use `Enum` to validate a closed set of values (`Rarity`) instead of
  accepting arbitrary strings.

## 📁 Project Structure

```
.
├── __init__.py          # Required for absolute imports
├── main.py              # Chains all five exercise main() functions
├── ex0/
│   ├── __init__.py
│   ├── Card.py
│   ├── CreatureCard.py
│   ├── main.py
│   └── README.md
├── ex1/
│   ├── __init__.py
│   ├── SpellCard.py
│   ├── ArtifactCard.py
│   ├── Deck.py
│   ├── main.py
│   └── README.md
├── ex2/
│   ├── __init__.py
│   ├── Combatable.py
│   ├── Magical.py
│   ├── EliteCard.py
│   ├── main.py
│   └── README.md
├── ex3/
│   ├── __init__.py
│   ├── GameStrategy.py
│   ├── CardFactory.py
│   ├── AggressiveStrategy.py
│   ├── FantasyCardFactory.py
│   ├── GameEngine.py
│   ├── main.py
│   └── README.md
├── ex4/
│   ├── __init__.py
│   ├── Rankable.py
│   ├── TournamentCard.py
│   ├── TournamentPlatform.py
│   ├── main.py
│   └── README.md
└── tools/               # Development helpers — NOT submitted
    └── card_generator.py
```

## 🚀 Usage

Execute all exercises from the **repository root**:

```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
```

Or run every exercise's demo in one go via the root entry point:

```bash
python3 main.py
```

## 📚 Exercises

### ex0 — Card Foundation

`ex0/Card.py`, `ex0/CreatureCard.py`

Establishes `Card(ABC)`, the abstract base class every card type in
DataDeck inherits from.

- `Card` cannot be instantiated directly — the abstract `play(game_state)`
  method is the contract every subtype must fulfil, while
  `get_card_info()` and `is_playable(available_mana)` are shared concrete
  helpers.
- `Rarity(Enum)` (`Common`, `Uncommon`, `Rare`, `Legendary`) validates
  rarity values at construction time.
- `CreatureCard(Card)` adds `attack` and `health`, implements `play()`,
  and exposes a creature-specific `attack_target()`.

### ex1 — Deck Builder

`ex1/SpellCard.py`, `ex1/ArtifactCard.py`, `ex1/Deck.py`

Adds two more concrete card types and a `Deck` manager that never depends
on any concrete card class.

- `SpellCard(Card)` models instant, consumed-on-play effects;
  `ArtifactCard(Card)` models permanent, persistent modifiers. Both fully
  implement `play()`.
- `Deck` stores `list[Card]` and only relies on the `Card` interface —
  `add_card()`, `remove_card()`, `shuffle()` (via `random.shuffle`),
  `draw_card()` (pops index 0, raises `ValueError` when empty), and
  `get_deck_stats()` (counts cards by type).
- This is "programming to an interface, not an implementation": adding a
  new card type never requires touching `Deck`.

### ex2 — Ability System

`ex2/Combatable.py`, `ex2/Magical.py`, `ex2/EliteCard.py`

Introduces two independent capability interfaces and combines them with
`Card` via multiple inheritance.

- `Combatable(ABC)` models "can fight": abstract `attack()`, `defend()`,
  `get_combat_stats()`.
- `Magical(ABC)` models "can cast": abstract `cast_spell()`,
  `channel_mana()`, `get_magic_stats()`. Kept separate from `Combatable`
  so a card that is magical but not combatable (or vice versa) isn't
  forced to implement unneeded methods.
- `EliteCard(Card, Combatable, Magical)` implements every abstract method
  from all three bases; `isinstance(elite, Combatable)` and
  `isinstance(elite, Magical)` both return `True`.
- MRO: `EliteCard → Card → Combatable → Magical → ABC → object`.

### ex3 — Game Engine

`ex3/GameStrategy.py`, `ex3/CardFactory.py`, `ex3/AggressiveStrategy.py`,
`ex3/FantasyCardFactory.py`, `ex3/GameEngine.py`

Combines the Strategy and Abstract Factory patterns into a pluggable
turn simulator.

- `GameStrategy(ABC)` — abstract `execute_turn()`, `get_strategy_name()`,
  `prioritize_targets()`. `AggressiveStrategy` plays the cheapest cards
  first, with damage roughly proportional to mana cost.
- `CardFactory(ABC)` — abstract `create_creature()`, `create_spell()`,
  `create_artifact()`, `create_themed_deck()`, `get_supported_types()`.
  `FantasyCardFactory` produces dragons, goblins, elemental spells, and
  magical artifacts.
- `GameEngine` is wired with a factory and a strategy via
  `configure_engine()`; `simulate_turn()` returns a structured result
  dict. Swapping either dependency changes engine behaviour without
  modifying `GameEngine` itself.

### ex4 — Tournament Platform

`ex4/Rankable.py`, `ex4/TournamentCard.py`, `ex4/TournamentPlatform.py`

Synthesises every prior pattern into a ranked-match platform.

- `Rankable(ABC)` — abstract `calculate_rating()`, `update_wins()`,
  `update_losses()`, `get_rank_info()`.
- `TournamentCard(Card, Combatable, Rankable)` reaches back through the
  ex0 and ex2 hierarchies; rating starts from a rarity-based baseline
  (Legendary 1200, Rare 1150, Uncommon 1100, Common 1050) and shifts by
  ±16 per win/loss.
- `TournamentPlatform` registers cards under name-based IDs (a per-name
  counter avoids collisions) and stores them in
  `dict[str, TournamentCard]`; `create_match()` updates both cards'
  ratings and returns a structured result, or an error dict for unknown
  IDs.

## 🧠 Key Concepts

**Abstract Base Class** — `class Card(ABC): @abstractmethod def
play(...): ...` prevents instantiation until every subclass supplies a
concrete `play()`. This is enforced by the interpreter at instantiation
time, not just by a type checker.

**Multiple inheritance + MRO** — `EliteCard(Card, Combatable, Magical)`
and `TournamentCard(Card, Combatable, Rankable)` combine independent
capability interfaces. Python's C3 linearisation determines method
resolution order left-to-right, depth-first per the base order in the
class definition; inspect it directly with `ClassName.__mro__`.
Cooperative `super().__init__()` calls walk that same MRO correctly as
long as every class in the chain also calls `super().__init__()`.

**Strategy pattern** — `GameEngine` holds a `GameStrategy` reference and
calls it only through the abstract interface. Swapping
`AggressiveStrategy` for a different strategy changes turn behaviour
without touching `GameEngine`.

**Abstract Factory pattern** — `GameEngine` similarly holds a
`CardFactory` reference. Swapping `FantasyCardFactory` for a different
themed factory changes which card flavours get produced, again without
modifying `GameEngine`.

**Card hierarchy design** — `Deck` (ex1) and `GameEngine`/`CardFactory`
(ex3) all depend only on the `Card` / `GameStrategy` / `CardFactory`
abstractions, never on concrete subclasses. This keeps the codebase open
for extension (new card types, strategies, factories) and closed for
modification (no existing class needs to change).

## 🧪 Testing

This module has no pytest suite. Correctness is verified by running each
exercise's demonstration entry point and inspecting the printed output:

```bash
python3 -m ex0.main   # card creation, playability check, play result
python3 -m ex1.main   # deck build, shuffle, draw-until-empty
python3 -m ex2.main   # isinstance checks across Card/Combatable/Magical
python3 -m ex3.main   # configured engine simulating one turn
python3 -m ex4.main   # card registration and a simulated tournament match
```

Static analysis is used as an additional correctness gate — see
Code Style & Requirements below.

## ✅ Code Style & Requirements

- **Python ≥ 3.10** — modern union syntax (`str | int | None`) is used in
  signatures such as `CardFactory.create_creature`.
- **Full type annotations** on every function signature and class method.
  `Any` is used where a heterogeneous return type is intentional (e.g.
  result dicts); `dict[str, Any]` is the standard return shape for
  `play()`, `get_*_stats()`, and similar methods.
- **`from abc import ABC, abstractmethod`** for every abstract class, so
  Pylance/pyright correctly flags any subclass that fails to implement
  an abstract method ("Cannot instantiate abstract class").
- `Rarity(Enum)` validates card rarity in `Card`; invalid rarities raise
  `ValueError` at construction time instead of failing silently later.
- `Deck.draw_card()` raises `ValueError` on an empty deck; callers handle
  exhaustion via exception handling rather than `None` checks.
- **Authorized imports**: standard library only — `abc`, `typing`,
  `random`, `enum`, `datetime`, and similar. External packages
  (`pip install …`) are forbidden.
- Run a static-analysis sanity check with pyright/Pylance:

  ```bash
  python3 -m pyright .   # optional, requires pyright installed
  ```

  Each exercise directory's own `README.md` documents exercise-specific
  Pylance notes (e.g. how narrowing behaves around `Optional[CardFactory]`
  in ex3, or how `TournamentPlatform._cards` being typed
  `dict[str, TournamentCard]` rejects non-`TournamentCard` arguments at
  call sites in ex4).

## 🛡️ Defense Notes

- **MRO in practice**: `EliteCard` and `TournamentCard` both inherit from
  multiple mixins (e.g. `Combatable`, `Magical`, `Rankable`) — Python
  resolves method calls via `__mro__` (left-to-right, depth-first per
  base order), so the order bases are listed in the class definition
  determines which mixin's method wins on a name clash. For `EliteCard`
  that's `EliteCard → Card → Combatable → Magical → ABC → object`; for
  `TournamentCard` it's `TournamentCard → Card → Combatable → Rankable →
  ABC → object`.
- **ABC vs `Protocol`**: an `ABC` with `@abstractmethod` enforces
  inheritance and blocks instantiation until every abstract method is
  implemented — enforced by the interpreter, no runtime call needed to
  discover the bug. A `Protocol` instead checks structurally (duck
  typing), verified only by a type checker. ABCs were used here because
  the card hierarchy needed real inheritance and shared behaviour (e.g.
  `Card.get_card_info()`, `Card.is_playable()`), not just a shared
  interface.
- **Why two separate ability interfaces instead of one**: `Combatable`
  and `Magical` model independent capability axes. A `SpellCard` might be
  `Magical` but not `Combatable`; merging them into a single interface
  would force every card to implement abilities it doesn't have.
- **Why `Deck` never imports concrete card classes**: if `Deck` imported
  `CreatureCard` directly, adding a new card type would require modifying
  `Deck`. By depending only on `Card`, `Deck` stays open for extension
  and closed for modification.
- **Cooperative `super()` with multiple inheritance**: `super().__init__()`
  works correctly across multiple inheritance because it walks the MRO,
  not just the immediate parent — as long as every `__init__` in the
  chain also calls `super().__init__()`. Where a base class has no
  `__init__` of its own (e.g. `Combatable`, `Magical`), there's no
  diamond-`__init__` ambiguity to resolve.
- **Strategy vs Abstract Factory, briefly**: Strategy varies a single
  *algorithm* (how a turn is executed); Abstract Factory varies a
  *family of objects being created* (which card flavours a factory
  produces). `GameEngine` in ex3 uses both simultaneously, each
  independently swappable.
- **Common errors**:
  - `TypeError: Can't instantiate abstract class` — a subclass is
    missing an implementation for one or more `@abstractmethod`s; check
    the error message for exactly which method and interface.
  - Unexpected `AttributeError` on a multiply-inherited class — usually
    means the MRO resolved to a different base than expected; inspect
    `ClassName.__mro__` to confirm resolution order.
  - `ImportError` when running an exercise directly — exercises must be
    run as modules from the module root (e.g. `python3 -m ex1.main`),
    not as bare scripts, since they use absolute imports across
    exercise packages.

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
