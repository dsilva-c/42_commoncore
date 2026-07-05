# The Matrix — Welcome to the Real World of Data Engineering

Python Piscine · Module 08

## Overview

Master the real-world data-engineering survival kit: virtual environments,
dependency management, and secure configuration.

| Exercise | Focus | Key Tools |
|----------|-------|-----------|
| ex0 | Virtual Environments | `venv`, `sys`, `os`, `site` |
| ex01 | Package Management | `pip`, `Poetry`, `pandas`, `numpy`, `matplotlib` |
| ex02 | Environment Variables | `python-dotenv`, `.env`, `.gitignore` |

## Project structure

```
.
├── __init__.py
├── ex0/
│   ├── __init__.py
│   ├── construct.py
│   ├── main.py
│   └── README.md
├── ex01/
│   ├── __init__.py
│   ├── loading.py
│   ├── requirements.txt
│   ├── pyproject.toml
│   ├── main.py
│   └── README.md
└── ex02/
    ├── __init__.py
    ├── oracle.py
    ├── .env.example
    ├── .gitignore
    ├── main.py
    └── README.md
```

## Running exercises

Execute from the **module root**:

```bash
# Exercise 0 — virtual environment detection
python3 ex0/construct.py          # run directly
python3 -m ex0.main               # run as module

# Exercise 01 — package management & data analysis
pip install -r ex01/requirements.txt
python3 ex01/loading.py           # run directly
python3 -m ex01.main              # run as module

# Exercise 02 — secure configuration via .env
cd ex02 && cp .env.example .env   # fill in real values
python3 ex02/oracle.py            # run directly
python3 -m ex02.main              # run as module
```

## Pylance / static analysis

All source files comply with Pylance strict-mode expectations:

- **Full type annotations** on every function signature (`-> None`, `-> str`,
  `-> bool`, `-> dict[str, str]`, etc.).
- **No implicit `Any`** — every variable that could be inferred as `Any` is
  explicitly typed.
- **`str | None`** union syntax (Python ≥ 3.10 short form) is used throughout.
- External packages (`pandas`, `numpy`, `matplotlib`, `python-dotenv`) are
  imported at the top level after being installed in the virtual environment,
  so Pylance resolves them without errors.  Install once with:
  ```bash
  pip install pandas numpy matplotlib requests python-dotenv
  ```
- `importlib.util.find_spec()` is used for **runtime** dependency checking
  (graceful degradation messages) without creating unresolved-import warnings
  in Pylance.
- `os.environ.get()` returns `str | None`; every usage performs explicit
  `None`-checks so Pylance does not raise *"Object of type None cannot be
  used in a string context"* errors.
- `site.getsitepackages()` returns `list[str]`; the result is guarded before
  indexing.

Run a quick sanity check with pyright / Pylance CLI:

```bash
pip install pyright
python3 -m pyright .
```

## General requirements

- Python 3.10 or later.
- `flake8` linting standards — max line length 79 characters, snake\_case
  naming, proper spacing.
- All functions use `try-except` blocks where external state (environment,
  files, packages) can fail.
- Never commit real secrets — `.env` is in `.gitignore`.
