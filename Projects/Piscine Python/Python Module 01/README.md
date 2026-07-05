# Module 01 - CodeCultivation
## Object-Oriented Garden Systems

### Learning Object-Oriented Programming through garden management

---

## 📋 Project Overview

This module introduces Object-Oriented Programming (OOP) concepts through garden management system exercises. You'll learn classes, objects, inheritance, encapsulation, and advanced OOP patterns while building a comprehensive garden monitoring system.

**Python Version**: 3.10+  
**Focus**: Object-Oriented Programming (OOP)  
**Theme**: Smart Garden Management Systems

---

## 📁 Project Structure

```
Python Module 01/
├── ex0/
│   └── ft_garden_intro.py         # Entry point, main function
├── ex1/
│   └── ft_garden_data.py          # Basic class structure
├── ex2/
│   └── ft_plant_growth.py         # Instance methods and attributes
├── ex3/
│   └── ft_plant_factory.py        # Inheritance and super()
├── ex4/
│   └── ft_garden_security.py      # Encapsulation, private attributes
├── ex5/
│   └── ft_plant_types.py          # Multiple inheritance
├── ex6/
│   └── ft_garden_analytics.py     # Nested classes, decorators
├── main.py                         # Test suite for all exercises
├── DEFENSE_GUIDE.md               # Comprehensive defense preparation
├── README.md                      # This file
├── SUBMISSION_CHECKLIST.md        # Pre-submission verification
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
# Exercise 0 - Garden Intro (Entry Point)
python3 ex0/ft_garden_intro.py

# Exercise 1 - Garden Data (Basic Class)
python3 ex1/ft_garden_data.py

# Exercise 2 - Plant Growth (Instance Methods)
python3 ex2/ft_plant_growth.py

# Exercise 3 - Plant Factory (Inheritance)
python3 ex3/ft_plant_factory.py

# Exercise 4 - Garden Security (Encapsulation)
python3 ex4/ft_garden_security.py

# Exercise 5 - Plant Types (Multiple Inheritance)
python3 ex5/ft_plant_types.py

# Exercise 6 - Garden Analytics (Nested Classes)
python3 ex6/ft_garden_analytics.py
```

### Check Code Quality
```bash
python3 -m flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/ --max-line-length=79
```

---

## 📚 Exercises

### Exercise 0: Garden Intro - Entry Point
**File**: `ex0/ft_garden_intro.py`

Learn program execution and the `if __name__ == "__main__"` pattern.

**Concepts**:
- Entry point
- `if __name__ == "__main__"`
- `main()` function
- Type hints
- Module execution vs. import

---

### Exercise 1: Garden Data Organizer
**File**: `ex1/ft_garden_data.py`

Create a basic class structure for organizing garden data.

**Concepts**:
- Class definition
- `__init__` constructor
- Instance attributes
- Print method
- Basic class structure

---

### Exercise 2: Plant Growth Tracker
**File**: `ex2/ft_plant_growth.py`

Implement instance methods and modify object state.

**Concepts**:
- Instance methods
- `self` parameter
- Modifying attributes
- Method chaining (optional)
- Object state management

---

### Exercise 3: Plant Factory
**File**: `ex3/ft_plant_factory.py`

Use inheritance to create specialized plant types.

**Concepts**:
- Class inheritance
- `super()` function
- Method overriding
- Parent-child relationships
- Extending base classes

---

### Exercise 4: Garden Security System
**File**: `ex4/ft_garden_security.py`

Implement encapsulation with private attributes.

**Concepts**:
- Private attributes (`__attribute`)
- Getter methods
- Setter methods
- Encapsulation
- Data protection

---

### Exercise 5: Plant Type Classifier
**File**: `ex5/ft_plant_types.py`

Demonstrate multiple inheritance.

**Concepts**:
- Multiple inheritance
- Method Resolution Order (MRO)
- Diamond problem
- Mixin classes
- Complex inheritance hierarchies

---

### Exercise 6: Garden Analytics Dashboard
**File**: `ex6/ft_garden_analytics.py`

Implement nested classes and decorators.

**Concepts**:
- Nested classes
- `@staticmethod` decorator
- `@classmethod` decorator
- Class attributes vs. instance attributes
- Advanced OOP patterns

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

1. **OOP Fundamentals**
   - Classes and objects
   - Instance and class attributes
   - Methods (`__init__`, instance methods)
   - `self` parameter

2. **Inheritance**
   - Single inheritance
   - Multiple inheritance
   - `super()` function
   - Method overriding
   - Method Resolution Order (MRO)

3. **Encapsulation**
   - Private attributes (`__name`)
   - Getters and setters
   - Data hiding
   - Access control

4. **Advanced OOP**
   - Nested classes
   - `@staticmethod` decorator
   - `@classmethod` decorator
   - Class vs. instance attributes
   - Design patterns

5. **Best Practices**
   - Type hints in OOP
   - Clean class design
   - Separation of concerns
   - Code organization

---

## 📖 Documentation

For detailed information about each exercise, concepts, and defense preparation, see:

**[DEFENSE_GUIDE.md](DEFENSE_GUIDE.md)** - Comprehensive guide including:
- Detailed exercise explanations with code examples
- Expected defense questions and answers
- OOP concepts explained clearly
- Common mistakes and how to avoid them
- Tips for success in evaluation

**[SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)** - Pre-submission verification:
- File structure verification
- Code quality checks
- Functionality tests
- OOP requirements checklist
- Git submission steps

---

## 🧪 Testing

### Manual Testing
Each exercise can be run directly as they all include test code in their main blocks.

### Automated Testing
The `main.py` file runs all exercises sequentially and shows their output.

### Expected Behavior
All exercises should:
- Run without errors
- Demonstrate proper OOP concepts
- Pass flake8 linting
- Follow Python best practices
- Show correct output

---

## 📝 Code Style

All code follows:
- PEP 8 style guide
- flake8 linting standards
- Maximum line length: 79 characters
- Type hints throughout
- Clear class and method names
- Proper docstrings

---

## 🛠️ Troubleshooting

### Common Issues

**Problem**: `NameError: name 'ClassName' is not defined`  
**Solution**: Make sure class is defined before trying to use it

**Problem**: `AttributeError: object has no attribute`  
**Solution**: Verify attribute is initialized in `__init__`

**Problem**: Private attribute not accessible  
**Solution**: Use getter method or name mangling (`_ClassName__attribute`)

**Problem**: Multiple inheritance confusion  
**Solution**: Use `ClassName.__mro__` to see Method Resolution Order

---

## 📊 Project Statistics

- **Total Exercises**: 7
- **Classes Implemented**: 15+
- **Concepts Covered**: 20+
- **Lines of Code**: ~400 (across all exercises)
- **OOP Patterns**: Entry point, inheritance, encapsulation, decorators

---

## 🌟 Key Features

- ✅ Complete OOP implementation
- ✅ Progressive complexity (basics to advanced)
- ✅ Real-world garden management theme
- ✅ All OOP pillars demonstrated (encapsulation, inheritance, polymorphism)
- ✅ Advanced patterns (nested classes, decorators)
- ✅ Flake8 compliant
- ✅ Comprehensive documentation
- ✅ Test suite included

---

## 📚 Additional Resources

- [Python Official Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
- [PEP 8 - Style Guide](https://pep8.org/)
- [Real Python - OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

## 🎓 OOP Concepts Covered

| Concept | Exercise | Description |
|---------|----------|-------------|
| Entry Point | 0 | `if __name__ == "__main__"` pattern |
| Basic Classes | 1 | Class definition, `__init__`, attributes |
| Instance Methods | 2 | Methods, `self`, state modification |
| Inheritance | 3 | Parent-child, `super()`, overriding |
| Encapsulation | 4 | Private attributes, getters/setters |
| Multiple Inheritance | 5 | Multiple parents, MRO |
| Nested Classes | 6 | Classes within classes |
| Decorators | 6 | `@staticmethod`, `@classmethod` |

---

## 🛡️ Defense notes

- **Name mangling**: a double-underscore attribute like `self.__name` is
  rewritten by Python to `self._ClassName__name` (e.g. `_SecurePlant__name`),
  not made truly private — it's a naming convention to avoid subclass
  collisions, not access control.
- **Forward references**: annotating a method with a type that isn't defined
  yet (e.g. a method on `GardenManager` returning `list[GardenManager]`)
  requires `from __future__ import annotations` on Python < 3.11.
- **MRO (Method Resolution Order)**: with multiple inheritance, Python
  resolves attribute/method lookup left-to-right, depth-first, per class
  base order — check it with `ClassName.__mro__` when overriding behaves
  unexpectedly.
- **Common pitfalls**: forgetting to call `super().__init__()` in a
  subclass (parent state never initializes), omitting `->` return type
  hints, and reaching into another object's private attributes directly
  instead of going through its public interface.

---

## 👨‍💻 Author

**Student**: Daniel Cardoso (dsilva-c)  
**Module**: Python Module 01  
**School**: 42  
**Project**: CodeCultivation - Object-Oriented Garden Systems

---

## 📄 License

This project is part of the 42 School curriculum.

---

## 🎓 Acknowledgments

Built as part of the 42 Python Piscine, introducing Object-Oriented Programming concepts through practical garden management system examples.

---

**Happy Coding! 🌱**
