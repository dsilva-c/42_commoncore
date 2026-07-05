# ex4 — Tournament Platform

## Goal

Synthesise every pattern learned so far into a **Tournament Platform** that
manages ranked matches between cards implementing `Card`, `Combatable`, and
`Rankable` simultaneously.

## Files

<div align="center">

| File | Role |
|------|------|
| `Rankable.py` | Abstract ranking interface |
| `TournamentCard.py` | Triple-inheritance tournament participant |
| `TournamentPlatform.py` | Platform management system |
| `main.py` | Demonstration entry-point |

</div>

## Class design

```
Rankable (ABC)
├── calculate_rating() → int      ← abstract
├── update_wins(wins) → None      ← abstract
├── update_losses(losses) → None  ← abstract
└── get_rank_info() → dict        ← abstract

TournamentCard(Card, Combatable, Rankable)
├── Inherits ALL abstract methods from three interfaces
├── Rating system: base from rarity + ±16 per win/loss
└── get_tournament_stats() → dict   ← platform helper

TournamentPlatform
├── register_card(card) → str         (returns unique ID)
├── create_match(id1, id2) → dict
├── get_leaderboard() → list[dict]
└── generate_tournament_report() → dict
```

## Rating system

<div align="center">

| Rarity | Base rating |
|--------|-------------|
| Legendary | 1200 |
| Rare | 1150 |
| Uncommon | 1100 |
| Common | 1050 |

</div>

Each match applies a fixed delta of **+16** (winner) / **−16** (loser).

## Running

```bash
# from repository root
python3 -m ex4.main
```

## Pylance notes

- `TournamentCard` inherits from three ABCs — Pylance tracks each separately
  and will flag any missing implementation with a precise error pointing to the
  unimplemented method name and its origin interface.
- `TournamentPlatform._cards` is typed `dict[str, TournamentCard]`, so
  `register_card` and `create_match` operate on strongly-typed values —
  Pylance will reject non-`TournamentCard` arguments at call sites.
- `get_leaderboard()` returns `list[dict[str, Any]]`; each entry's fields are
  documented in the method body — narrowing individual entries requires
  `cast()` or key access, which Pylance will type as `Any` (as expected for
  heterogeneous dict values).
- The `_RARITY_BASE_RATING` module-level dict is typed
  `dict[str, int]`; using `.get(rarity, 1000)` avoids a `KeyError` and keeps
  the narrowed return type as `int` — no Pylance narrowing warning.
- Because `TournamentCard.__init__` calls `Card.__init__` explicitly and the
  other two bases have no `__init__`,  Pylance does not detect any `super()`
  chain conflict.
