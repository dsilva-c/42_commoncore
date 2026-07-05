"""Exercise 0: Entering the Matrix — virtual environment detection.

Detects whether the interpreter is running inside a virtual environment,
shows Python environment details, and gives instructions when none is found.

Authorized: sys, os, site modules, print()
"""

import os
import site
import sys


def is_in_virtual_environment() -> bool:
    """Return True when running inside a virtual environment.

    Checks both the sys prefix difference and the VIRTUAL_ENV variable
    so it works with venv, virtualenv, conda, and Poetry shells.
    """
    prefix_differs = sys.prefix != sys.base_prefix
    env_var_set = os.environ.get("VIRTUAL_ENV") is not None
    return prefix_differs or env_var_set


def get_venv_name() -> str | None:
    """Return the base name of the active virtual environment, or None."""
    venv_path: str | None = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        return os.path.basename(venv_path)
    # Fallback: derive from sys.prefix when VIRTUAL_ENV is not exported
    if sys.prefix != sys.base_prefix:
        return os.path.basename(sys.prefix)
    return None


def get_venv_path() -> str:
    """Return the absolute path to the active virtual environment."""
    venv_path: str | None = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        return venv_path
    return sys.prefix


def get_package_install_path() -> str:
    """Return the first site-packages directory for the current environment."""
    try:
        paths: list[str] = site.getsitepackages()
        if paths:
            return paths[0]
        return "Unknown (site-packages not found)"
    except AttributeError:
        # site.getsitepackages() is unavailable in some minimal environments
        return "Unknown (site module incomplete)"


def show_outside_matrix() -> None:
    """Print the status output when NOT inside a virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate  # On Unix")
    print("  matrix_env\\Scripts\\activate    # On Windows")
    print()
    print("Then run this program again.")


def show_inside_construct() -> None:
    """Print the status output when running INSIDE a virtual environment."""
    venv_name: str | None = get_venv_name()
    venv_path: str = get_venv_path()
    pkg_path: str = get_package_install_path()

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(pkg_path)


def run_construct() -> None:
    """Entry point — detect environment and display the appropriate info."""
    if is_in_virtual_environment():
        show_inside_construct()
    else:
        show_outside_matrix()


if __name__ == "__main__":
    run_construct()
