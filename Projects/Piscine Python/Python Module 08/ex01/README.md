# ex01 — Loading Programs

## Goal

Demonstrate **package dependency management** with both `pip` and `Poetry`,
while performing a real data-analysis workflow using `pandas`, `numpy`, and
`matplotlib`.

## Files

<div align="center">

| File | Role |
|------|------|
| `loading.py` | Core program — dependency check, analysis, visualisation |
| `main.py` | Module-style entry-point |
| `requirements.txt` | pip dependency file |
| `pyproject.toml` | Poetry project & dependency file |

</div>

## Function design

```
check_dependencies() -> bool
    Iterates _REQUIRED and _OPTIONAL via importlib.util.find_spec().
    Prints [OK] / [MISSING] status with version strings.
    Returns False and prints install instructions on any missing required pkg.

generate_matrix_data(n: int) -> pd.DataFrame
    Creates a sine-wave "signal" plus Gaussian noise with numpy.
    Seeds numpy's default_rng for reproducibility.

analyse_data(df: pd.DataFrame) -> dict[str, float]
    Computes mean, std, min, max, range on the combined channel.

create_visualisation(df, output_path) -> None
    Saves a two-panel PNG: signal overlay and noise histogram.

show_package_manager_comparison() -> None
    Prints a formatted table comparing pip and Poetry workflows.

run_loading() -> None
    Top-level dispatcher: checks deps, runs analysis, saves plot.
```

## Running

```bash
# pip workflow
pip install -r requirements.txt
python3 ex01/loading.py           # direct execution
python3 -m ex01.main              # module execution

# Poetry workflow
cd ex01
poetry install
poetry run python loading.py
```

## Expected output (condensed)

```
LOADING STATUS: Loading programs...

Checking dependencies:
  [OK] pandas     (2.1.x)
  [OK] numpy      (1.26.x)
  [OK] matplotlib (3.8.x)
  [optional] requests (2.31.x) — available

Analysing Matrix data...
Processing 1000 data points...

Statistics:
  mean    : +0.0023
  std     : +0.7321
  min     : -2.1345
  max     : +2.0987
  range   : +4.2332

Generating visualisation...
Analysis complete!
Results saved to: matrix_analysis.png

───────────────────────────────────────────────────────
  Package Manager Comparison
...
```

## pip vs Poetry — key differences

<div align="center">

| Aspect | pip | Poetry |
|--------|-----|--------|
| Dependency file | `requirements.txt` | `pyproject.toml` |
| Lock file | `pip freeze > …` | `poetry.lock` (automatic) |
| Virtual env | Manual (`python -m venv`) | Automatic |
| Add a package | `pip install pkg` | `poetry add pkg` |
| Run a script | `python script.py` | `poetry run python script.py` |

</div>

## Pylance notes

- `pandas`, `numpy`, and `matplotlib` are top-level imports; once installed
  in the virtual environment Pylance resolves all symbols without errors.
- `matplotlib` ships as `matplotlib-stubs` for typing — annotating the axes
  objects as `Any` from `typing` is avoided by using direct attribute access
  which Pylance resolves through the installed stubs.
- `pd.Series` and `pd.DataFrame` are explicitly typed on every assignment to
  prevent `Unknown` inference warnings.
- `importlib.util.find_spec()` returns `ModuleSpec | None`; the `None` branch
  is always handled before any attribute access.
- `np.random.default_rng()` returns `numpy.random.Generator`; `.normal()` and
  `.linspace()` all carry return-type stubs so Pylance infers `np.ndarray`
  without extra annotations.
- Long lines are kept within 79 characters (flake8 E501).
