# ex0 — Entering the Matrix

## Goal

Detect whether the Python interpreter is running inside a **virtual
environment** and adapt the output accordingly.

## Files

<div align="center">

| File | Role |
|------|------|
| `construct.py` | Core logic — venv detection and display |
| `main.py` | Module-style entry-point |

</div>

## Function design

```
is_in_virtual_environment() -> bool
    Checks sys.prefix vs sys.base_prefix AND the VIRTUAL_ENV env-var.

get_venv_name() -> str | None
    Derives the environment name from VIRTUAL_ENV or sys.prefix.

get_venv_path() -> str
    Returns the absolute path to the active environment.

get_package_install_path() -> str
    Returns site-packages path (graceful fallback on AttributeError).

show_outside_matrix() -> None
    Output when NOT in a venv — warns and shows activation commands.

show_inside_construct() -> None
    Output when in a venv — shows details and package install location.

run_construct() -> None
    Top-level dispatcher: calls show_inside/show_outside based on detection.
```

## Running

```bash
# From module root — run directly
python3 ex0/construct.py

# From module root — run as module (uses __init__.py imports)
python3 -m ex0.main

# Example: create and test a virtual environment
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 ex0/construct.py
deactivate
```

## Expected output

**Outside a virtual environment**

```
MATRIX STATUS: You're still plugged in
Current Python: /usr/bin/python3.11
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
  python -m venv matrix_env
  source matrix_env/bin/activate  # On Unix
  matrix_env\Scripts\activate    # On Windows

Then run this program again.
```

**Inside a virtual environment**

```
MATRIX STATUS: Welcome to the construct
Current Python: /path/to/matrix_env/bin/python
Virtual Environment: matrix_env
Environment Path: /path/to/matrix_env

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:
/path/to/matrix_env/lib/python3.11/site-packages
```

## Pylance notes

- `sys.prefix` and `sys.base_prefix` are both `str`, so the comparison
  `sys.prefix != sys.base_prefix` is fully typed — no `Any`.
- `os.environ.get("VIRTUAL_ENV")` returns `str | None`; the result is stored
  in an explicit `str | None` variable and checked before use.
- `get_venv_name()` is typed `-> str | None`; all callers use an explicit
  `str | None` annotation on the receiving variable so Pylance propagates
  the `None` branch correctly.
- `site.getsitepackages()` is wrapped in `try/except AttributeError` because
  it does not exist in all Python builds — Pylance sees the fallback string
  and reports no unreachable code warnings.
- All functions have explicit return-type annotations; no implicit `None`
  leaks through untyped paths.
