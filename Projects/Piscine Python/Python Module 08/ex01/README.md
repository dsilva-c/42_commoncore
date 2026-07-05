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

## Concepts explained

### `find_spec()` vs a bare `try: import`

`check_dependencies()` calls `importlib.util.find_spec(pkg)` for every
name in `_REQUIRED` and `_OPTIONAL`, rather than doing `try: import pkg`
and catching `ImportError`. The difference is not stylistic — the two
approaches perform fundamentally different amounts of work:

- `find_spec(name)` walks `sys.meta_path` finders (the same machinery
  the import system itself uses) to *locate* the module: it checks
  whether a matching `.py` file, package directory, or compiled
  extension exists somewhere on `sys.path`, and returns a `ModuleSpec`
  describing where it lives — or `None` if nothing is found. Crucially,
  it stops there. The module's top-level code never runs.
- `import pkg` does everything `find_spec` does, *and then* executes the
  module's entire top-level code, populates `sys.modules[name]`, resolves
  every one of *its* imports transitively, and runs any side effects
  those modules have (opening files, registering plugins, spawning
  threads, printing warnings, etc.).

For a "is this installed?" presence check, only the first half is
relevant — actually importing `pandas` or `matplotlib` just to answer a
yes/no question wastes real startup time (import-heavy packages like
`matplotlib` can take a noticeable fraction of a second) and risks
tripping an unrelated import-time error in a package you don't even
intend to use yet. `check_dependencies()` only pays the real import cost
in `_pkg_version()`, and only *after* `find_spec` has already confirmed
the package exists — at that point importing it is safe and necessary
because the version string lives on the loaded module object
(`mod.__version__`), which `find_spec`'s `ModuleSpec` does not expose.

### Two dependency-management philosophies: pip vs Poetry

`requirements.txt` and `pyproject.toml` in this directory declare the
*same* four packages (`numpy`, `pandas`, `matplotlib`, `requests`), but
they represent two different philosophies for keeping a project's
dependencies reproducible:

- **pip + `requirements.txt`** is declarative but *unpinned by default*.
  `numpy>=1.26.0` is a floor, not a fixed version — installing today and
  installing a year from now can resolve to different actual versions
  of every dependency, because pip re-resolves the whole graph each
  time using whatever satisfies the constraint at that moment. A fully
  reproducible pip setup requires a separate, manually generated lock
  step (`pip freeze > requirements.lock.txt`) capturing exact resolved
  versions — pip itself has no built-in concept of a lockfile.
- **Poetry + `pyproject.toml`** separates *intent* from *resolution*.
  `pyproject.toml` states caret ranges (`numpy = "^1.26.0"`, meaning
  "compatible with 1.26, i.e. `>=1.26.0,<2.0.0"`), but Poetry always
  resolves the full dependency graph once and writes the exact result —
  every transitive dependency, pinned to an exact version and hash — to
  `poetry.lock`. `poetry install` reads the lock file when present, so
  every machine and every CI run gets byte-identical dependency versions
  until someone deliberately reruns `poetry update`. This is the core
  difference: pip's reproducibility is opt-in and manual, Poetry's is
  automatic and enforced by the tool.

Both files coexisting here means the exact same install can be verified
through either tool (`pip install -r requirements.txt` or
`poetry install`), which is why `show_package_manager_comparison()`
walks through the two workflows side by side — same destination
(`numpy`, `pandas`, `matplotlib`, `requests` importable), different
guarantees about what "install this again later" actually reproduces.

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
