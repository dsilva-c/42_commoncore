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
