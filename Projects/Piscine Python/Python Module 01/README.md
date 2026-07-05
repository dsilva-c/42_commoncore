# Module 01 - CodeCultivation
## Object-Oriented Garden Systems

### Learning Object-Oriented Programming through garden management

---

## 📋 Overview

This module introduces Object-Oriented Programming (OOP) through a series of garden-management exercises, progressing from a plain script entry point to multiple inheritance and nested classes with decorators. Each exercise builds on the previous one's concepts, using a "Plant" class hierarchy as the running example.

**Python Version**: 3.10+
**Focus**: Object-Oriented Programming (OOP)
**Theme**: Smart Garden Management Systems

---

## 🎯 Learning Objectives

After completing this module, you should understand:

- Classes, objects, and the difference between a blueprint and an instance
- Instance attributes vs. class attributes, and how `__init__` initializes state
- Instance methods and the role of `self`
- Single inheritance, `super().__init__()`, and method overriding
- Encapsulation via name-mangled private attributes (`__attr`) and getter/setter methods
- Multiple inheritance, the diamond problem, and Method Resolution Order (MRO)
- Nested classes, `@staticmethod`, `@classmethod`, and class vs. instance attributes
- Writing type-hinted, PEP 8-compliant OOP code

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
│   └── ft_plant_factory.py        # Constructor and inheritance
├── ex4/
│   └── ft_garden_security.py      # Encapsulation, private attributes
├── ex5/
│   └── ft_plant_types.py          # Multiple inheritance
├── ex6/
│   └── ft_garden_analytics.py     # Nested classes, decorators
├── main.py                        # Test suite for all exercises
└── en.subject.pdf                 # Original project subject
```

---

## 🚀 Usage

### Run All Tests
```bash
python3 main.py
```

### Run Individual Exercises
```bash
python3 ex0/ft_garden_intro.py      # Garden Intro (entry point)
python3 ex1/ft_garden_data.py       # Garden Data (basic class)
python3 ex2/ft_plant_growth.py      # Plant Growth (instance methods)
python3 ex3/ft_plant_factory.py     # Plant Factory (constructor/inheritance)
python3 ex4/ft_garden_security.py   # Garden Security (encapsulation)
python3 ex5/ft_plant_types.py       # Plant Types (multiple inheritance)
python3 ex6/ft_garden_analytics.py  # Garden Analytics (nested classes)
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

### Exercise 1: Garden Data Organizer
**File**: `ex1/ft_garden_data.py`

Define a basic `Plant` class for organizing garden data.

**Concepts**:
- Class definition
- `__init__` constructor
- Instance attributes
- Print/display method
- Basic class structure

### Exercise 2: Plant Growth Tracker
**File**: `ex2/ft_plant_growth.py`

Implement instance methods that modify a `Plant` object's state.

**Concepts**:
- Instance methods
- `self` parameter
- Modifying attributes
- Object state management

### Exercise 3: Plant Factory
**File**: `ex3/ft_plant_factory.py`

Build a `Plant` base class with a full constructor, used as the foundation the later exercises extend.

**Concepts**:
- `__init__` constructor and parameters
- Instance attribute initialization
- Object creation via a class used as a factory
- Parent-child relationships (sets up Exercise 5/6)

### Exercise 4: Garden Security System
**File**: `ex4/ft_garden_security.py`

Implement encapsulation in `SecurePlant` with private attributes.

**Concepts**:
- Private attributes (`__attribute`)
- Getter methods
- Setter methods with validation
- Encapsulation / data protection

### Exercise 5: Plant Type Classifier
**File**: `ex5/ft_plant_types.py`

Derive `Flower`, `Tree`, and `Vegetable` from a common `Plant` base class.

**Concepts**:
- Single inheritance from a shared base
- `super()` function
- Method overriding
- Extending base classes with specialized attributes/methods

### Exercise 6: Garden Analytics Dashboard
**File**: `ex6/ft_garden_analytics.py`

Implement a multi-level hierarchy (`Plant` → `FloweringPlant` → `PrizeFlower`) plus a `GardenManager` with a nested `GardenStats` class.

**Concepts**:
- Nested classes
- `@staticmethod` decorator
- `@classmethod` decorator
- Class attributes vs. instance attributes
- Multi-level inheritance chains

---

## 🧠 Key Concepts

| Concept | Exercise | Description |
|---------|----------|-------------|
| Entry Point | 0 | `if __name__ == "__main__"` pattern |
| Basic Classes | 1 | Class definition, `__init__`, attributes |
| Instance Methods | 2 | Methods, `self`, state modification |
| Constructor/Inheritance | 3 | `__init__`, parameters, base-class design |
| Encapsulation | 4 | Private attributes, getters/setters |
| Inheritance | 5 | `Flower`/`Tree`/`Vegetable` extending `Plant`, `super()` |
| Nested Classes & Decorators | 6 | Classes within classes, `@staticmethod`, `@classmethod` |

**Name mangling**: a double-underscore attribute like `self.__name` is rewritten by Python to `self._ClassName__name` (e.g. `_SecurePlant__name`). It is not truly private — it's a naming convention that avoids accidental collisions in subclasses, not real access control. It can still be reached from outside via the mangled name, which is why getters/setters (Exercise 4) are the intended interface.

**Forward references**: annotating a method with a type that isn't fully defined yet (e.g. a method on `GardenManager` returning `list[GardenManager]` in Exercise 6) requires `from __future__ import annotations` on Python versions before 3.11, since the annotation is otherwise evaluated immediately at class-definition time.

**MRO (Method Resolution Order)**: with multiple/multi-level inheritance, Python resolves attribute and method lookup left-to-right, depth-first, following the base-class order given in the `class` statement. Inspect it with `ClassName.__mro__` whenever overriding or `super()` chains behave unexpectedly.

**Instance vs. class vs. static methods**:

| Type | First Parameter | Access To | Decorator | Use Case |
|------|----------------|-----------|-----------|----------|
| Instance | `self` | Instance data | none | Operate on this object's state |
| Class | `cls` | Class data | `@classmethod` | Factory methods, class-variable access |
| Static | none | Neither | `@staticmethod` | Utility logic that belongs in the class namespace |

---

## 🧪 Testing

Run `python3 main.py` to execute all seven exercises sequentially and inspect their combined output; each exercise can also be run individually as shown under Usage, since every file includes its own `if __name__ == "__main__"` test block. A run is considered passing when:

- Every exercise executes without raising an exception
- Output matches the behavior described in the subject (object creation, growth/state changes, inheritance/encapsulation demonstrations, analytics report)
- `flake8` reports no errors on any of the `ex0`-`ex6` files

---

## ✅ Code Style & Requirements

- Python 3.10 or higher
- `flake8` for linting (install with `pip install flake8`)
- PEP 8 style guide, 79-character line length limit
- Type hints on all function/method signatures, including `-> None` where appropriate
- Docstrings on classes and non-trivial methods
- `PascalCase` for class names, `snake_case` for functions and methods

---

## 🛡️ Defense Notes

- **Name mangling is not privacy.** `self.__name` becomes `self._ClassName__name` internally — it prevents accidental name clashes in subclasses, not deliberate external access. Be ready to explain why Python has no true private attributes and why getters/setters (Exercise 4) are the convention instead.
- **`super().__init__()` is not automatic.** A subclass that defines its own `__init__` must explicitly call the parent's, or the parent's attributes never get set. This is the single most common bug across Exercises 3, 5, and 6.
- **`self` is passed implicitly.** Calling `rose.grow()` is equivalent to `Plant.grow(rose)` — Python inserts the instance as the first argument automatically; forgetting `self` as the first parameter in a method definition is a classic mistake.
- **MRO resolves multi-level and multiple inheritance**, not just direct parent-child pairs. When behavior from `Plant` vs. `FloweringPlant` vs. `PrizeFlower` seems to come from the "wrong" class, check `ClassName.__mro__` rather than guessing.
- **`@staticmethod` vs. `@classmethod`**: a static method takes neither `self` nor `cls` and behaves like a plain function namespaced under the class (e.g. a validation helper); a classmethod takes `cls` and is typically used for factory methods or to read/modify class-level state (e.g. a running count of all instances).
- **Forward references** (e.g. a method annotated to return `list[GardenManager]` inside `GardenManager` itself) need `from __future__ import annotations` on Python < 3.11, since the class name doesn't exist yet at the point the annotation is normally evaluated.

---

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
