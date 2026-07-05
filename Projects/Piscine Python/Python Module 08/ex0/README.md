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

## Concepts explained

### What a virtual environment actually is

A virtual environment is not a sandboxed copy of the Python interpreter —
it is a **directory layout plus a redirect**. `python3 -m venv matrix_env`
creates `matrix_env/bin/python` (usually a symlink or thin launcher
pointing back at the system interpreter binary), an empty
`matrix_env/lib/python3.X/site-packages`, and a `pyvenv.cfg` file that
records which base interpreter it was built from. No second Python
runtime is compiled or copied — the same interpreter executable is
reused, but it boots into a different *mode*.

### What activation changes at runtime

`source matrix_env/bin/activate` does exactly two things that matter to
Python code: it prepends `matrix_env/bin` to `$PATH` (so typing `python3`
resolves to the venv's launcher instead of the global one), and it
exports `VIRTUAL_ENV=/absolute/path/to/matrix_env`. Neither of those is a
Python-level construct — they're shell-level. The Python-level effect
happens the moment the venv's `python3` launcher starts: it reads
`pyvenv.cfg` sitting next to it and uses that to compute `sys.prefix`.

This is the mechanism `is_in_virtual_environment()` exploits:

```python
prefix_differs = sys.prefix != sys.base_prefix
env_var_set = os.environ.get("VIRTUAL_ENV") is not None
return prefix_differs or env_var_set
```

`sys.base_prefix` is fixed once, at interpreter build/install time, to
the root of the *actual* Python installation (e.g. `/usr`) — it never
changes no matter how the interpreter is invoked. `sys.prefix` is
resolved fresh at every interpreter startup by walking up from
`sys.executable` looking for `pyvenv.cfg`; if it's found, `sys.prefix`
is rewritten to that venv's root directory. Outside any venv, no
`pyvenv.cfg` is found and `sys.prefix` collapses back to
`sys.base_prefix`, so the two are equal. This is precisely why the
comparison works: it doesn't ask "was `activate` sourced?" (a shell
question), it asks "did this specific interpreter process boot from a
`pyvenv.cfg`?" (an interpreter-state question) — which is the actually
correct question for a Python program to ask.

### Why check `VIRTUAL_ENV` too

The prefix comparison alone is not universal. Some environment managers
(older `conda` setups, certain nested shells, some CI runner
configurations) launch a Python whose `sys.prefix` legitimately equals
`sys.base_prefix` from the interpreter's point of view, yet the
surrounding shell still considers itself "inside" an isolated
environment via `VIRTUAL_ENV`. Combining both checks with `or` means
`is_in_virtual_environment()` reports isolation if *either* signal is
present, covering more real-world activation styles than either check
alone. `get_venv_name()` and `get_venv_path()` follow the same
precedence: they trust `VIRTUAL_ENV` first (it directly names the venv
directory) and only fall back to deriving a name from `sys.prefix` when
the environment variable isn't exported.

### Why this matters practically

Without a venv, `pip install <package>` writes into the single global
`site-packages` shared by every Python program on the machine. Two
projects that need different major versions of the same library (e.g.
one needs `numpy 1.x`, another needs `numpy 2.x`) cannot both be
satisfied globally — installing one breaks the other. This is the
classic "works on my machine" failure: a script relies on whatever
happens to be installed globally at the time, so it silently breaks
when the global state changes or when run on a different machine with
a different global state. A venv gives each project its own
`site-packages` (what `get_package_install_path()` locates via
`site.getsitepackages()`), so `pip install` there is scoped to that
project only — reproducibility comes from isolation, not from careful
manual bookkeeping of a shared global environment.

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
