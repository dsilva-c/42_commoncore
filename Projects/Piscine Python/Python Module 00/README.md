# Module 00 - Growing Code
## Python Fundamentals Through Garden Data

### Learning Python basics through agricultural data management

---

## 📋 Overview

This module introduces fundamental Python programming concepts through garden and agriculture-themed exercises: basic syntax, control structures, functions, and data types, applied to managing virtual garden data.

**Python Version**: 3.10+
**Focus**: Python Fundamentals
**Theme**: Garden Data Management

---

## 🎯 Learning Objectives

After completing this module, you should understand:

- Function definitions, print/input operations, and variables
- Type conversion (`int()`) and string formatting with f-strings
- Conditional statements (`if`/`elif`/`else`) and boolean logic
- For loops and the accumulation pattern
- Iteration vs. recursion, including base case and recursive case design
- Type hints/annotations on function signatures
- Writing PEP 8 / flake8-compliant code

---

## 📁 Project Structure

```
Python Module 00/
├── ex0/
│   └── ft_hello_garden.py             # Basic function and output
├── ex1/
│   └── ft_garden_name.py              # Input and fixed output messages
├── ex2/
│   └── ft_plot_area.py                # Input, type conversion, arithmetic
├── ex3/
│   └── ft_harvest_total.py            # Multiple inputs and addition
├── ex4/
│   └── ft_plant_age.py                # Conditional statements (if/else)
├── ex5/
│   └── ft_water_reminder.py           # Boolean logic and conditions
├── ex6/
│   ├── ft_count_harvest_iterative.py  # Iteration with loops
│   └── ft_count_harvest_recursive.py  # Recursion
├── ex7/
│   └── ft_seed_inventory.py           # Type annotations and conditionals
├── main.py                            # Interactive test helper
├── README.md                          # This file
└── en.subject.pdf                     # Original project subject
```

---

## 🚀 Usage

### Run All Tests

```bash
python3 main.py
```

This launches an interactive menu; pick a single exercise number (`0`-`7`) or `a` to run all of them in sequence.

### Run Individual Exercises

```bash
# Exercise 0 - Hello Garden
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"

# Exercise 1 - Garden Name (interactive)
python3 -c "from ex1.ft_garden_name import ft_garden_name; ft_garden_name()"

# Exercise 2 - Plot Area (interactive)
python3 -c "from ex2.ft_plot_area import ft_plot_area; ft_plot_area()"

# Exercise 3 - Harvest Total (interactive)
python3 -c "from ex3.ft_harvest_total import ft_harvest_total; ft_harvest_total()"

# Exercise 4 - Plant Age (interactive)
python3 -c "from ex4.ft_plant_age import ft_plant_age; ft_plant_age()"

# Exercise 5 - Water Reminder (interactive)
python3 -c "from ex5.ft_water_reminder import ft_water_reminder; ft_water_reminder()"

# Exercise 6 - Count Harvest (Iterative)
python3 -c "from ex6.ft_count_harvest_iterative import ft_count_harvest_iterative; ft_count_harvest_iterative()"

# Exercise 6 - Count Harvest (Recursive)
python3 -c "from ex6.ft_count_harvest_recursive import ft_count_harvest_recursive; ft_count_harvest_recursive()"

# Exercise 7 - Seed Inventory
python3 -c "from ex7.ft_seed_inventory import ft_seed_inventory; ft_seed_inventory('tomato', 15, 'packets')"
```

### Check Code Quality

```bash
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/ ex7/ --max-line-length=79
```

---

## 📚 Exercises

### Exercise 0: Hello Garden
**File**: `ex0/ft_hello_garden.py`

Print a fixed welcome message (`Hello, Garden Community!`).

**Concepts**:
- Function definition with `def`
- Print statements
- Function structure

---

### Exercise 1: Garden Name
**File**: `ex1/ft_garden_name.py`

Ask for a garden name and print its status (`Enter garden name: ` → `Garden: <name>` / `Status: Growing well!`).

**Concepts**:
- User input with `input()`
- F-strings for formatting

---

### Exercise 2: Plot Area
**File**: `ex2/ft_plot_area.py`

Calculate the area of a rectangular garden plot from length and width input.

**Concepts**:
- Type conversion with `int()`
- Variables and arithmetic operations
- F-strings for formatting

---

### Exercise 3: Harvest Total
**File**: `ex3/ft_harvest_total.py`

Sum three days of harvest input into a total.

**Concepts**:
- Multiple sequential inputs
- Accumulation pattern
- Return values via `print`

---

### Exercise 4: Plant Age Check
**File**: `ex4/ft_plant_age.py`

Report whether a plant is ready to harvest based on its age in days (threshold: `> 60`).

**Concepts**:
- If/else statements
- Comparison operators

---

### Exercise 5: Water Reminder
**File**: `ex5/ft_water_reminder.py`

Report whether plants need watering based on days since last watering (threshold: `> 2`).

**Concepts**:
- Boolean logic
- Conditional statements

---

### Exercise 6: Count to Harvest
**Files**:
- `ex6/ft_count_harvest_iterative.py`
- `ex6/ft_count_harvest_recursive.py`

Count from 1 to a given number using both iteration and recursion; both must produce identical output (`Day 1` ... `Day n`, then `Harvest time!`).

**Concepts**:
- **Iterative**: `for` loops, `range()`
- **Recursive**: base case, recursive case, private helper function
- Comparing iteration vs. recursion

---

### Exercise 7: Seed Inventory with Type Annotations
**File**: `ex7/ft_seed_inventory.py`

Display seed inventory information, formatted differently depending on the unit (`packets`, `grams`, `area`, or unknown).

**Concepts**:
- Type hints: `def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:`
- String methods (`str.capitalize()`)
- Conditional branching on string values

---

## 🧠 Key Concepts

- **Functions only, no `main` blocks**: every exercise file defines exactly the requested function and nothing else — no `if __name__ == "__main__":` guard. `main.py` is a helper script (kept outside the graded exercises) that imports and drives each function interactively.
- **Iteration vs. recursion (Exercise 6)**: the iterative version uses a `for` loop over `range(1, days + 1)`. The recursive version uses a private nested helper (`count_days`) that carries `current` and `total` as parameters, prints, then calls itself with `current + 1` until `current > total` — the base case that stops the recursion.
- **Type hints (Exercise 7)**: `seed_type: str, quantity: int, unit: str` and a `-> None` return annotation document the expected interface without changing runtime behavior. Pylance/Pyright can then catch a wrong-typed call at edit time instead of at runtime.
- **No error handling by design**: none of the exercises validate input (e.g. non-numeric input to `int()`). The subject leaves behavior on invalid input undefined, so no try/except is added — this is intentional, not an oversight.

### Pylance — Static Type Checker in VS Code

**Pylance** is the default Python language server for VS Code. It performs *static analysis* — it reads source code without running it and reports type errors, missing imports, unknown attributes, and other issues directly in the editor.

<div align="center">

| Benefit | What it catches |
|---------|----------------|
| **Type safety** | Calling a function with the wrong argument type |
| **Undefined names** | Using a variable before assignment |
| **Missing imports** | Referencing a symbol that was never imported |
| **Unreachable code** | Logic that can never execute |
| **Return-type mismatches** | Returning `None` when a `str` is expected |

</div>

Severity levels: 🔴 Error (definite type violation), 🟡 Warning (probable issue), 🔵 Information (style/deprecation hint). Hover over any underlined token in VS Code to see the full message.

Common fix pattern seen throughout this piscine:

```python
# ❌ Pylance: "Expected type arguments for generic class 'dict'"
game_state: dict = {}

# ✅ Fixed: fully parametrised generic
from typing import Any
game_state: dict[str, Any] = {}
```

Strictness is configured in `.vscode/settings.json` via `python.analysis.typeCheckingMode` (`basic` / `standard` / `strict`); this piscine uses **basic** mode throughout. For Module 00 specifically, the only file where Pylance has real type information to check is Exercise 7 (`ft_seed_inventory`), since it's the only function with annotated parameters.

---

## 🧪 Testing

- Run `python3 main.py` and either pick a single exercise number or `a` to run all nine exercise functions in sequence with sample input.
- Each exercise can also be run standalone with the one-liners in [Usage](#-usage) to verify prompts and output match the subject exactly.
- A pass means: the program runs without raising an exception, every prompt/output string matches the subject's wording exactly, and `flake8` reports no errors.

---

## ✅ Code Style & Requirements

- Python 3.10 or higher
- `flake8` for style checking (`pip install flake8`)
- PEP 8 style guide, maximum line length: 79 characters
- Each exercise file contains only the requested function — no `if __name__ == "__main__":` block
- Function and file names match the subject exactly
- Type hints required only in Exercise 7

---

## 🛡️ Defense Notes

- **Why is there no error handling on `int(input(...))`?** The subject leaves invalid-input behavior undefined, so raising on bad input (e.g. `ValueError` from a non-numeric string) is acceptable and expected — don't add unsolicited try/except blocks defending against cases the subject doesn't specify.
- **Why no `if __name__ == "__main__":` in the exercise files?** The subject requires each file to expose only the function itself; the runnable entry point lives in `main.py`, which is a helper and not itself graded.
- **What is recursion, concretely, for Exercise 6?** A function (the nested `count_days` helper) that calls itself with an incremented counter until it hits the base case (`current > total`), at which point it prints `Harvest time!` and returns instead of recursing further — this mirrors the iterative version's `for` loop exactly, which is the point of pairing the two implementations.
- **Exercise 7 unit branching**: the four branches (`packets`, `grams`, `area`, and an else/default) must be checked in that order with `elif`, and the seed name is normalized with `str.capitalize()` regardless of how it was typed in — expect to justify why `capitalize()` and not `.title()` or manual casing (subject examples only ever pass single words).
- **Exact string matching matters**: prompts and output strings (e.g. `Enter garden name: `, `Plant is ready to harvest!`) are graded on exact match with the subject, not just equivalent meaning — trailing spaces, punctuation, and capitalization are significant.

---

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
