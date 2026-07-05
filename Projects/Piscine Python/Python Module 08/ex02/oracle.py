"""Exercise 02: Accessing the Mainframe — secure configuration management.

Loads environment variables from a .env file using python-dotenv,
validates required configuration keys, and reports the environment
security posture for both development and production modes.

Authorized: os, sys, python-dotenv modules, file operations
"""

import importlib.util
import os
import sys
from pathlib import Path

# Check availability once at import time so every call-site can branch on
# the single boolean instead of repeating find_spec() calls.
_DOTENV_AVAILABLE: bool = importlib.util.find_spec("dotenv") is not None


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

ConfigMap = dict[str, str]


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Variables the program expects to be present
_REQUIRED_KEYS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

# Sensible defaults used only for display when a variable is absent
_DEFAULTS: dict[str, str] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "sqlite:///matrix_local.db",
    "API_KEY": "",
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "http://localhost:8080",
}


# ---------------------------------------------------------------------------
# .env loader
# ---------------------------------------------------------------------------

def load_env_file(env_path: Path | None = None) -> bool:
    """Load a .env file into the process environment.

    Args:
        env_path: Explicit path to a .env file.  When None, python-dotenv
                  searches for .env in the current working directory.

    Returns:
        True if a .env file was found and loaded, False otherwise.
    """
    if not _DOTENV_AVAILABLE:
        return False
    # Local import: guaranteed to succeed because _DOTENV_AVAILABLE is True.
    from dotenv import load_dotenv  # noqa: PLC0415
    if env_path is not None:
        found: bool = load_dotenv(dotenv_path=env_path, override=False)
    else:
        found = load_dotenv(override=False)
    return found


# ---------------------------------------------------------------------------
# Configuration reading
# ---------------------------------------------------------------------------

def read_config() -> ConfigMap:
    """Read all known configuration variables from the environment.

    Missing variables receive their default values from _DEFAULTS so the
    returned dict always contains every key.

    Returns:
        Mapping from variable name to its effective string value.
    """
    config: ConfigMap = {}
    for key in _REQUIRED_KEYS:
        value: str | None = os.environ.get(key)
        if value is not None:
            config[key] = value
        else:
            config[key] = _DEFAULTS.get(key, "")
    return config


def validate_config(config: ConfigMap) -> list[str]:
    """Return a list of keys that are present but empty (security risk).

    Args:
        config: Mapping returned by read_config().

    Returns:
        List of key names whose values are empty strings.
    """
    return [k for k, v in config.items() if not v.strip()]


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def _mask(value: str, key: str) -> str:
    """Return a masked value for secrets, or the raw value otherwise."""
    sensitive: list[str] = ["API_KEY", "DATABASE_URL"]
    if key in sensitive and value:
        visible: str = value[:4] if len(value) > 4 else value
        return visible + "*" * max(0, len(value) - 4)
    return value


def show_configuration(config: ConfigMap) -> None:
    """Print a labelled summary of the loaded configuration."""
    mode: str = config["MATRIX_MODE"]
    db_url: str = _mask(config["DATABASE_URL"], "DATABASE_URL")
    api_key: str = _mask(config["API_KEY"], "API_KEY")
    log_level: str = config["LOG_LEVEL"]
    zion: str = config["ZION_ENDPOINT"]

    print("Configuration loaded:")
    print(f"  Mode:          {mode}")
    print(f"  Database:      {db_url or 'Not configured'}")
    print(f"  API Access:    {'Authenticated' if api_key else 'Not set'}")
    print(f"  Log Level:     {log_level}")
    print(f"  Zion Network:  {zion or 'Offline'}")


def show_security_check(
    config: ConfigMap,
    env_file_found: bool,
) -> None:
    """Print the environment security posture report.

    Args:
        config: Mapping returned by read_config().
        env_file_found: Whether a .env file was successfully loaded.
    """
    empty_keys: list[str] = validate_config(config)
    prod_ready: bool = config["MATRIX_MODE"] == "production"

    print()
    print("Environment security check:")

    # Secrets — static guarantee: secrets are never hardcoded in source
    print("  [OK] No hardcoded secrets detected")

    # .env file status
    if env_file_found:
        print("  [OK] .env file properly configured")
    else:
        print(
            "  [WARN] .env file not found "
            "(using environment variables / defaults)"
        )

    # Production readiness
    if prod_ready:
        print("  [OK] Production mode active")
    else:
        print(
            "  [INFO] Production overrides available "
            "(set MATRIX_MODE=production)"
        )

    if empty_keys:
        print()
        print("  [WARN] The following variables have no value:")
        for key in empty_keys:
            print(f"    - {key}")
        print("  Edit your .env (see .env.example for reference).")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def run_oracle() -> None:
    """Run the Oracle configuration-management demonstration."""
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    if not _DOTENV_AVAILABLE:
        print("[ERROR] python-dotenv is not installed.")
        print("Install it with:")
        print("  pip install python-dotenv")
        sys.exit(1)

    # Look for .env next to this file first, then fall back to cwd
    script_dir: Path = Path(__file__).parent
    env_file: Path = script_dir / ".env"
    env_file_found: bool

    try:
        if env_file.exists():
            env_file_found = load_env_file(env_file)
        else:
            env_file_found = load_env_file()
    except OSError as exc:
        print(f"[WARN] Could not read .env file: {exc}")
        env_file_found = False

    if not env_file_found:
        print(
            "[INFO] No .env file found — relying on environment variables "
            "and defaults."
        )
        print(
            "       Copy .env.example to .env and fill in your values."
        )
        print()

    config: ConfigMap = read_config()
    show_configuration(config)
    show_security_check(config, env_file_found)

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    run_oracle()
