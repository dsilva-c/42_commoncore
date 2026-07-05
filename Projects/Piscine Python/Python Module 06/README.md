# Module 06 – The Alchemist's Codex
## Mastering Python's Import Mysteries

## 📋 Overview

This module explores Python's package and import system through the metaphor
of an **Alchemical Laboratory**. Four experiments (Parts I–IV) build up a
complete `alchemy` package that demonstrates professional Python code
organisation: controlling a package's public API via `__init__.py`, using
the various `import` styles, choosing between absolute and relative imports,
and resolving circular dependencies safely.

**Python Version**: 3.10+
**Focus**: `__init__.py`, absolute vs relative imports, `from...import`, circular-dependency resolution

## 🎯 Learning Objectives

After completing this module you should understand:

- What makes a directory a Python package, and how `__init__.py` runs once
  per process and defines the package's public surface.
- How to control what a package exposes by re-exporting selected symbols in
  `__init__.py`, leaving the rest reachable only via direct submodule access.
- The difference between `import module`, `from module import name`, and
  aliased imports (`... as alias`), and when each is appropriate.
- How absolute imports (starting at the top-level package) differ from
  relative imports (dot notation relative to the current package), and why
  relative imports are invalid in top-level scripts.
- Why circular imports happen (a module is only half-loaded when another
  module tries to import from it) and how to break the cycle with a late
  import, dependency injection, or a shared lower-level module.

## 📁 Project Structure

```
Python Module 06/
├── alchemy/
│   ├── __init__.py                   # Sacred Scroll – controls package API
│   ├── elements.py                   # Four elemental spell functions
│   ├── potions.py                    # Potion recipe functions
│   ├── transmutation/
│   │   ├── __init__.py               # Exposes all transmutation functions
│   │   ├── basic.py                  # Absolute imports
│   │   └── advanced.py               # Relative imports
│   └── grimoire/
│       ├── __init__.py               # Exposes grimoire public API
│       ├── validator.py              # Ingredient validator
│       └── spellbook.py              # Spell recorder (late import pattern)
├── ft_sacred_scroll.py               # Part I demo script
├── ft_import_transmutation.py        # Part II demo script
├── ft_pathway_debate.py              # Part III demo script
├── ft_circular_curse.py              # Part IV demo script
├── main.py                           # Automated test suite (33 tests)
├── pyrightconfig.json                # Pyright / Pylance configuration
├── README.md                         # This file
└── en.subject.pdf                    # Original project subject
```

## 🚀 Usage

```bash
# Run the automated test suite
python3 main.py

# Run individual demo scripts
python3 ft_sacred_scroll.py
python3 ft_import_transmutation.py
python3 ft_pathway_debate.py
python3 ft_circular_curse.py

# Verbose test output
python3 main.py -v
```

## 📚 Exercises

### Part I – The Sacred Scroll (`ft_sacred_scroll.py`, `alchemy/__init__.py`, `alchemy/elements.py`)

Goal: show that `__init__.py` controls a package's public API.

- `alchemy/elements.py` defines four elemental factory functions:
  `create_fire`, `create_water`, `create_earth`, `create_air`.
- `alchemy/__init__.py` re-exports only `create_fire` and `create_water`,
  plus package metadata (`__version__`, `__author__`).
- `ft_sacred_scroll.py` calls both `alchemy.create_fire()` (package-level,
  exposed) and `alchemy.elements.create_fire()` (direct submodule access,
  always available), and shows that `alchemy.create_earth()` raises
  `AttributeError` because it was never imported into `__init__.py`.

### Part II – Import Transmutation (`ft_import_transmutation.py`, `alchemy/potions.py`)

Goal: practice the different ways Python lets you bring a name into scope.

- `alchemy/potions.py` adds `healing_potion`, `strength_potion`,
  `invisibility_potion`, and `wisdom_potion` to exercise cross-module
  imports.
- `ft_import_transmutation.py` demonstrates four import styles in one file:
  - full module import — `import alchemy.elements`
  - specific function import — `from alchemy.elements import create_water`
  - aliased import — `from alchemy.potions import healing_potion as heal`
  - multiple imports in one statement — `from alchemy.elements import create_earth, create_fire`

### Part III – The Great Pathway Debate (`ft_pathway_debate.py`, `alchemy/transmutation/`)

Goal: prove absolute and relative imports resolve to the same object.

- `alchemy/transmutation/basic.py` uses an **absolute** import:
  `from alchemy.elements import create_fire`.
- `alchemy/transmutation/advanced.py` uses **relative** imports:
  `from .basic import lead_to_gold` and `from ..potions import healing_potion`.
- `alchemy/transmutation/__init__.py` re-exports both modules' public
  functions so the subpackage presents one clean API surface.
- `ft_pathway_debate.py` calls functions from both modules and shows
  identical output, confirming the two import styles reach the same code.

### Part IV – Breaking the Circular Curse (`ft_circular_curse.py`, `alchemy/grimoire/`)

Goal: resolve a circular-dependency risk without hacks.

- `alchemy/grimoire/validator.py` validates ingredient strings, returning a
  string ending in `" - VALID"` or `" - INVALID"`.
- `alchemy/grimoire/spellbook.py` records spells with `record_spell`, which
  needs `validator` — but imports it **inside the function body** (a late
  import) instead of at module top level, so no cycle forms at load time.
- `ft_circular_curse.py` demonstrates that `spellbook` and `validator` can
  reference each other safely thanks to the late import.

## 🧠 Key Concepts

### The Sacred Scroll (`__init__.py`)

`__init__.py` is what turns a plain directory into a Python **package**.
It runs once per process, the first time the package is imported, and the
loaded module is cached in `sys.modules`. Whatever you import inside it
becomes accessible as `package.name`. Symbols *not* imported there remain
hidden at the package level and require direct submodule access.

```python
# alchemy/__init__.py
from .elements import create_fire, create_water  # exposed
# create_earth and create_air are NOT imported → hidden
```

This is the standard way to control a package's public API: re-export the
symbols meant for external use, keep internal helpers unexposed, and only
define `__all__` when `import *` is actually justified.

### Absolute vs Relative Imports

<div align="center">

| Style | Example | When to use |
|-------|---------|-------------|
| Absolute | `from alchemy.elements import create_fire` | Cross-package references, top-level scripts |
| Relative | `from .basic import lead_to_gold` | Intra-package references |

</div>

Absolute imports start at the top-level package name and work the same
regardless of where the importing file lives. Relative imports use dot
notation relative to the current package (`.` for the same package, `..`
for the parent) and are only valid *inside* a package — they cannot be used
in a standalone top-level script. Relative imports tend to be more
refactoring-friendly within a package, while PEP 8 recommends absolute
imports for most other cases.

### Breaking Circular Dependencies (Late Import)

A circular import happens when module A imports module B, which in turn
tries to import from module A before A has finished loading — Python caches
the partially-initialized module, so the second import can raise
`ImportError` or `AttributeError`.

The simplest fix is to import the conflicting module **inside the
function** so it only runs at call time, long after both modules have
finished loading:

```python
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients  # late import
    ...
```

Late imports aren't the only fix, though — **dependency injection** (pass
the needed function/object in as a parameter instead of importing it) or
**extracting the shared code into a third, lower-level module** that
neither original module imports both avoid the cycle without deferring
anything.

## 🧪 Testing

`main.py` is the automated test suite covering all four parts (33 tests).
Each test function returns a `(bool, str)` pass/fail result with a message,
and the suite exits with status code 1 if any test fails.

```bash
python3 main.py       # normal run
python3 main.py -v    # verbose output
```

Expected output on success:

```
╔══════════════════════════════════════════════════════════╗
║  The Alchemist's Codex – Module 06 Test Suite           ║
╚══════════════════════════════════════════════════════════╝
...
  RESULTS: 33/33 tests passed  – All mysteries mastered!
```

Each of the four `ft_*.py` demo scripts can also be run individually to
visually inspect its output against the behaviour described in the
Exercises section above.

## ✅ Code Style & Requirements

- Python 3.10+.
- All functions carry complete type annotations.
- All files pass `flake8` with zero warnings.
- Pyright / Pylance strict mode: 0 errors (see `pyrightconfig.json`).
- Only standard-library imports are used inside the `alchemy` package —
  no third-party dependencies.
- No `sys.path` modification, no `eval()`/`exec()`, and no dynamic
  `importlib` imports — package structure and standard import statements
  only.

## 🛡️ Defense Notes

- **Substring gotcha in validation checks**: testing `"VALID" in result`
  breaks when `result` can be `"INVALID"`, since `"VALID"` is itself a
  substring of `"INVALID"`. `alchemy/grimoire/validator.py` avoids this by
  returning strings that end in `" - VALID"` or `" - INVALID"` — check for
  the more specific marker (or use equality/prefix checks) rather than
  plain substring containment.
- **Late imports aren't the only cycle-breaker**: besides moving the
  `import` inside the function body, a circular dependency can also be
  resolved with dependency injection (pass the needed function/object in
  as a parameter instead of importing it) or by extracting the shared code
  into a third, lower-level module that neither original module imports.
- **Package-level vs submodule access are genuinely different**:
  `alchemy.create_fire()` only works because `__init__.py` explicitly
  imported `create_fire`; `alchemy.elements.create_fire()` always works
  because it addresses the submodule directly. Confusing the two is a
  common source of "why is this AttributeError happening" during defense.
- **Absolute and relative imports must resolve identically**: Part III's
  whole point is that `alchemy/transmutation/basic.py` (absolute) and
  `alchemy/transmutation/advanced.py` (relative) reach the exact same
  functions — if their outputs ever diverged, that would indicate a bug in
  package structure, not a legitimate difference between import styles.
- **Relative imports have a hard scope limit**: they only work inside a
  package (a module imported as part of a package hierarchy); attempting a
  relative import from a script run directly (`python3 script.py`) raises
  `ImportError: attempted relative import with no known parent package`.

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
