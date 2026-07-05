# Module 02 - Garden Guardian
## Data Engineering for Smart Agriculture

### Exception Handling in Python

---

## 📋 Project Overview

This module focuses on exception handling in Python, demonstrating how to build robust data pipelines for agricultural monitoring systems. Through a smart garden theme, you'll learn to handle sensor failures, validate data, and create fault-tolerant monitoring systems.

**Python Version**: 3.10+  
**Focus**: Exception Handling, Error Recovery, Data Validation

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
python3 ex0/ft_first_exception.py
python3 ex1/ft_different_errors.py
python3 ex2/ft_custom_errors.py
python3 ex3/ft_finally_block.py
python3 ex4/ft_raise_errors.py
python3 ex5/ft_garden_management.py
```

### Check Code Quality
```bash
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ main.py --max-line-length=79
```

---

## 📚 Exercises

### Exercise 0: Agricultural Data Validation Pipeline
**File**: `ex0/ft_first_exception.py`

Learn basic exception handling by validating temperature sensor data.

**Key Concepts**:
- Try/except blocks
- ValueError handling
- Input validation

---

### Exercise 1: Different Types of Problems
**File**: `ex1/ft_different_errors.py`

Handle multiple types of built-in exceptions in garden operations.

**Key Concepts**:
- Multiple exception types
- Specific vs. general exception handling
- Catching multiple exceptions

---

### Exercise 2: Making Your Own Error Types
**File**: `ex2/ft_custom_errors.py`

Create custom exception classes for garden-specific errors.

**Key Concepts**:
- Custom exception classes
- Exception inheritance
- Domain-specific errors

---

### Exercise 3: Finally Block - Always Clean Up
**File**: `ex3/ft_finally_block.py`

Use finally blocks to ensure cleanup operations always occur.

**Key Concepts**:
- Try/except/finally structure
- Resource management
- Guaranteed cleanup

---

### Exercise 4: Raising Your Own Errors
**File**: `ex4/ft_raise_errors.py`

Raise exceptions to signal validation failures.

**Key Concepts**:
- Using raise keyword
- Input validation
- Defensive programming

---

### Exercise 5: Garden Management System
**File**: `ex5/ft_garden_management.py`

Integrate all exception handling techniques into a complete system.

**Key Concepts**:
- All previous techniques combined
- Error recovery
- System resilience

---

## ✅ Requirements

- Python 3.10 or higher
- flake8 (for code style checking)

### Install Requirements
```bash
pip install flake8
```

---

## 🎯 Learning Objectives

After completing this module, you will understand:

1. **Exception Handling Basics**
   - try/except/else/finally blocks
   - Catching specific exception types
   - Error propagation

2. **Built-in Exceptions**
   - ValueError, TypeError, ZeroDivisionError
   - FileNotFoundError, KeyError, IndexError
   - When to use each type

3. **Custom Exceptions**
   - Creating custom exception classes
   - Exception inheritance hierarchy
   - Domain-specific error handling

4. **Resource Management**
   - Using finally for cleanup
   - Ensuring resources are released
   - Handling errors gracefully

5. **Defensive Programming**
   - Input validation
   - Raising meaningful errors
   - Building fault-tolerant systems

---

## 🧪 Testing

### Manual Testing
Each exercise can be tested individually by running its Python file.

### Automated Testing
The `main.py` file runs all exercises in sequence and provides a summary.

### Expected Output
All exercises should:
- Run without crashing
- Display appropriate error messages
- Demonstrate error handling
- Complete successfully

---

## 📝 Code Style

All code follows:
- PEP 8 style guide
- flake8 linting standards
- Maximum line length: 79 characters
- Type hints for all functions
- Docstrings for all modules and functions

---

## 🛠️ Troubleshooting

### Common Issues

**Problem**: `ModuleNotFoundError` when running `main.py`  
**Solution**: Ensure you're in the correct directory:
```bash
cd "/path/to/Python Module 02"
python3 main.py
```

**Problem**: Flake8 errors  
**Solution**: Check code style, line length, and unused imports

**Problem**: Import errors in individual exercises  
**Solution**: Run from the module root directory

---

## 📊 Project Statistics

- **Total Exercises**: 6
- **Lines of Code**: ~550 (across all exercises)
- **Functions**: 15+
- **Custom Classes**: 4
- **Exception Types**: 7+ different types

---

## 🌟 Key Features

- ✅ Complete exception handling implementation
- ✅ All exercises with type hints
- ✅ Comprehensive docstrings
- ✅ Flake8 compliant
- ✅ Automated test suite
- ✅ Individual exercise testing
- ✅ Real-world agricultural theme

---

## 📚 Additional Resources

- [Python Official Documentation - Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [PEP 8 - Style Guide](https://pep8.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

## 🛡️ Defense notes

- **Why not bare `except Exception`?** It silently swallows bugs you didn't
  anticipate (e.g. `TypeError`, `KeyboardInterrupt`) alongside the ones you
  meant to handle, making failures harder to diagnose — catch the specific
  exception types you expect.
- **Except block order matters**: blocks are checked top-to-bottom, and the
  first matching type wins — a broader exception (e.g. `Exception`) listed
  before a more specific one (e.g. `ValueError`) will shadow it and the
  specific handler never runs.
- **Proactive validation vs. reactive exceptions**: validate inputs up front
  when a bad value is expected/common (clearer control flow), and reserve
  `try`/`except` for genuinely exceptional, hard-to-predict failures (e.g.
  I/O errors).

---

## 👨‍💻 Author

**Student**: Daniel Cardoso (dsilva-c)  
**Module**: Python Module 02  
**School**: 42  
**Project**: Garden Guardian - Data Engineering for Smart Agriculture

---

## 📄 License

This project is part of the 42 School curriculum.

---

## 🎓 Acknowledgments

Built as part of the 42 Python Piscine, focusing on practical exception handling for data engineering applications.

---

**Happy Coding! 🌱**
