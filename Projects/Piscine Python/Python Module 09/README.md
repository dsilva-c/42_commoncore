# Cosmic Data Observatory — Discover Pydantic Models & Validation

Python Piscine · Module 09

## Overview

Master Pydantic data validation through space-themed exercises.  Learn
to create robust models, implement custom validation, and handle nested
structures while managing cosmic data streams.

| Exercise | Focus | Key Tools |
|----------|-------|-----------|
| ex0 | Basic model + field validation | `BaseModel`, `Field` |
| ex1 | Custom multi-field rules | `model_validator`, `Enum` |
| ex2 | Nested models & relationships | `list[Model]`, complex validators |

## Project structure

```
.
├── __init__.py
├── main.py
├── requirements.txt
├── ex0/
│   ├── __init__.py
│   ├── space_station.py
│   ├── main.py
│   └── README.md
├── ex1/
│   ├── __init__.py
│   ├── alien_contact.py
│   ├── main.py
│   └── README.md
└── ex2/
    ├── __init__.py
    ├── space_crew.py
    ├── main.py
    └── README.md
```

## Running exercises

Execute from the **module root** (activate the venv first):

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Exercise 0 — Space Station Data
python3 ex0/space_station.py      # direct execution
python3 -m ex0.main               # module execution

# Exercise 1 — Alien Contact Logs
python3 ex1/alien_contact.py
python3 -m ex1.main

# Exercise 2 — Space Crew Management
python3 ex2/space_crew.py
python3 -m ex2.main

# Run all exercises at once
python3 main.py
python3 -m main
```

## Pylance / static analysis

All source files are fully compliant with **Pylance strict-mode**
expectations:

- **`from __future__ import annotations`** at the top of every module
  enables PEP 563 postponed evaluation of annotations, allowing forward
  references such as `-> AlienContact` inside the class body without
  quoting.
- **Full type annotations** on every function and method signature
  (`-> None`, `-> AlienContact`, `-> SpaceMission`, etc.).
- **`str | None`** union syntax (Python ≥ 3.10 short form) is used
  instead of `Optional[str]` throughout.
- **`list[CrewMember]`** (lowercase built-in generic) replaces
  `List[CrewMember]` to avoid importing `List` from `typing`.
- **`model_validator(mode="after")`** returns the correct self-type;
  Pylance resolves the return annotation through the postponed
  annotation mechanism without needing `typing.Self` or `typing_extensions`.
- **Enum base class `str`** (`class ContactType(str, Enum)`) lets
  Pylance correctly type `.value` as `str` and allows Pydantic to
  accept plain string inputs.
- No implicit `Any` — all variables are either inferred or explicitly
  annotated.

Run a quick type-check (subject requirement: mypy). You can still use
pyright for Pylance validation.

```bash
pip install mypy
python3 -m mypy .

# Optional (Pylance / pyright)
pip install pyright
python3 -m pyright .
```

## Pydantic v2 notes

- Use `@model_validator(mode="after")` — the deprecated `@validator`
  decorator from Pydantic v1 is intentionally avoided.
- `Field(ge=…, le=…)` replaces manual range checks.
- `Field(min_length=…, max_length=…)` works on both `str` *and*
  `list` fields (validates string length vs. list size respectively).
- Pydantic automatically coerces `"2024-01-15T10:30:00"` → `datetime`,
  `"radio"` → `ContactType.radio`, etc.

## General requirements

- Python 3.10 or later.
- `flake8` linting standards — max line length 79 characters,
  `snake_case` naming, proper spacing.
- All Pydantic models use type hints on every field.
- Never use deprecated Pydantic v1 decorators (`@validator`).

---

## 🛡️ Defense notes

Business rules that live in validators (not immediately obvious from the
model fields alone):

- A `physical` contact must have `is_verified=True`.
- A `telepathic` contact requires at least 3 independent witnesses to be
  considered valid.

**Reading nested Pydantic validation errors**: `exc.errors()` returns a list
of dicts whose `"loc"` is a tuple describing the exact failure path through
nested models/lists, e.g. `("crew", 0, "age")` means "the `age` field of the
first (`0`) item in the `crew` list."

**Pydantic v1 vs v2 field constraints**: v2 uses `min_length`/`max_length`
for both strings and lists; the v1 aliases `min_items`/`max_items` still
work but are deprecated — prefer the v2 names in new code.
