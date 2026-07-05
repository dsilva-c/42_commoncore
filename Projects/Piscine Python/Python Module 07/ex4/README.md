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

## Concepts explained

### Synthesising two independent multiple-inheritance hierarchies

`TournamentCard(Card, Combatable, Rankable)` reaches across every prior
exercise: `Card` (ex0), `Combatable` (ex2), and a brand-new `Rankable`
interface introduced in this exercise. This is the same multiple
inheritance mechanic as `ex2`'s `EliteCard(Card, Combatable, Magical)`
— the C3-linearised MRO is:

```python
>>> from ex4.TournamentCard import TournamentCard
>>> [c.__name__ for c in TournamentCard.__mro__]
['TournamentCard', 'Card', 'Combatable', 'Rankable', 'ABC', 'object']
```

— but note that `EliteCard` and `TournamentCard` share the exact same
`Combatable` interface from `ex2` rather than redefining combat
methods. That's the payoff of `ex2`'s interface segregation: because
`Combatable` was already split out as its own reusable `ABC` (not fused
into `Card` or `Magical`), any later hierarchy can mix it in again
without dragging in unrelated capabilities. `TournamentCard.attack()`,
`.defend()`, and `.get_combat_stats()` are, in fact, implemented nearly
identically to `EliteCard`'s — the interface is doing its job of
letting unrelated card lineages (elite vs. tournament) share one
combat contract without sharing a class hierarchy otherwise.

`TournamentCard.__init__` calls `Card.__init__(self, name, cost,
rarity)` explicitly rather than `super().__init__(...)`. This works
because `Combatable` and `Rankable` are both pure interfaces with no
`__init__` of their own — there's no cooperative multi-parent
constructor chain to walk, so an explicit call to the one base that
*does* have meaningful `__init__` logic (`Card`) is sufficient and
unambiguous.

### `Rankable`: a third interface, same contract-enforcement mechanics as `Card`

`Rankable(ABC)` declares `calculate_rating()`, `update_wins(wins)`,
`update_losses(losses)`, and `get_rank_info()` as abstract — the same
`ABCMeta` mechanics from `ex0` apply here: any class that inherits
`Rankable` without implementing all four remains abstract and cannot be
instantiated. `TournamentCard` implements all four, so
`TournamentCard.__abstractmethods__` ends up empty and instances can be
built normally.

### Walking the rating calculation

`TournamentCard` stores two numbers instead of one running total:
`self._base_rating` (looked up once at construction from
`_RARITY_BASE_RATING.get(rarity, 1000)` — Legendary 1200, Rare 1150,
Uncommon 1100, Common 1050) and `self._rating_adjustment` (starts at
`0`). `calculate_rating()` simply returns `self._base_rating +
self._rating_adjustment` — it's a *derived* value, recomputed from the
two stored numbers rather than mutated directly, so `wins`/`losses`
and the adjustment can never drift out of sync with each other.

`update_wins(wins)` does `self.wins += wins` and
`self._rating_adjustment += _RATING_DELTA * wins`; `update_losses`
mirrors it with a `-=`. `_RATING_DELTA = 16` is a module-level constant,
so every match shifts rating by a fixed ±16 regardless of who the
opponent was — a simplified stand-in for a real ELO system (which
would scale the delta by the *ratings gap* between the two players).
`TournamentPlatform.create_match()` decides the winner purely by
comparing `card1.attack_power >= card2.attack_power` (ties go to
`card1`), then calls `winner.update_wins(1)` and `loser.update_losses(1)`
— both calls going through the `Rankable` interface, exactly the same
"depend on the abstraction" discipline as `Deck` (ex1) depending only
on `Card`: `TournamentPlatform` never needs to know `TournamentCard`'s
internal rating formula, only that it can call `update_wins` /
`update_losses` / `calculate_rating` on anything typed `Rankable`.

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
