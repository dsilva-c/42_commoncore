# ex02 — Accessing the Mainframe

## Goal

Build a **secure configuration system** that loads secrets and settings
from `.env` files using `python-dotenv`, validates them, and reports the
environment's security posture.

## Files

<div align="center">

| File | Role |
|------|------|
| `oracle.py` | Core program — env loading, validation, security check |
| `main.py` | Module-style entry-point |
| `.env.example` | Template — copy to `.env` and fill in real values |
| `.gitignore` | Ensures `.env` is never accidentally committed |

</div>

## Function design

```
load_env_file(env_path: Path | None) -> bool
    Calls python-dotenv's load_dotenv(); returns True if .env was found.
    Checks _DOTENV_AVAILABLE before calling to gracefully degrade.

read_config() -> ConfigMap
    Reads all _REQUIRED_KEYS from os.environ; fills gaps from _DEFAULTS.
    Always returns a complete dict, never raises KeyError callers.

validate_config(config: ConfigMap) -> list[str]
    Returns keys whose values are empty — potential configuration gaps.

_mask_value(value: str, key: str) -> str
    Partially masks sensitive keys (API_KEY, DATABASE_URL) for display.

show_configuration(config: ConfigMap) -> None
    Prints a formatted configuration summary with masked secrets.

show_security_check(config, env_file_found) -> None
    Prints [OK] / [WARN] / [INFO] security posture lines.

run_oracle() -> None
    Top-level dispatcher: loads env, reads config, shows report.
```

## Concepts explained

### Why secrets belong in `.env`, never in source

Anything committed to version control is effectively permanent and
widely readable: it lives in every clone, every fork, every CI log that
checks the repo out, and — even after a later commit "removes" it —
in the git history forever unless the history itself is rewritten. A
secret hardcoded as `API_KEY = "sk-live-..."` in `oracle.py` would leak
to anyone with read access to the repository, including automated
scanners and, on a public repo, the entire internet. `.env` solves this
by keeping the *values* outside the codebase entirely: `oracle.py` only
ever references key *names* (`_REQUIRED_KEYS`), and the actual secret
strings live in a file that `ex02/.gitignore` explicitly excludes from
commits. `.env.example` is the safe half of that split — it documents
which keys the program expects, with obviously-fake placeholder values
(`your-api-key-here`), so a new clone knows what to fill in without any
real secret ever touching the repository.

### What `load_dotenv(override=False)` actually does

`python-dotenv`'s `load_dotenv()` reads a `.env` file line by line and
calls `os.environ.setdefault(key, value)` — or, if `override=True`,
`os.environ[key] = value` unconditionally — for each entry. The
`override` flag controls which source wins when both a real process
environment variable *and* a `.env` entry exist for the same key.
`load_env_file()` in this exercise always passes `override=False`:

```python
found: bool = load_dotenv(dotenv_path=env_path, override=False)
```

With `override=False`, if `MATRIX_MODE` is already set in `os.environ`
before `load_dotenv()` runs, the `.env` file's `MATRIX_MODE=development`
line is silently ignored and the pre-existing value survives. This is
the safe default for CI/CD specifically because pipelines inject real
configuration and secrets through the platform's own environment
variable mechanism (GitHub Actions secrets, a Kubernetes `Secret`
mounted as env vars, etc.) — not through a `.env` file, which typically
isn't even present in that environment, or is a leftover placeholder
checked out from the repo (`.env.example` renamed, or a stray
development `.env`). If `override=True` were used instead, a stray or
outdated `.env` file could silently clobber the real, deliberately-set
production values, which is exactly backwards: the more "official" and
more direct configuration mechanism should win. `override=False` encodes
the correct precedence — real environment always outranks a file on
disk — without the program needing to know *why* a variable exists in
the environment already.

### Collecting all validation failures instead of failing fast

`validate_config()` returns a `list[str]` of every key with an empty
value, rather than raising on the first problem it encounters:

```python
def validate_config(config: ConfigMap) -> list[str]:
    return [k for k, v in config.items() if not v.strip()]
```

If this instead raised `ValueError` the moment it hit the first empty
key, fixing a misconfigured environment would become a slow loop:
run the program, see one error, fix one variable, run again, see the
*next* error, fix it, run again — one round-trip per problem. Collecting
every failing key up front means `show_security_check()` can print the
complete list in a single pass (`for key in empty_keys: print(f"  - {key}")`),
so a person fixing a `.env` file sees every missing value at once and
can fix them all before the next run. This "report everything, then
decide what to do" pattern is a general validation principle: raising
on the first error is appropriate for something that must halt
immediately (a truly fatal, unrecoverable state), but for configuration
checks — where the useful output is a diagnosis, not a crash — gathering
the full picture first gives the caller strictly more information for
the same amount of effort.

## Running

```bash
# Without .env — uses defaults and shows warnings
python3 ex02/oracle.py

# With .env file
cp ex02/.env.example ex02/.env
# edit ex02/.env with real values
python3 ex02/oracle.py

# Override with shell variables (takes precedence over .env)
MATRIX_MODE=production API_KEY=s3cr3t python3 ex02/oracle.py

# Module style
python3 -m ex02.main
```

## Configuration variables

<div align="center">

| Variable | Purpose | Default |
|----------|---------|---------|
| `MATRIX_MODE` | `development` or `production` | `development` |
| `DATABASE_URL` | Connection string | `sqlite:///matrix_local.db` |
| `API_KEY` | External service authentication | *(empty)* |
| `LOG_LEVEL` | Logging verbosity | `DEBUG` |
| `ZION_ENDPOINT` | Resistance network URL | `http://localhost:8080` |

</div>

## Expected output

```
ORACLE STATUS: Reading the Matrix...

Configuration loaded:
  Mode:         development
  Database:     sqli********************
  API Access:   Not set
  Log Level:    DEBUG
  Zion Network: http://localhost:8080

Environment security check:
  [OK] No hardcoded secrets detected
  [OK] .env file properly configured
  [INFO] Production overrides available (set MATRIX_MODE=production)

The Oracle sees all configurations.
```

## Security rules

- `.env` is in `.gitignore` — real secrets stay off version control.
- `.env.example` is committed as a template with placeholder values only.
- `override=False` in `load_dotenv` means actual shell variables take
  precedence over `.env` entries — safe for CI/CD pipelines.
- Sensitive values are masked before printing (`_mask_value`).

## Pylance notes

- `from dotenv import load_dotenv as _load_dotenv` is guarded by
  `if _DOTENV_AVAILABLE:` after a `find_spec("dotenv")` check.
  Pylance correctly sees `_load_dotenv` used only inside the same guard,
  so it does not raise *"possibly unbound"* warnings.
- `os.environ.get(key)` returns `str | None`; the result is stored in
  `str | None` and handled properly before assigning to `ConfigMap`.
- `ConfigMap = dict[str, str]` is a plain type alias; Pylance resolves
  it as a concrete type, not `Any`.
- `Path.__truediv__` (the `/` operator) returns `Path`, fully typed.
- `OSError` wraps any file-system error from `Path.exists()` or
  `load_dotenv()`, preventing unhandled exceptions in Pylance's
  exception-flow analysis.
- `_load_dotenv` is typed via python-dotenv's bundled stubs so Pylance
  knows keyword argument names (`dotenv_path`, `override`), return type
  (`bool`), etc., with zero `type: ignore` comments needed.
