# Module 04 - Data Archivist
## Digital Preservation in the Cyber Archives

### Python File Operations, Streams & Error Handling

---

## 📋 Overview

This module focuses on Python's core file I/O capabilities and resource
management. Through a sci-fi archival theme ("Cyber Archives 2087"), the
exercises cover reading and writing files, managing the `stdin`/`stdout`/
`stderr` streams, using context managers for automatic resource cleanup, and
handling file-related exceptions gracefully.

**Python Version**: 3.10+
**Focus**: File Operations, Stream Management, Context Managers, Error Handling

---

## 🎯 Learning Objectives

After completing this module you should understand:

- How to open, read, write and close files with `open()`, and the difference
  between `read()`, `readline()` and `readlines()`.
- The purpose of file modes (`'r'`, `'w'`, `'a'`) and what happens to existing
  content in each case.
- The role of the three standard streams (`stdin`, `stdout`, `stderr`) and why
  keeping them separate matters for redirection and piping.
- How the `with` statement implements RAII (Resource Acquisition Is
  Initialization) in Python, guaranteeing a file is closed even if an
  exception is raised inside the block.
- How to catch specific exceptions (`FileNotFoundError`, `PermissionError`)
  before falling back to a generic `Exception` handler, and why ordering
  matters.
- Where `FileNotFoundError` and `PermissionError` sit in Python's built-in
  exception hierarchy.

---

## 📁 Project Structure

```
Python Module 04/
├── ex0/
│   └── ft_ancient_text.py         # Read from a storage vault (file)
├── ex1/
│   └── ft_archive_creation.py     # Write a new archive file
├── ex2/
│   └── ft_stream_management.py    # stdin / stdout / stderr channels
├── ex3/
│   └── ft_vault_security.py       # Context managers (with statement)
├── ex4/
│   └── ft_crisis_response.py      # try/except + context managers
├── data_generator.py              # Generates required test data files
├── main.py                        # Integration script exercising all 5 exercises
├── sample_data.json               # Reference JSON metadata
├── README.md                      # This file
└── en.subject.pdf                 # Original project subject
```

Each exercise folder also holds the `.txt` data files produced by
`data_generator.py` (e.g. `ancient_fragment.txt`, `classified_data.txt`,
`security_protocols.txt`, `standard_archive.txt`) — see **Usage** below for
how to (re)generate them.

---

## 🚀 Usage

### 1. Generate the required test data

The exercises read from files that don't ship pre-made — they must be
generated first with `data_generator.py`:

```bash
# For ex0 (creates ancient_fragment.txt)
cd ex0 && python3 ../data_generator.py

# For ex3 (creates classified_data.txt, security_protocols.txt)
cd ex3 && python3 ../data_generator.py

# For ex4 (creates standard_archive.txt; also set up a permission-denied file)
cd ex4 && python3 ../data_generator.py
echo "CLASSIFIED" > classified_vault.txt && chmod 000 classified_vault.txt
```

`data_generator.py` writes several template files at once (ancient fragment,
classified data, security protocols, standard archive, a corrupted archive,
and a `sample_data.json`), so running it once per exercise directory covers
everything that exercise needs.

### 2. Run each exercise individually

```bash
python3 ex0/ft_ancient_text.py
python3 ex1/ft_archive_creation.py
python3 ex2/ft_stream_management.py          # interactive: prompts for input
python3 ex3/ft_vault_security.py
python3 ex4/ft_crisis_response.py
```

Exercise 2 reads from `stdin`, so it can also be fed non-interactively:

```bash
echo -e "ARCH_7742\nAll systems nominal" | python3 ex2/ft_stream_management.py
```

### 3. Check code quality

```bash
flake8 ex0/ ex1/ ex2/ ex3/ ex4/
```

---

## 📚 Exercises

### Exercise 0 — Ancient Text Recovery
**File**: `ex0/ft_ancient_text.py`
**Goal**: Read the full contents of a file using the most basic `open`/`read`/
`close` pattern.

- `recover_ancient_text()` opens `ancient_fragment.txt` in default `'r'` mode,
  reads the entire content with `read()`, then closes the handle manually.
- The `__main__` guard wraps the call in `try/except FileNotFoundError` to
  print a clean message instead of letting the traceback surface.

### Exercise 1 — Archive Creation
**File**: `ex1/ft_archive_creation.py`
**Goal**: Write a brand-new file from scratch.

- `create_archive()` opens `new_discovery.txt` in `'w'` mode (creates or
  overwrites), writes three labelled entries followed by `\n`, then closes
  the handle.
- No error handling is implemented here — write failures on a fresh file are
  not part of the exercise's scope.

### Exercise 2 — Stream Management
**File**: `ex2/ft_stream_management.py`
**Goal**: Demonstrate the three standard data channels.

- `manage_streams()` reads an archivist ID and a status report via `input()`
  (which pulls from `stdin`).
- Normal status output is written with `sys.stdout.write()`; a diagnostic
  alert is written separately with `sys.stderr.write()`.
- Keeping the two output channels distinct means output redirection
  (`> file`) and error redirection (`2> file`) can be handled independently.

### Exercise 3 — Vault Security
**File**: `ex3/ft_vault_security.py`
**Goal**: Replace manual `open()`/`close()` pairs with context managers.

- `secure_extraction()` reads `classified_data.txt` via `with open(...) as
  vault:`.
- `secure_preservation()` writes `security_protocols.txt` the same way.
- `vault_security_protocol()` ties both together into one demo run.
- Every function carries full type hints (`filename: str -> None`, etc.).
- The `with` block guarantees the file is closed on exit, even if an
  exception were raised while reading or writing.

### Exercise 4 — Crisis Response
**File**: `ex4/ft_crisis_response.py`
**Goal**: Combine context managers with layered exception handling.

- `crisis_handler()` wraps a `with open(...) as vault:` block inside a
  `try/except` that catches, in order: `FileNotFoundError`, `PermissionError`,
  then a generic `Exception` fallback.
- The success/failure label (`ROUTINE ACCESS` vs `CRISIS ALERT`) is decided
  **after** the attempt completes, based on which branch actually ran —
  not assumed beforehand.
- `run_crisis_response()` drives `crisis_handler()` across three scenarios:
  a missing file, a permission-denied file, and a normal successful read.

---

## 🧠 Key Concepts

### File Modes
| Mode | Meaning |
|------|---------|
| `'r'` | Read (default) — file must exist |
| `'w'` | Write — creates or **overwrites** |
| `'a'` | Append — creates or adds to end |

### The Three Streams
- **stdin** (`sys.stdin` / `input()`) — receive data from the user or another process
- **stdout** (`sys.stdout` / `print()`) — normal program output
- **stderr** (`sys.stderr`) — error and alert messages; separate from stdout

### Context Managers (`with`)
```python
with open("file.txt", 'r') as f:
    data = f.read()
# file is automatically closed here, even if an exception occurred
```
This is equivalent to a manual `try/finally` that calls `f.close()` in the
`finally` block — `with` just delegates that cleanup to the file object's
`__exit__` method, so it happens automatically and can't be forgotten.

### Exception Hierarchy for File Operations
```
Exception
└── OSError
    ├── FileNotFoundError   # file does not exist
    └── PermissionError     # access denied
```

---

## 🧪 Testing

This module has no automated `pytest`/`unittest` suite. Correctness is
verified manually in two ways:

1. **Per-exercise runs** — execute each script directly (see **Usage**) and
   check the printed output against the expected behaviour described in
   **Exercises** above (e.g. that ex0 prints recovered lines, that ex4 labels
   failures as `CRISIS ALERT` and successes as `ROUTINE ACCESS`).
2. **`main.py` integration run** — `python3 main.py` imports all five
   exercise modules and drives them through several scenarios each
   (existing file, missing file, permission-denied file, mocked `stdin`,
   temporary files that are created and cleaned up afterwards). A full,
   uninterrupted run through all five sections without unhandled tracebacks
   is the practical definition of "passing" for this module.

`main.py` must be run from the module's root directory (not from inside an
`exN/` folder) since it resolves data files relative to the current working
directory.

---

## ✅ Code Style & Requirements

- Python 3.10+ syntax throughout.
- `flake8` must pass with zero warnings on `ex0/`–`ex4/`.
- All functions carry type hints on parameters and return values.
- `sys` is the only standard-library import needed outside of `ex2`
  (used there for `sys.stdin`/`sys.stdout`/`sys.stderr`); no third-party
  dependencies are used anywhere in the module.
- Exercise 3 and Exercise 4 must use the `with` statement for file access;
  Exercise 4 must additionally use `try/except` covering
  `FileNotFoundError`, `PermissionError`, and a generic `Exception`.

---

## 🛡️ Defense Notes

- **Why `close()` matters**: leaving file handles open leaks OS-level
  resources and, in the worst case, can leave writes unflushed if the
  process ends abruptly — this is exactly the problem `with` was designed
  to eliminate in later exercises.
- **`'w'` mode truncates immediately**: opening a file in `'w'` mode erases
  its existing content the moment `open()` is called, before any `write()`
  happens — a common source of "I lost my data" surprises if the wrong mode
  is used by mistake.
- **Why catch specific exceptions before the generic one**: ordering
  `FileNotFoundError` and `PermissionError` ahead of a bare `except
  Exception` gives more actionable feedback; if the generic handler came
  first (or was the only one), it would silently swallow the real cause of
  a failure.
- **stdout vs stderr under redirection**: `python3 script.py > out.txt` only
  redirects `stdout` — `stderr` still prints to the terminal. This is why
  ex2 deliberately separates "standard" and "alert" messages onto different
  streams, and it's also why `2> errors.txt` is needed to redirect errors
  specifically.
- **What a `with` block actually does under the hood**: it's sugar for a
  `try/finally` where `__exit__` (here, closing the file) runs in the
  `finally`, so cleanup happens whether the block exits normally or via an
  exception — this is Python's version of RAII (Resource Acquisition Is
  Initialization).
- **Binary mode**: the same `open()`/`with` patterns used here extend to
  binary data by opening in `'rb'`/`'wb'` mode, in which case the file
  object works with `bytes` instead of `str`.

---

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
