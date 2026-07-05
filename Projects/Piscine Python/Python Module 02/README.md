# Module 02 - Garden Guardian
## Data Engineering for Smart Agriculture

---

## 📋 Overview

This module focuses on exception handling in Python, using a smart-garden
theme to model data pipelines for agricultural monitoring. Across six
exercises it builds from basic `try`/`except` blocks up to a small
integrated system that validates sensor data, raises and catches custom
errors, and recovers from failures instead of crashing.

**Python Version**: 3.10+
**Focus**: Exception Handling, Error Recovery, Data Validation

---

## 🎯 Learning Objectives

- Understand the `try`/`except`/`else`/`finally` control flow and the order
  in which each block runs.
- Catch specific built-in exceptions (`ValueError`, `TypeError`,
  `ZeroDivisionError`, `FileNotFoundError`, `KeyError`, `AttributeError`)
  instead of relying on a bare `except`.
- Design custom exception classes and build an inheritance hierarchy for
  domain-specific errors.
- Use `finally` to guarantee cleanup regardless of whether an error
  occurred.
- Raise exceptions deliberately to enforce input validation and defensive
  programming.
- Combine all of the above into a single system that keeps running and
  recovers after an error instead of terminating.

---

## 📁 Project Structure

```
Python Module 02/
├── ex0/
│   └── ft_first_exception.py      # Basic exception handling
├── ex1/
│   └── ft_different_errors.py     # Multiple exception types
├── ex2/
│   └── ft_custom_errors.py        # Custom exception classes
├── ex3/
│   └── ft_finally_block.py        # Finally blocks for cleanup
├── ex4/
│   └── ft_raise_errors.py         # Raising custom errors
├── ex5/
│   └── ft_garden_management.py    # Complete system integration
├── main.py                        # Test suite for all exercises
├── README.md                      # This file
└── en.subject.pdf                 # Original project subject
```

---

## 🚀 Usage

### Run all tests
```bash
python3 main.py
```

### Run individual exercises
```bash
python3 ex0/ft_first_exception.py
python3 ex1/ft_different_errors.py
python3 ex2/ft_custom_errors.py
python3 ex3/ft_finally_block.py
python3 ex4/ft_raise_errors.py
python3 ex5/ft_garden_management.py
```

### Check code quality
```bash
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ main.py --max-line-length=79
```

---

## 📚 Exercises

### Exercise 0: Agricultural Data Validation Pipeline
**File**: `ex0/ft_first_exception.py`

Validates temperature sensor data with a basic `try`/`except` block:
`check_temperature("25")` returns `25.0`, while `check_temperature("abc")`
or an out-of-range value (outside 0-40°C) raises `ValueError`.

**Key Concepts**:
- Try/except blocks
- ValueError handling
- Input validation and range checking

---

### Exercise 1: Different Types of Problems
**File**: `ex1/ft_different_errors.py`

Handles multiple built-in exception types in garden operations:
`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`, and
`AttributeError`.

**Key Concepts**:
- Multiple exception types
- Specific vs. general exception handling
- Catching several exceptions in one block: `except (ValueError, ZeroDivisionError)`

---

### Exercise 2: Making Your Own Error Types
**File**: `ex2/ft_custom_errors.py`

Defines a small exception hierarchy for garden-specific errors:
`GardenError` (base) with `PlantError` and `WaterError` as subclasses.
Catching `GardenError` catches both subclasses.

**Key Concepts**:
- Custom exception classes
- Exception inheritance
- Catching by base class to group related errors

---

### Exercise 3: Finally Block - Always Clean Up
**File**: `ex3/ft_finally_block.py`

`water_plants()` opens a "watering system", waters each plant, and uses a
`finally` block to guarantee the system is closed again — even when a
`None` entry in the plant list raises a `ValueError` mid-loop.

**Key Concepts**:
- Try/except/finally structure
- Resource management
- Guaranteed cleanup regardless of success or failure

---

### Exercise 4: Raising Your Own Errors
**File**: `ex4/ft_raise_errors.py`

`check_plant_health()` validates a plant name (non-empty), water level
(1-10) and sunlight hours (2-12), raising `ValueError` with a specific
message whenever a rule is broken.

**Key Concepts**:
- Using the `raise` keyword
- Input validation
- Defensive programming with helpful error messages

---

### Exercise 5: Garden Management System
**File**: `ex5/ft_garden_management.py`

A `GardenManager` class integrates everything: `add_plant()` validates
input, `water_plants()` uses `finally` for cleanup, `check_plant_health()`
raises custom errors, and `refill_water_tank()` demonstrates recovering
from a `WaterError` and continuing operation.

**Key Concepts**:
- All previous techniques combined
- Error recovery
- System resilience

---

## 🧠 Key Concepts

**Exception handling basics** — separating error handling from normal
control flow makes code more readable and lets a program provide detailed
error information instead of crashing outright:

```python
try:
    risky_operation()
except SpecificError as e:
    print(f"Error: {e}")
except AnotherError:
    pass
else:
    print("Success!")   # runs only if no exception occurred
finally:
    cleanup()            # always runs
```

**Built-in exception types** used across this module:

<div align="center">

| Exception | When it occurs |
|-----------|----------------|
| `ValueError` | Right type, invalid value |
| `TypeError` | Wrong type of argument |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | File doesn't exist |
| `KeyError` | Dictionary key not found |
| `IndexError` | List index out of range |
| `AttributeError` | Attribute doesn't exist |

</div>

**Custom exceptions** are worth creating when built-in types aren't
specific enough, when you want self-documenting error names, or when you
want to group related errors via inheritance (e.g. catching `GardenError`
also catches `PlantError` and `WaterError`).

**The finally block** guarantees cleanup — closing files, releasing locks,
closing network connections — regardless of whether the `try` block
succeeded or raised.

**Raising exceptions deliberately** is appropriate when a precondition is
violated or invalid state is detected; pairing `raise` with a specific,
descriptive message (e.g. `"Plant name cannot be empty"`) makes failures
easier to diagnose than a generic message.

---

## 🧪 Testing

Each exercise file can be run individually and prints its own
demonstration output. `main.py` runs all six exercises in sequence and
prints a combined summary. A passing run means every exercise executes
without an uncaught exception, produces the expected validation/error
messages, and `main.py` completes end to end.

---

## ✅ Code Style & Requirements

- Python 3.10 or higher
- flake8 for style checking (`pip install flake8`), max line length 79
- Type hints on all functions
- Docstrings on all modules and functions
- PEP 8 compliant

---

## 🛡️ Defense Notes

- **Why not bare `except Exception`?** It silently swallows bugs you
  didn't anticipate (e.g. `TypeError`, `KeyboardInterrupt`) alongside the
  ones you meant to handle, making failures harder to diagnose — catch the
  specific exception types you expect.
- **Except block order matters**: blocks are checked top-to-bottom, and
  the first matching type wins — a broader exception (e.g. `Exception`)
  listed before a more specific one (e.g. `ValueError`) will shadow it and
  the specific handler never runs.
- **Proactive validation vs. reactive exceptions**: validate inputs up
  front when a bad value is expected/common (clearer control flow), and
  reserve `try`/`except` for genuinely exceptional, hard-to-predict
  failures (e.g. I/O errors).
- **Catching vs. propagating vs. re-raising**: catching handles the error
  at the current level; propagating lets it bubble up uncaught; re-raising
  (`raise` with no argument inside an `except`) lets you log or react to an
  error and then still pass it up the call stack.
- **Keep `try` blocks small.** A large `try` block makes it unclear which
  line actually failed, and can accidentally catch an exception raised by
  unrelated code further down, hiding real bugs.
- **`ValueError` vs. a custom exception**: use `ValueError` for a generic
  invalid value; reach for a custom exception (like `WaterError`) when the
  failure belongs to your program's domain and you want clearer semantics
  or the ability to catch a whole family of related errors at once via a
  shared base class.
- **What `finally` doesn't survive**: it runs after normal completion,
  after a caught exception, and after an uncaught one propagates out — the
  only ways to skip it are an interpreter crash, `os._exit()`, or the
  process losing power.

---

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
