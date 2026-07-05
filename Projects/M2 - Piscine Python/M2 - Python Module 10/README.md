# FuncMage Chronicles — Master the Ancient Arts of Functional Programming

Python Piscine · Module 10

## Overview

Explore functional programming through five themed exercises.  Master
anonymous functions, higher-order functions, closures, `functools`, and
decorators — the powerful tools that make Python code elegant and reusable.

| Exercise | Theme | Key Concepts |
|----------|-------|-------------|
| ex0 | Lambda Sanctum | `lambda`, `map`, `filter`, `sorted` |
| ex1 | Higher Realm | higher-order functions, first-class functions |
| ex2 | Memory Depths | closures, lexical scoping, `nonlocal` |
| ex3 | Ancient Library | `functools.reduce`, `partial`, `lru_cache`, `singledispatch` |
| ex4 | Master's Tower | decorators, `functools.wraps`, `@staticmethod` |

## Project structure

```
.
├── __init__.py
├── main.py
├── pyrightconfig.json
├── requirements.txt
├── tools/
│   └── data_generator.py
├── ex0/
│   ├── __init__.py
│   ├── lambda_spells.py
│   ├── main.py
│   └── README.md
├── ex1/
│   ├── __init__.py
│   ├── higher_magic.py
│   ├── main.py
│   └── README.md
├── ex2/
│   ├── __init__.py
│   ├── scope_mysteries.py
│   ├── main.py
│   └── README.md
├── ex3/
│   ├── __init__.py
│   ├── functools_artifacts.py
│   ├── main.py
│   └── README.md
└── ex4/
    ├── __init__.py
    ├── decorator_mastery.py
    ├── main.py
    └── README.md
```

## Running exercises

Execute from the **module root** (no virtual environment needed — only
standard library modules are used):

```bash
# All exercises at once
python3 main.py

# Individual exercises
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py

# Module-style execution
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main

# Data generator helper
python3 tools/data_generator.py
```

## Type checking with Pylance

Type annotations follow PEP 484/526 and are verified with **Pylance**
(VS Code's Python language server, powered by Pyright).  The
[pyrightconfig.json](pyrightconfig.json) targets Python 3.10 so that
built-in generic aliases (`list[int]`, `dict[str, Any]`, `tuple[...]`)
are available without importing `from __future__ import annotations`.

When using `Callable` as a type hint, use `collections.abc.Callable`.
`Any` still comes from `typing`. The lowercase `callable` built-in is
not a type hint.

## Authorized imports

| Module | Purpose |
|--------|---------|
| `functools` | `reduce`, `partial`, `lru_cache`, `singledispatch`, `wraps` |
| `collections.abc` | `Callable` type hints |
| `typing` | `Any` type hints |
| `operator` | `add`, `mul` for functional operations |
| `itertools` | advanced iteration patterns |
| `time` | timing in the `spell_timer` decorator |

No external packages (`pip install`) are required.
