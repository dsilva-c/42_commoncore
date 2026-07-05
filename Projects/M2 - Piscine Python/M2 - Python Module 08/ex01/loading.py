"""Exercise 01: Loading Programs — package management & data analysis.

Demonstrates:
  • Dependency checking via importlib (graceful degradation)
  • pip vs Poetry dependency management approaches
  • Data analysis with pandas and numpy
  • Visualization with matplotlib

Authorized: pandas, requests, matplotlib, numpy, sys, importlib
"""

from __future__ import annotations

import importlib
import importlib.util
import sys
from typing import Any


# ---------------------------------------------------------------------------
# Dependency helpers
# ---------------------------------------------------------------------------

_REQUIRED: list[str] = ["pandas", "numpy", "matplotlib"]
_OPTIONAL: list[str] = ["requests"]


def _pkg_version(name: str) -> str:
    """Return the installed version string for *name*, or 'unknown'."""
    try:
        mod: Any = importlib.import_module(name)
        version: Any = getattr(mod, "__version__", None)
        if isinstance(version, str):
            return version
        return "unknown"
    except ImportError:
        return "not installed"


def check_dependencies() -> bool:
    """Check required packages and print status for each.

    Returns True only when all required packages are present.
    """
    print("Checking dependencies:")
    all_ok: bool = True

    for pkg in _REQUIRED:
        spec = importlib.util.find_spec(pkg)
        if spec is None:
            print(f"  [MISSING] {pkg} — not installed")
            all_ok = False
        else:
            ver: str = _pkg_version(pkg)
            label: str = pkg.ljust(10)
            print(f"  [OK] {label} ({ver})")

    for pkg in _OPTIONAL:
        spec = importlib.util.find_spec(pkg)
        status: str = "available" if spec is not None else "not installed"
        ver2: str = _pkg_version(pkg) if spec is not None else "—"
        print(f"  [optional] {pkg} ({ver2}) — {status}")

    if not all_ok:
        print()
        print("Install missing packages with one of:")
        print("  pip install -r requirements.txt          # pip approach")
        print("  poetry install                           # Poetry approach")

    return all_ok


# ---------------------------------------------------------------------------
# Data generation and analysis
# ---------------------------------------------------------------------------

def generate_matrix_data(n: int = 1000) -> Any:
    """Generate synthetic 'Matrix signal' data.

    Args:
        n: Number of data points to simulate.

    Returns:
        DataFrame with columns: time, signal, noise, combined.
    """
    import numpy as np
    import pandas as pd

    rng = np.random.default_rng(seed=42)
    time: np.ndarray = np.linspace(0, 4 * np.pi, n)
    signal: np.ndarray = np.sin(time) + 0.5 * np.sin(3 * time)
    noise: np.ndarray = rng.normal(0, 0.15, n)
    combined: np.ndarray = signal + noise

    return pd.DataFrame(
        {
            "time": time,
            "signal": signal,
            "noise": noise,
            "combined": combined,
        }
    )


def analyse_data(df: Any) -> dict[str, float]:
    """Compute summary statistics on the combined signal.

    Args:
        df: DataFrame produced by generate_matrix_data().

    Returns:
        Dictionary of named statistics.
    """
    combined = df["combined"]
    stats: dict[str, float] = {
        "mean": float(combined.mean()),  # type: ignore[arg-type]
        "std": float(combined.std()),  # type: ignore[arg-type]
        "min": float(combined.min()),  # type: ignore[arg-type]
        "max": float(combined.max()),  # type: ignore[arg-type]
        "range": float(  # type: ignore[arg-type]
            combined.max() - combined.min()
        ),
    }
    return stats


# ---------------------------------------------------------------------------
# Visualisation
# ---------------------------------------------------------------------------

def create_visualisation(
    df: Any,
    output_path: str = "matrix_analysis.png",
) -> None:
    """Generate and save a two-panel plot of the Matrix signal.

    Args:
        df: DataFrame produced by generate_matrix_data().
        output_path: File path for the saved PNG image.
    """
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))  # type: ignore[misc]
    fig.suptitle(  # type: ignore[misc]
        "Matrix Signal Analysis", fontsize=14, fontweight="bold"
    )

    # Panel 1 — raw signal vs combined
    ax1.plot(df["time"], df["signal"], label="Clean signal", alpha=0.8)
    ax1.plot(
        df["time"],
        df["combined"],
        label="Signal + noise",
        alpha=0.5,
        linewidth=0.8,
    )
    ax1.set_ylabel("Amplitude")
    ax1.set_title("Signal Components")
    ax1.legend(loc="upper right")
    ax1.grid(True, alpha=0.3)

    # Panel 2 — histogram of residuals
    residuals = df["combined"] - df["signal"]
    ax2.hist(residuals, bins=40, color="steelblue", edgecolor="white",
             alpha=0.8)
    ax2.set_xlabel("Residual (noise)")
    ax2.set_ylabel("Count")
    ax2.set_title("Noise Distribution")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=100)  # type: ignore[misc]
    plt.close(fig)


# ---------------------------------------------------------------------------
# pip vs Poetry comparison
# ---------------------------------------------------------------------------

def show_package_manager_comparison() -> None:
    """Print a side-by-side comparison of pip and Poetry workflows."""
    print()
    print("─" * 55)
    print("  Package Manager Comparison")
    print("─" * 55)
    rows: list[tuple[str, str, str]] = [
        ("Dependency file",  "requirements.txt", "pyproject.toml"),
        ("Install",          "pip install -r …", "poetry install"),
        ("Add package",      "pip install pkg",  "poetry add pkg"),
        ("Virtual env",      "manual (venv)",    "automatic"),
        ("Lock file",        "pip freeze >…",    "poetry.lock"),
        ("Run script",       "python script.py", "poetry run …"),
        ("Version pinning",  "manual",           "automatic"),
    ]
    header: tuple[str, str, str] = ("Feature", "pip", "Poetry")
    fmt = "  {:<18} {:<18} {:<16}"
    print(fmt.format(*header))
    print("  " + "-" * 53)
    for row in rows:
        print(fmt.format(*row))
    print("─" * 55)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def run_loading() -> None:
    """Run the full loading-programs demonstration."""
    print("LOADING STATUS: Loading programs...")
    print()

    if not check_dependencies():
        sys.exit(1)

    print()
    print("Analysing Matrix data...")
    print(f"Processing {1000} data points...")

    df = generate_matrix_data(1000)
    stats: dict[str, float] = analyse_data(df)

    print()
    print("Statistics:")
    for key, val in stats.items():
        print(f"  {key:<8}: {val:+.4f}")

    print()
    print("Generating visualisation...")
    output: str = "matrix_analysis.png"
    try:
        create_visualisation(df, output)
        print("Analysis complete!")
        print(f"Results saved to: {output}")
    except OSError as exc:
        print(f"[ERROR] Could not save visualisation: {exc}")

    show_package_manager_comparison()


if __name__ == "__main__":
    run_loading()
