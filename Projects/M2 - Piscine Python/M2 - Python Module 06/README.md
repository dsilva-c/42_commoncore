# Module 06 – The Alchemist's Codex
## Mastering Python's Import Mysteries

### Python Packages, `__init__.py`, and Import Mechanisms

---

## Project Overview

This module explores Python's import system through the metaphor of an
**Alchemical Laboratory**.  Four experiments (Parts I–IV) build up a complete
`alchemy` package that demonstrates professional Python code organisation.

**Python Version**: 3.10+  
**Focus**: `__init__.py`, absolute vs relative imports, `from...import`, circular-dependency resolution

---

## Project Structure

```
M2 - Python Module 06/
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
├── DEFENSE_GUIDE.md                  # Defense preparation
├── SUBMISSION_CHECKLIST.md           # Submission checklist
└── en.subject.pdf                    # Original project subject
```

---

## Quick Start

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

---

## Part Summary

| Part | File(s) | Key Concept |
|------|---------|-------------|
| I | `alchemy/__init__.py`, `elements.py` | `__init__.py` controls package API |
| II | `alchemy/potions.py` | `from...import`, aliased & multiple imports |
| III | `alchemy/transmutation/` | Absolute vs relative imports |
| IV | `alchemy/grimoire/` | Late import to break circular dependencies |

---

## Key Concepts

### The Sacred Scroll (`__init__.py`)

`__init__.py` is what turns a plain directory into a Python **package**.
Whatever you import inside it becomes accessible as `package.name`.
Symbols *not* imported there remain hidden and require direct module access.

```python
# alchemy/__init__.py
from .elements import create_fire, create_water  # exposed
# create_earth and create_air are NOT imported → hidden
```

### Absolute vs Relative Imports

| Style | Example | When to use |
|-------|---------|-------------|
| Absolute | `from alchemy.elements import create_fire` | Cross-package references, top-level scripts |
| Relative | `from .basic import lead_to_gold` | Intra-package references |

### Breaking Circular Dependencies (Late Import)

Import the conflicting module **inside the function** so it only runs at
call time, not at module load time:

```python
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients  # late import
    ...
```

---

## Running the Test Suite

```
╔══════════════════════════════════════════════════════════╗
║  The Alchemist's Codex – Module 06 Test Suite           ║
╚══════════════════════════════════════════════════════════╝
...
  RESULTS: 33/33 tests passed  – All mysteries mastered!
```
