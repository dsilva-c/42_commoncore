# Module 00 - Growing Code
## Python Fundamentals Through Garden Data

### Learning Python basics through agricultural data management

---

## 📋 Project Overview

This module introduces fundamental Python programming concepts through garden and agriculture-themed exercises. You'll learn basic syntax, control structures, functions, and data types while managing virtual garden data.

**Python Version**: 3.10+  
**Focus**: Python Fundamentals  
**Theme**: Garden Data Management

---

## 📁 Project Structure

```
Python Module 00/
├── ex0/
│   └── ft_hello_garden.py         # Basic function and output
├── ex1/
│   └── ft_garden_name.py          # Input and fixed output messages
├── ex2/
│   └── ft_plot_area.py            # Input, type conversion, arithmetic
├── ex3/
│   └── ft_harvest_total.py        # Multiple inputs and addition
├── ex4/
│   └── ft_plant_age.py            # Conditional statements (if/else)
├── ex5/
│   └── ft_water_reminder.py       # Boolean logic and conditions
├── ex6/
│   ├── ft_count_harvest_iterative.py  # Iteration with loops
│   └── ft_count_harvest_recursive.py  # Recursion
├── ex7/
│   └── ft_seed_inventory.py       # Type annotations and lists
├── main.py                         # Test suite for all exercises
├── README.md                      # This file
└── en.subject.pdf                 # Original project subject
```

---

## 🚀 Quick Start

### Run All Tests
```bash
python3 main.py
```

### Run Individual Exercises
```bash
# Exercise 0 - Hello Garden
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"

# Exercise 1 - Plot Area (interactive)
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

Learn basic function definition and output.

**Concepts**:
- Function definition with `def`
- Print statements
- Function structure

---

### Exercise 1: Garden Name
**File**: `ex1/ft_garden_name.py`

Calculate garden plot area from user input.

**Concepts**:
- User input with `input()`
- Type conversion with `int()`
- Variables
- Arithmetic operations
- F-strings for formatting

---

### Exercise 2: Plot Area Calculator
**File**: `ex2/ft_plot_area.py`

Sum up harvest quantities from a list.

**Concepts**:
- Lists
- For loops
- Accumulation pattern
- Return values

---

### Exercise 3: Harvest Total
**File**: `ex3/ft_harvest_total.py`

Categorize plants by age using conditional statements.

**Concepts**:
- If/elif/else statements
- Conditional logic
- Comparison operators

---

### Exercise 4: Plant Age Check
**File**: `ex4/ft_plant_age.py`

Determine if plants need watering based on conditions.

**Concepts**:
- Boolean logic
- Multiple conditions
- Logical operators (and, or)

---

### Exercise 5: Water Reminder
**File**: `ex5/ft_water_reminder.py`

Determine if plants need watering based on days since last watering.

**Concepts**:
- Boolean logic
- Conditional statements

---

### Exercise 6: Count to Harvest
**Files**:
- `ex6/ft_count_harvest_iterative.py`
- `ex6/ft_count_harvest_recursive.py`

Count from 1 to a given number using both iteration and recursion.

**Concepts**:
- **Iterative**: For loops, `range()`
- **Recursive**: Base case, recursive case, helper functions
- Comparing iteration vs. recursion

---

### Exercise 7: Seed Inventory with Type Annotations
**File**: `ex7/ft_seed_inventory.py`

Display seed inventory with type annotations.

**Concepts**:
- Type hints
- String methods
- Conditional logic

---

## ✅ Requirements

- Python 3.10 or higher
- flake8 (for code style checking)

### Install Requirements
```bash
pip install flake8
```

---

## 🔍 Pylance — Static Type Checker in VS Code

**Pylance** is the default Python language server for VS Code. It performs
*static analysis* — it reads your source code without running it and reports
type errors, missing imports, unknown attributes, and other issues directly
in the editor as you type.

### Why it matters across the whole piscine

| Benefit | What it catches |
|---------|----------------|
| **Type safety** | Calling a function with the wrong argument type |
| **Undefined names** | Using a variable before assignment |
| **Missing imports** | Referencing a symbol that was never imported |
| **Unreachable code** | Logic that can never execute |
| **Return-type mismatches** | Returning `None` when a `str` is expected |

### How to read Pylance errors

Pylance uses three severity levels:

- 🔴 **Error** — definite type violation; code may crash at runtime
- 🟡 **Warning** — probable issue; worth fixing
- 🔵 **Information** — style or deprecation hint

Hover over any underlined token in VS Code to see the full Pylance message.

### Common fixes seen throughout this piscine

```python
# ❌ Pylance: "Expected type arguments for generic class 'dict'"
game_state: dict = {}

# ✅ Fixed: fully parametrised generic
from typing import Any
game_state: dict[str, Any] = {}

# ❌ Pylance: "Unnecessary isinstance call; 'int' is always an instance of 'int'"
def f(x: int) -> None:
    if isinstance(x, int):   # x is already declared int — redundant
        ...

# ✅ Fixed: trust the type annotation
def f(x: int) -> None:
    if x > 0:
        ...
```

### Pylance strictness levels

You can raise the strictness in `.vscode/settings.json`:

```json
{
  "python.analysis.typeCheckingMode": "basic"   // default
  // or "standard" / "strict" for progressively more checks
}
```

Throughout this piscine, **basic** mode is used. Each module's `README.md`
contains a _Pylance notes_ section describing which specific warnings are
relevant to that module's patterns.

---

## 🎯 Learning Objectives

After completing this module, you will understand:

1. **Basic Python Syntax**
   - Function definitions
   - Variables and data types
   - Print and input operations

2. **Control Structures**
   - Conditional statements (if/elif/else)
   - For loops
   - Boolean logic

3. **Data Structures**
   - Lists
   - Dictionaries
   - String manipulation

4. **Programming Concepts**
   - Iteration
   - Recursion
   - Type hints
   - Code organization

5. **Best Practices**
   - PEP 8 style guidelines
   - Function documentation
   - Code readability

---

## 🧪 Testing

### Manual Testing
Each exercise can be tested individually using the commands in the Quick Start section.

### Automated Testing
The `main.py` file runs all exercises and provides output for verification.

### Expected Behavior
All exercises should:
- Run without errors
- Produce correct output
- Pass flake8 linting
- Follow Python best practices

---

## 📝 Code Style

All code follows:
- PEP 8 style guide
- flake8 linting standards
- Maximum line length: 79 characters
- Clear, descriptive function names
- Proper spacing and indentation

---

## 🛠️ Troubleshooting

### Common Issues

**Problem**: `ModuleNotFoundError` when running exercises  
**Solution**: Ensure you're in the module root directory

**Problem**: Flake8 errors  
**Solution**: Check line length, spacing, and naming conventions

**Problem**: Exercise doesn't run  
**Solution**: Verify the exact import statement and function name

---

## 📊 Project Statistics

- **Total Exercises**: 8
- **Exercise Files**: 9 (Exercise 5 has 2 files)
- **Concepts Covered**: 15+
- **Lines of Code**: ~200 (across all exercises)

---

## 🌟 Key Features

- ✅ Complete Python fundamentals implementation
- ✅ Agricultural/garden theme throughout
- ✅ Both iterative and recursive solutions (Exercise 5)
- ✅ Type hints demonstration (Exercise 7)
- ✅ Flake8 compliant
- ✅ Comprehensive documentation
- ✅ Test suite included

---

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 - Style Guide](https://pep8.org/)
- [Python For Beginners](https://www.python.org/about/gettingstarted/)

---

## 👨‍💻 Author

**Student**: Daniel Cardoso (dsilva-c)  
**Module**: Python Module 00  
**School**: 42  
**Project**: Growing Code - Python Fundamentals

---

## 📄 License

This project is part of the 42 School curriculum.

---

## 🎓 Acknowledgments

Built as part of the 42 Python Piscine, introducing fundamental programming concepts through practical agricultural data management examples.

---

**Happy Coding! 🌱**
