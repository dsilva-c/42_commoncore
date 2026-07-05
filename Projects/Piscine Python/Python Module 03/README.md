# Module 03 - Data Quest
## Mastering Python Collections for Data Engineering

*Python Collections, Generators & Comprehensions*

---

## 📋 Overview

This module builds a small "PixelMetrics 3000" game-analytics toolkit to
drill Python's core collection types and the tools built around them. Each
exercise isolates one data structure — lists, tuples, sets, dictionaries —
plus generators and comprehensions, and applies it to a realistic
analytics task (score crunching, coordinate tracking, achievement
comparison, inventory management, event streaming, data transformation).

**Python Version**: 3.10+
**Focus**: Collections, Generators, Comprehensions

---

## 🎯 Learning Objectives

- Choose the right built-in collection (list, tuple, set, dict) based on
  ordering, mutability, and uniqueness requirements
- Process `sys.argv` for CLI-driven scripts, including graceful handling
  of missing or malformed arguments
- Validate and convert user input safely with `try/except`
- Perform set algebra (`union()`, `intersection()`, `difference()`) to
  compare collections
- Build and update dictionaries as key-value stores with `O(1)` lookups
- Write generator functions with `yield` for lazy, memory-efficient
  iteration, and understand how `next()` and `for` consume them
- Replace explicit loops with list/dict comprehensions where they improve
  clarity

---

## 📁 Project Structure

```
Python Module 03/
├── ex0/
│   └── ft_command_quest.py        # Command-line argument processing
├── ex1/
│   └── ft_score_analytics.py      # List-based score analytics
├── ex2/
│   └── ft_coordinate_system.py    # Tuple-based 3D coordinates
├── ex3/
│   └── ft_achievement_tracker.py  # Set operations for achievements
├── ex4/
│   └── ft_inventory_system.py     # Dictionary-based inventory
├── ex5/
│   └── ft_data_stream.py          # Generator data streaming
├── ex6/
│   └── ft_data_alchemist.py       # Comprehensions with lists/dicts
├── main.py                        # Test suite for all exercises
├── README.md                      # This file
└── en.subject.pdf                 # Original project subject
```

---

## 🚀 Usage

### Run All Tests
```bash
python3 main.py
```
This drives every exercise in sequence (including the no-argument and
with-argument variants) and prints each one's output under a labeled
separator.

### Run Individual Exercises
```bash
python3 ex0/ft_command_quest.py
python3 ex0/ft_command_quest.py hello world 42
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ex2/ft_coordinate_system.py
python3 ex3/ft_achievement_tracker.py
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1
python3 ex5/ft_data_stream.py
python3 ex6/ft_data_alchemist.py
```
Exercise 2 reads coordinates from stdin interactively (format `x,y,z`);
the other exercises that take input do so via CLI arguments.

### Check Code Quality
```bash
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/ main.py \
    --max-line-length=79
```

---

## 📚 Exercises

### Exercise 0: Command Quest (`ex0/ft_command_quest.py`)
Print the program name and every argument passed on the command line.
- `sys.argv[0]` is always the program/script path; `sys.argv[1:]` holds
  the user-supplied arguments
- Handles the no-argument case with a dedicated message instead of an
  empty loop
- Uses `enumerate(user_args, start=1)` to number arguments starting at 1
  for display, while `len(sys.argv)` (which includes the program name)
  is reported as the total

### Exercise 1: Score Cruncher (`ex1/ft_score_analytics.py`)
Compute aggregate statistics over a list of player scores taken from
`sys.argv`.
- Scores are accumulated in a `list[int]` via `append()`, since the
  input size is unknown ahead of time
- Each argument is converted with `int(arg)` inside `try/except
  ValueError`, so a bad token is reported and skipped instead of
  crashing the script
- Total, average, high, low, and range are derived with `sum()`,
  `max()`, `min()`, and plain arithmetic

### Exercise 2: Position Tracker (`ex2/ft_coordinate_system.py`)
Read two 3D coordinates from stdin and compute distances.
- `get_player_pos()` loops with `while True`, re-prompting until it
  receives exactly three comma-separated values that all parse as
  `float`
- Coordinates are returned as an immutable `tuple[float, float, float]`
  and unpacked/indexed (`first[0]`, `first[1]`, `first[2]`)
- Uses `math.sqrt()` to compute the Euclidean distance from the origin
  to the first point, then the distance between the two points

### Exercise 3: Achievement Hunter (`ex3/ft_achievement_tracker.py`)
Generate randomized achievement sets for four players and compare them.
- `gen_player_achievements()` uses `random.sample()` on a fixed
  `ACHIEVEMENTS` list to build a `set[str]` per player (4-9 achievements,
  no duplicates)
- `union()` builds the set of every achievement earned by anyone
- Repeated `intersection()` across all players' sets finds achievements
  everyone shares
- Per player, `difference()` against the union of every other player's
  set isolates achievements only that player has, and `difference()`
  against the global union finds what they're still missing

### Exercise 4: Inventory Master (`ex4/ft_inventory_system.py`)
Parse `item:qty` arguments into an inventory and report on it.
- `parse_inventory()` splits each argument on `:`, rejecting malformed
  tokens, empty names, non-integer quantities, and duplicate item names
  (first occurrence wins, later ones are discarded as "redundant")
- The inventory is a `dict[str, int]`; totals and per-item percentages
  are computed by iterating `inventory.items()`/keys
- Most/least abundant items are found in a single pass using
  `iter(inventory)` and `next()` to seed the first candidate
- `inventory.update({...})` adds a new item after the report, showing
  in-place dictionary mutation

### Exercise 5: Stream Wizard (`ex5/ft_data_stream.py`)
Stream random game events using generators instead of building lists
upfront.
- `gen_event()` is an infinite generator (`while True: yield ...`)
  producing `(player, action)` tuples on demand; `next()` is called on
  it 1000 times to print events without ever materializing the full
  sequence
- `consume_event()` takes a finite `list[tuple[str, str]]` and yields
  (and removes, via `list.pop(idx)`) one random element at a time until
  the list is empty, which a plain `for` loop can drive directly
- Both generators are annotated with `typing.Generator[YieldType,
  SendType, ReturnType]`

### Exercise 6: Data Alchemist (`ex6/ft_data_alchemist.py`)
Transform a list of player names using comprehensions only.
- List comprehension: `[name.capitalize() for name in players]` builds a
  normalized copy without a manual loop
- Filtering list comprehension: `[name for name in players if
  name[:1].isupper()]` keeps only already-capitalized entries
- Dict comprehension: `{name: random.randint(0, 1000) for name in
  all_capitalized}` builds a name → score mapping in one line
- A second filtering dict comprehension keeps only entries above the
  computed average score

---

## 🧠 Key Concepts

### Lists
- Ordered, mutable sequences
- Used for score storage and sequential analytics
- Methods: `append()`, `sum()`, `max()`, `min()`

### Tuples
- Ordered, **immutable** sequences
- Perfect for coordinates and fixed data
- Supports unpacking: `x, y, z = (1, 2, 3)`
- Attempting to modify one raises `TypeError`, which is exactly why
  they're a good fit for coordinate data that shouldn't change after
  creation

### Sets
- Unordered, unique elements
- Operations: `union()`, `intersection()`, `difference()`
- Ideal for deduplication and membership testing (`x in my_set` is
  `O(1)`, versus `O(n)` for a list)
- Require hashable elements — see Defense Notes for why

### Dictionaries
- Key-value mappings with `O(1)` average-case lookups
- Methods: `keys()`, `values()`, `items()`, `get()`, `update()`
- Insertion-ordered since Python 3.7, which this module relies on when
  picking a "first-seen" item
- Support nested structures

### Generators
- `yield`-based lazy evaluation
- Constant memory usage regardless of data size — an infinite generator
  like `gen_event()` never allocates more than one item at a time
- Used with `next()`, `for` loops, `iter()`
- Once exhausted (or, for infinite generators, once the underlying list
  is empty), further calls to `next()` raise `StopIteration`

### Comprehensions
- List: `[expr for x in iterable if cond]`
- Dict: `{k: v for x in iterable}`
- Set: `{expr for x in iterable}`
- Same semantics as the equivalent `for` loop with `append()`/item
  assignment, just condensed to one expression — prefer them when the
  loop body is a single transformation/filter, fall back to a real loop
  once there's multi-step logic

---

## 🧪 Testing

Run `python3 main.py` from the module root. It executes every exercise
(including the no-argument and with-argument variants for the scripts
that take CLI input, and a scripted stdin transcript for Exercise 2's
prompts) as a subprocess and prints each one's stdout/stderr under a
labeled separator. A pass looks like: no unhandled tracebacks in any
section, `ValueError`/malformed-input cases printing a friendly error
message instead of crashing, and the final `TEST SUITE COMPLETED` banner
being reached. Individual exercises can also be run and inspected on
their own as shown in Usage above.

---

## ✅ Code Style & Requirements

- Python 3.10+ syntax (`list[int]`, `dict[str, int]`, `tuple[float, ...]`
  built-in generics; `str | None`-style unions where relevant)
- All functions carry type hints, including generator functions annotated
  with `typing.Generator[YieldType, SendType, ReturnType]`
- Lint clean under `flake8 --max-line-length=79`
- No file I/O; only the imports each exercise's subject authorizes
  (`sys`, `math`, `random`, `typing`)
- Exceptions (`ValueError` from bad `int()`/`float()` conversions) are
  caught and reported per-item rather than allowed to crash the script

---

## 🛡️ Defense Notes

- Type checkers can misreport an empty list literal (`numbers = []`) as
  `reportUnknownMemberType` once you start appending typed values — annotate
  it explicitly instead, e.g. `numbers: list[int] = []`.
- **`dict.get(key)` vs `dict[key]`**: `.get()` returns `None` (or a supplied
  default) for a missing key, while `dict[key]` raises `KeyError` — prefer
  `.get()` for optional lookups, direct indexing when the key is guaranteed
  to exist.
- **Why sets require hashable elements**: a set is backed by a hash table,
  so every element needs a stable `__hash__()` (lists and dicts are
  unhashable/mutable and can't be set members; tuples of hashable values
  can).
- **Why tuples for coordinates**: immutability prevents a bug elsewhere in
  the program from silently changing a position after it's been recorded;
  attempting to assign to `coords[0]` raises `TypeError` rather than
  corrupting data.
- **Why generators over lists for the event stream**: `gen_event()` is
  infinite by design — materializing it as a list would never terminate.
  A generator yields one `(player, action)` tuple at a time with constant
  memory, whether you consume 10 events or 10 million.
- **List vs set for achievements**: a list would allow duplicate
  achievements and require an `O(n)` scan for membership tests; a set
  guarantees uniqueness and gives `O(1)` `in` checks, which is also what
  makes `union()`/`intersection()`/`difference()` cheap.
- **Preserving "first-seen" order while rejecting duplicates**: the
  inventory parser checks `if name in inventory` before inserting, relying
  on dicts being insertion-ordered (Python 3.7+) so the reported item list
  reflects the order items were first encountered on the command line.

---

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
