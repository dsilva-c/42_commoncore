# Module 03 - Data Quest
## Mastering Python Collections for Data Engineering

### Python Collections, Generators & Comprehensions

---

## Project Overview

This module focuses on Python's core collection data structures and advanced
data-processing techniques. Through a game analytics theme ("PixelMetrics
3000"), you'll master lists, tuples, sets, dictionaries, generators, and
comprehensions.

**Python Version**: 3.10+
**Focus**: Collections, Generators, Comprehensions

---

## Project Structure

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
├── DEFENSE_GUIDE.md               # Comprehensive defense preparation
├── IMPLEMENTATION_SUMMARY.md      # Implementation notes
├── SUBMISSION_CHECKLIST.md        # Submission checklist
├── README.md                      # This file
└── en.subject.pdf                 # Original project subject
```

---

## Quick Start

### Run All Tests
```bash
python3 main.py
```

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

### Check Code Quality
```bash
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/ main.py \
    --max-line-length=79
```

---

## Exercise Summaries

| # | Name | Data Structure | Key Concept |
|---|------|---------------|-------------|
| 0 | Command Quest | — | `sys.argv`, CLI processing |
| 1 | Score Cruncher | List | Ordered collection, stats |
| 2 | Position Tracker | Tuple | Immutable 3D coords |
| 3 | Achievement Hunter | Set | Unique values, set ops |
| 4 | Inventory Master | Dictionary | Key-value, inventory stats |
| 5 | Stream Wizard | Generator | `yield`, memory efficiency |
| 6 | Data Alchemist | All | Comprehensions |

---

## Key Concepts

### Lists
- Ordered, mutable sequences
- Used for score storage and sequential analytics
- Methods: `append()`, `sum()`, `max()`, `min()`

### Tuples
- Ordered, **immutable** sequences
- Perfect for coordinates and fixed data
- Supports unpacking: `x, y, z = (1, 2, 3)`

### Sets
- Unordered, unique elements
- Operations: `union()`, `intersection()`, `difference()`
- Ideal for deduplication and membership testing

### Dictionaries
- Key-value mappings with O(1) lookups
- Methods: `keys()`, `values()`, `items()`, `get()`, `update()`
- Support nested structures

### Generators
- `yield`-based lazy evaluation
- Constant memory usage regardless of data size
- Used with `next()`, `for` loops, `iter()`

### Comprehensions
- List: `[expr for x in iterable if cond]`
- Dict: `{k: v for x in iterable}`
- Set: `{expr for x in iterable}`
