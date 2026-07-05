# The Matrix — Welcome to the Real World of Data Engineering

Python Piscine · Module 08

## 📋 Overview

Master the real-world data-engineering survival kit: virtual environment
detection, package dependency management (`pip` and Poetry) combined with
a real `pandas`/`numpy`/`matplotlib` data-analysis workflow, and secure
configuration via `.env` files. Targets Python 3.10+ with full type
annotations and Pylance/pyright strict-mode compliance throughout.

## 🎯 Learning Objectives

- Detect programmatically whether the interpreter is running inside a
  virtual environment, and understand what actually changes (`sys.prefix`,
  `sys.base_prefix`, `VIRTUAL_ENV`, `site-packages` location).
- Understand why per-project virtual environments exist and how `venv`
  relates to `virtualenv`, `conda`, and Poetry.
- Check for optional/required third-party dependencies at runtime without
  triggering import side effects (`importlib.util.find_spec`).
- Run the same dependency-management workflow through two different
  tools — `pip` + `requirements.txt` and Poetry + `pyproject.toml`.
- Perform a small end-to-end data-analysis pipeline: generate data with
  `numpy`, summarise it, and visualise it with `matplotlib`.
- Load secrets/configuration from a `.env` file with `python-dotenv`,
  validate it, and report a security posture without ever printing real
  secrets.
- Keep `.env` out of version control while still documenting required
  keys via a committed `.env.example`.

## 📁 Project Structure

```
.
├── __init__.py
├── main.py
├── matrix_analysis.png
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

## 🚀 Usage

Execute from the **module root**:

```bash
# Run all three exercises in sequence
python3 main.py

# Exercise 0 — virtual environment detection
python3 ex0/construct.py          # run directly
python3 -m ex0.main               # run as module

# Exercise 01 — package management & data analysis
pip install -r ex01/requirements.txt
python3 ex01/loading.py           # run directly
python3 -m ex01.main              # run as module

# Exercise 01 — Poetry workflow alternative
cd ex01 && poetry install && poetry run python loading.py

# Exercise 02 — secure configuration via .env
cd ex02 && cp .env.example .env   # fill in real values
python3 ex02/oracle.py            # run directly
python3 -m ex02.main              # run as module

# Exercise 02 — override .env with shell variables
MATRIX_MODE=production API_KEY=s3cr3t python3 ex02/oracle.py
```

## 📚 Exercises

### ex0 — Entering the Matrix

`ex0/construct.py`

Detect whether the interpreter is running inside a virtual environment
and adapt the output accordingly.

- `is_in_virtual_environment() -> bool` combines `sys.prefix != sys.base_prefix`
  with `os.environ.get("VIRTUAL_ENV")` so it works across `venv`,
  `virtualenv`, conda, and Poetry shells.
- `get_venv_name()` / `get_venv_path()` derive the environment's name and
  absolute path from `VIRTUAL_ENV`, falling back to `sys.prefix`.
- `get_package_install_path()` calls `site.getsitepackages()` inside a
  `try/except AttributeError`, since it doesn't exist in all Python builds.
- `show_outside_matrix()` / `show_inside_construct()` print different
  status reports (with activation instructions) depending on detection.

### ex01 — Loading Programs

`ex01/loading.py`

Demonstrate package dependency management with both `pip` and Poetry,
while running a real data-analysis workflow.

- `check_dependencies()` iterates required (`pandas`, `numpy`,
  `matplotlib`) and optional (`requests`) packages via
  `importlib.util.find_spec()`, printing `[OK]`/`[MISSING]` per package.
- `generate_matrix_data(n)` builds a sine-wave "signal" plus Gaussian
  noise using `numpy.random.default_rng` (seeded for reproducibility).
- `analyse_data(df)` computes mean, std, min, max, and range on the
  combined channel.
- `create_visualisation(df, output_path)` saves a two-panel PNG — signal
  overlay and noise histogram — to `matrix_analysis.png` (committed at
  the module root as a reference output of this exercise).
- `show_package_manager_comparison()` prints a side-by-side comparison of
  `pip` and Poetry workflows.
- The same dependency set is declared twice, in `requirements.txt` (pip)
  and `pyproject.toml` (Poetry), so both tools are exercised on identical
  packages.

### ex02 — Accessing the Mainframe

`ex02/oracle.py`

Build a secure configuration system that loads secrets from a `.env`
file, validates them, and reports the environment's security posture.

- `_DOTENV_AVAILABLE` is computed once at import time via
  `find_spec("dotenv")`; every later branch checks this flag instead of
  calling `find_spec` repeatedly.
- `load_env_file(path)` calls `load_dotenv()` with `override=False`, so
  real shell environment variables always take precedence over `.env`
  entries — safe for CI/CD pipelines.
- `read_config()` reads five keys (`MATRIX_MODE`, `DATABASE_URL`,
  `API_KEY`, `LOG_LEVEL`, `ZION_ENDPOINT`) from `os.environ`, falling
  back to sane defaults so it never raises `KeyError`.
- `validate_config(config)` returns a list of validation-failure strings
  instead of raising, so all problems can be reported at once.
- `_mask_value()` partially masks sensitive keys (e.g. `API_KEY`,
  `DATABASE_URL`) before they are ever printed.
- `.env.example` is committed as a template with placeholder values;
  `.env` itself is listed in `ex02/.gitignore` and never committed.

## 🧠 Key Concepts

**Virtual environment detection**

```python
import sys, os

def is_in_venv() -> bool:
    return (
        sys.prefix != sys.base_prefix
        or os.environ.get("VIRTUAL_ENV") is not None
    )
```

`sys.base_prefix` is fixed at interpreter startup to the original Python
installation root. `sys.prefix` is the *active* environment root — equal
to `sys.base_prefix` outside a venv, but rewritten to the venv path once
one is activated. Checking `VIRTUAL_ENV` as well covers setups (some
conda configurations, certain CI runners) where the prefix trick alone
doesn't apply.

**Graceful dependency checking**

```python
import importlib.util

def has_package(name: str) -> bool:
    return importlib.util.find_spec(name) is not None
```

`find_spec()` only *locates* a module on `sys.path` and returns a
`ModuleSpec` (or `None`) — it never executes the module, so it is the
correct tool for "is this installed?" checks, unlike a bare
`try: import x` which pays the full import cost and side effects.

**Loading `.env` securely**

```python
from dotenv import load_dotenv
load_dotenv(".env")                  # injects into os.environ
value = os.environ.get("API_KEY")    # str | None
```

Secrets never live in source code; `.env` supplies them at runtime and is
excluded from version control via `.gitignore`.

**`pip` vs Poetry**

| Concern | pip | Poetry |
|---------|-----|--------|
| Install a package | `pip install X` | `poetry add X` |
| Freeze dependencies | `pip freeze > requirements.txt` | `poetry.lock` (automatic) |
| Create the venv | `python -m venv .venv` | `poetry env use python3` |
| Run a script | `python3 script.py` | `poetry run python3 script.py` |
| Publish a package | manual `setup.py` / `twine` | `poetry publish` |

## 🧪 Testing

```bash
# Run everything at once
source .venv/bin/activate
python3 main.py

# Run each exercise individually
python3 -m ex0.main
python3 -m ex01.main
python3 -m ex02.main

# Lint
flake8 ex0/ ex01/ ex02/ --max-line-length=79

# Static type check
python3 -m pyright ex0/ ex01/ ex02/ main.py
```

Expected correctness signals per exercise:

- **ex0** — output differs clearly inside vs. outside a virtual
  environment; no crash if `site.getsitepackages()` is unavailable.
- **ex01** — `check_dependencies()` reports `[OK]`/`[MISSING]` for every
  package; a `pd.DataFrame` is produced and summarised; a PNG is written
  to disk; `requirements.txt` and `pyproject.toml` declare identical
  dependencies.
- **ex02** — `.env` loads correctly when present; validation reports
  missing/invalid values; the API key is masked in every printed report;
  the program still runs (with a warning, not a crash) when
  `python-dotenv` isn't installed.

## ✅ Code Style & Requirements

- Python 3.10 or later.
- `flake8` linting — max line length 79 characters, snake_case naming,
  proper spacing; all files pass with zero warnings.
- Full type annotations on every function signature (`-> None`, `-> str`,
  `-> bool`, `-> dict[str, str]`, etc.); no implicit `Any`.
- `str | None` union syntax (Python ≥ 3.10 short form) used throughout,
  e.g. for `os.environ.get()` results — every usage is guarded with an
  explicit `None` check before use.
- `site.getsitepackages()` returns `list[str]`; the result is guarded
  before indexing.
- `importlib.util.find_spec()` used for **runtime** dependency detection
  (never a bare `import` in a `try/except` used purely for a presence
  check).
- All functions wrap `try/except` around operations where external state
  (environment variables, files, packages) can fail.
- Never commit real secrets — `.env` is listed in `.gitignore`.
- External packages (`pandas`, `numpy`, `matplotlib`, `python-dotenv`)
  are imported at the top level after being installed in the virtual
  environment, so Pylance resolves them without errors. Install once
  with:
  ```bash
  pip install pandas numpy matplotlib requests python-dotenv
  ```
- Quick static-analysis sanity check:
  ```bash
  pip install pyright
  python3 -m pyright .
  ```

## 🛡️ Defense Notes

- **`importlib.util.find_spec()` doesn't execute the module** — it only
  locates it on `sys.path` and returns a spec (or `None`), so it's safe
  to use for "is this package installed?" checks without triggering
  import side effects. This is why it's preferred over a bare
  `try: import x` for presence checks.
- **`venv` vs `virtualenv`**: `venv` is the standard-library tool (Python
  3.3+, no extra install, slightly fewer features); `virtualenv` is a
  third-party package that's faster and supports older Pythons/more
  backends — this module uses the built-in `venv`. For most purposes the
  two are functionally equivalent.
- **Why a virtual environment per project?** Different projects may need
  different versions of the same package. Without isolation, installing
  package A for project 1 can silently break project 2 — a venv gives
  each project its own `site-packages` directory.
- **`sys.prefix` vs `sys.base_prefix`**: `sys.base_prefix` is set once at
  interpreter startup to the original Python installation root.
  `sys.prefix` is the active environment root — the same as
  `sys.base_prefix` outside a venv, but rewritten to the venv path once
  one is active. Checking `VIRTUAL_ENV` in addition to the prefix
  comparison covers conda and some CI setups that don't rewrite the
  prefix.
- **Why Pylance/pyright alongside flake8?** `flake8` checks style and
  obvious mistakes (unused imports, line length, spacing). Pylance/
  pyright performs static type analysis — catching type mismatches,
  wrong argument types, `None`-dereference risks, and unresolved
  imports that flake8 cannot see. Together they cover both style and
  correctness.
- **Pylance `reportMissingImports` inside a venv**: if Pylance can't
  resolve packages installed in `.venv`, point it at the interpreter
  explicitly via `pyrightconfig.json`'s `venvPath`/`venv` fields (or
  select the venv's interpreter in the editor) rather than reinstalling
  packages globally.
- **Guarding `os.environ.get()` results**: it returns `str | None`, so
  any direct use (e.g. string concatenation) triggers a Pylance
  "Object of type None cannot be used" error. Fix with an explicit
  check:
  ```python
  value = os.environ.get("KEY")
  if value is not None:
      print(value.upper())
  ```
- **What is `.env.example`?** A template committed to the repository
  showing which keys are required, with placeholder values instead of
  real secrets — new setups copy it to `.env` and fill in real values.
- **`os.environ.get()` vs `os.environ[...]`**: `.get()` returns `None` if
  the key is absent (no exception); `[...]` raises `KeyError`. For
  optional configuration, `.get()` with a default is safer.
- **What if `python-dotenv` isn't installed?** `_DOTENV_AVAILABLE` is
  `False`; `load_env_file()` returns `False` and prints a warning; the
  program continues using whatever variables are already in
  `os.environ` (e.g. from the shell) instead of crashing.

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
