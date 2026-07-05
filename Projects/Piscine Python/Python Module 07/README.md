# DataDeck — Master the Art of Abstract Card Architecture

Python Piscine · Module 07

## Overview

A modular trading-card-game engine that progressively demonstrates Python's
abstract-programming patterns.

| Exercise | Focus | Key Patterns |
|----------|-------|--------------|
| ex0 | Card Foundation | Abstract Base Class, Enum, Type Hints |
| ex1 | Deck Builder | Concrete Card Types, Deck Management |
| ex2 | Ability System | Multiple Interfaces, Multiple Inheritance |
| ex3 | Game Engine | Abstract Factory + Strategy Patterns |
| ex4 | Tournament Platform | Advanced Interface Composition |

## Project structure

```
.
├── __init__.py          # Required for absolute imports
├── ex0/
│   ├── __init__.py
│   ├── Card.py
│   ├── CreatureCard.py
│   └── main.py
├── ex1/
│   ├── __init__.py
│   ├── SpellCard.py
│   ├── ArtifactCard.py
│   ├── Deck.py
│   └── main.py
├── ex2/
│   ├── __init__.py
│   ├── Combatable.py
│   ├── Magical.py
│   ├── EliteCard.py
│   └── main.py
├── ex3/
│   ├── __init__.py
│   ├── GameStrategy.py
│   ├── CardFactory.py
│   ├── AggressiveStrategy.py
│   ├── FantasyCardFactory.py
│   ├── GameEngine.py
│   └── main.py
├── ex4/
│   ├── __init__.py
│   ├── Rankable.py
│   ├── TournamentCard.py
│   ├── TournamentPlatform.py
│   └── main.py
└── tools/               # Development helpers — NOT submitted
    ├── __init__.py
    └── card_generator.py
```

## Running exercises

Execute all exercises from the **repository root**:

```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
```

## Pylance / static analysis

All files use:
- **Full type annotations** on every function signature and class method.
- **`from abc import ABC, abstractmethod`** for abstract classes so Pylance
  correctly flags missing implementations.
- Modern union syntax (`str | int | None`) requiring Python ≥ 3.10.
- `Any` where a heterogeneous return type is intentional (e.g. result dicts).
- `Rarity(Enum)` validation in `Card` for consistent rarity values.
- `Deck.draw_card()` raises `ValueError` on empty decks; demos handle it.

Run a quick sanity check with pyright/Pylance:

```bash
python3 -m pyright .   # optional, requires pyright installed
```

> Each exercise directory contains its own `README.md` with exercise-specific
> Pylance notes.

## Authorized imports

`abc`, `typing`, `random`, `enum`, `datetime`, and other standard library modules only.
External packages (`pip install …`) are **forbidden**.
