# Cosmic Data Observatory — Discover Pydantic Models & Validation

Python Piscine · Module 09

## 📋 Overview

Master Pydantic v2 data validation through space-themed exercises.
This module covers `BaseModel` field constraints, custom multi-field
validation with `model_validator`, and nested models with
`list[Model]` relationships, while managing simulated cosmic data
streams. Written for Python 3.10+.

## 🎯 Learning Objectives

- Define Pydantic `BaseModel` classes with declarative field
  constraints instead of manual `if` checks.
- Use `Field(ge=…, le=…, min_length=…, max_length=…)` for numeric
  ranges, string lengths, and list sizes.
- Understand Pydantic's automatic type coercion (e.g. ISO date strings
  → `datetime`, plain strings → `str` Enum members).
- Implement multi-field business rules with
  `@model_validator(mode="after")`, replacing the deprecated v1
  `@validator` decorator.
- Compose nested models (`list[Model]` fields) and understand how
  validation errors propagate through the hierarchy.
- Read structured `ValidationError` output via `exc.errors()`,
  including nested error paths like `("crew", 0, "age")`.

## 📁 Project Structure

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

## 🚀 Usage

Execute from the **module root** (activate the venv first):

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Exercise 0 — Space Station Data
python3 ex0/space_station.py      # direct execution
python3 -m ex0.main                # module execution

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

## 📚 Exercises

### ex0 — Space Station Data

**File**: `ex0/space_station.py`
**Goal**: Create a `BaseModel` (`SpaceStation`) that validates incoming
space station telemetry, demonstrating automatic type coercion and
field-level constraints.

- `Field(ge=1, le=20)` on `crew_size` enforces a numeric range
  declaratively.
- `Field(min_length=3, max_length=10)` on `station_id` validates
  string length at construction time.
- `last_maintenance: datetime` accepts a `datetime` object directly;
  Pydantic can coerce ISO strings too, but the demo passes
  `datetime.fromisoformat(…)` to keep Pylance/mypy happy.
- `is_operational: bool = True` and `notes: str | None = None`
  demonstrate defaults and optional fields.
- `main()` builds a valid station, then triggers a `ValidationError`
  by passing `crew_size=25`.

### ex1 — Alien Contact Logs

**File**: `ex1/alien_contact.py`
**Goal**: Use `@model_validator(mode="after")` to enforce custom
multi-field business rules on alien contact reports, after Pydantic's
built-in field validation has already passed.

- `ContactType(str, Enum)` — `radio`, `visual`, `physical`,
  `telepathic` — an unknown string raises `ValidationError` before the
  model validator even runs.
- Business rules enforced in the validator:
  - `contact_id` must start with `"AC"`.
  - `physical` contacts must have `is_verified=True`.
  - `telepathic` contacts require at least 3 witnesses.
  - `signal_strength > 7.0` requires a non-`None` `message_received`.
- `main()` shows a valid radio contact, then triggers the telepathic
  witness rule.

### ex2 — Space Crew Management

**File**: `ex2/space_crew.py`
**Goal**: Compose nested Pydantic models (`CrewMember` inside
`SpaceMission`) and enforce multi-record safety rules via
`@model_validator`, exploring how validation errors propagate through
model hierarchies.

- `Rank(str, Enum)` — `cadet`, `officer`, `lieutenant`, `captain`,
  `commander`.
- `crew: list[CrewMember] = Field(min_length=1, max_length=12)` — list
  size constraints, not string length.
- Mission safety rules enforced in the validator:
  - `mission_id` must start with `"M"`.
  - At least one crew member must hold `commander` or `captain` rank.
  - Missions longer than 365 days require ≥ 50% of crew with 5+ years
    experience.
  - Every crew member must be active (`is_active=True`).
- Pydantic validates each `CrewMember` before the mission validator
  runs; a bad crew member raises `ValidationError` with the nested
  path before mission-level rules are even checked.
- `main()` creates a valid 3-person Mars mission, then triggers the
  missing-senior-officer rule.

## 🧠 Key Concepts

- **`@model_validator(mode="after")`** is used exclusively — the
  deprecated `@validator` decorator from Pydantic v1 is intentionally
  avoided. It receives the fully constructed, already-coerced model
  instance as `self`; always end the function with `return self`
  (returning `None` raises a `TypeError` since the return value
  replaces the model instance).
- `mode="after"` vs `mode="before"`: `after` gives a typed model
  instance with all fields already coerced; `before` gives the raw
  input dict and is better suited for pre-processing raw data ahead of
  field validation.
- **`Field(ge=…, le=…)`** replaces manual range checks for numeric
  fields.
- **`Field(min_length=…, max_length=…)`** works on both `str` *and*
  `list` fields — it validates string length or list size
  respectively. Pydantic v2 uses these names; the v1 aliases
  `min_items`/`max_items` still work but are deprecated.
- **Automatic type coercion**: Pydantic converts compatible types at
  construction time — `"2024-01-15T10:30:00"` → `datetime`, `"radio"`
  → `ContactType.radio`, `"true"` → `True` for a `bool` field, etc.
- **`str` Enum mixin** (`class ContactType(str, Enum)`): inheriting
  from `str` lets Pydantic accept plain strings as input and lets
  Pylance/mypy type `.value` as `str` without casting.
- **Nested models**: a `list[CrewMember]` field validates each element
  against the `CrewMember` schema individually, giving type safety and
  auto-coercion per record — this is preferred over `list[dict]`.
- If two rules fail inside the same `model_validator`, Pydantic v2
  stops at the first `ValueError` raised — only one error message is
  reported per validator call.

## 🧪 Testing

Each exercise's `main()` demonstrates both a valid model construction
and an intentional `ValidationError` (or business-rule violation) to
show the validation working in both directions:

```bash
# Run all exercises at once and inspect stdout
python3 main.py

# Or run individually
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```

There is no separate automated test suite for this module — correctness
is verified by reading the printed valid-model summary and the
expected `ValidationError` message for each exercise, and by running
`mypy`/`flake8` for static/style correctness.

## ✅ Code Style & Requirements

- Python 3.10 or later; `str | None` union syntax used throughout
  instead of `Optional[str]`; `list[CrewMember]` (lowercase builtin
  generic) instead of `List[CrewMember]` from `typing`.
- `from __future__ import annotations` at the top of every module
  enables PEP 563 postponed evaluation of annotations, allowing forward
  references such as `-> AlienContact` inside the class body without
  quoting.
- Full type annotations on every function and method signature; no
  implicit `Any`.
- `model_validator(mode="after")` returns the correct self-type;
  Pylance resolves the return annotation through the postponed
  annotation mechanism without needing `typing.Self` or
  `typing_extensions`.
- `flake8` linting standards — max line length 79 characters,
  `snake_case` naming, proper spacing.
- All Pydantic models use type hints on every field; never use
  deprecated Pydantic v1 decorators (`@validator`, `@root_validator`).

Run a quick type-check (subject requirement: mypy). You can still use
pyright for Pylance validation.

```bash
pip install mypy
python3 -m mypy .

# Optional (Pylance / pyright)
pip install pyright
python3 -m pyright .
```

`pyrightconfig.json` at the module root points to `.venv` so Pylance
resolves the `pydantic` package without import errors. Static type
checkers do not know about Pydantic's runtime coercion, so passing a
string literal to a `datetime` field is flagged by Pylance/mypy even
though Pydantic would accept it at runtime — the fix used throughout
this module is to pass a proper `datetime` object via
`datetime.fromisoformat(…)` instead of a raw string literal.

## 🛡️ Defense Notes

Business rules that live inside validators (not immediately obvious
from the model fields alone):

- A `physical` contact must have `is_verified=True`.
- A `telepathic` contact requires at least 3 independent witnesses to
  be considered valid.
- A `SpaceMission` needs at least one `commander` or `captain` among
  the crew, and missions longer than 365 days require at least half
  the crew to have 5+ years of experience.

**Reading nested Pydantic validation errors**: `exc.errors()` returns a
list of dicts whose `"loc"` key is a tuple describing the exact failure
path through nested models/lists, e.g. `("crew", 0, "age")` means "the
`age` field of the first (`0`) item in the `crew` list." Each dict also
carries `"msg"`, `"type"`, and `"input"` keys.

Common defense-style Q&A:

- **What happens when a `CrewMember` fails validation inside a
  mission?** Pydantic raises `ValidationError` for the crew member
  *before* the mission-level `model_validator` runs — the error's
  `"loc"` already points at the nested member (e.g.
  `("crew", 0, "age")`).
- **Why `mode="after"` instead of `mode="before"`?** `after` hands you
  a fully typed, already-coerced model instance; `before` only gives
  the raw input dict, which is better for pre-processing before field
  validation happens.
- **Why does `ContactType` inherit from both `str` and `Enum`?**
  Inheriting `str` makes each member a string subtype, so Pydantic
  accepts plain strings as input and Pylance types `.value` as `str`.
- **What if two rules fail at once inside one validator?** Pydantic v2
  stops at the first `ValueError` raised; only that one message is
  reported.
- **Why must you `return self`?** In `mode="after"`, the return value
  replaces the model instance; returning `None` raises a `TypeError`.
- **Pydantic v1 vs v2 field constraints**: v2 uses
  `min_length`/`max_length` for both strings and lists; the v1 aliases
  `min_items`/`max_items` still work but are deprecated — prefer the v2
  names in new code.
- **Can you add a new contact type without changing validation logic?**
  Yes — add a new member to `ContactType`. Existing validators operate
  on the enum value; if the new type needs no special rule, nothing
  else changes.
- **Why is `from __future__ import annotations` needed?** It enables
  PEP 563 postponed annotation evaluation, so the return annotation
  `-> AlienContact` inside the `AlienContact` class body doesn't need
  to be a quoted forward reference.

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
