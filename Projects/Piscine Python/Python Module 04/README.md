# Module 04 - Data Archivist
## Digital Preservation in the Cyber Archives

### Python File Operations, Streams & Error Handling

---

## Project Overview

This module focuses on Python's core file I/O capabilities and resource
management. Through a sci-fi archival theme ("Cyber Archives 2087"), you'll
master reading and writing files, managing stdin/stdout/stderr streams, using
context managers, and handling exceptions gracefully.

**Python Version**: 3.10+
**Focus**: File Operations, Stream Management, Context Managers, Error Handling

---

## Project Structure

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
├── sample_data.json               # Reference JSON metadata
├── README.md                      # This file
└── en.subject.pdf                 # Original project subject
```

---

## Quick Start

### Generate Required Test Data
```bash
# For ex0 (creates ancient_fragment.txt)
cd ex0 && python3 ../data_generator.py

# For ex3 (creates classified_data.txt, security_protocols.txt)
cd ex3 && python3 ../data_generator.py

# For ex4 (creates standard_archive.txt; also set up permission test)
cd ex4 && python3 ../data_generator.py
echo "CLASSIFIED" > classified_vault.txt && chmod 000 classified_vault.txt
```

### Run Individual Exercises
```bash
python3 ex0/ft_ancient_text.py
python3 ex1/ft_archive_creation.py
python3 ex2/ft_stream_management.py          # interactive: prompts for input
python3 ex3/ft_vault_security.py
python3 ex4/ft_crisis_response.py
```

### Check Code Quality
```bash
flake8 ex0/ ex1/ ex2/ ex3/ ex4/
```

---

## Exercise Summaries

| # | File | Concepts | Key Tools |
|---|------|----------|-----------|
| 0 | `ft_ancient_text.py` | File reading | `open()`, `read()`, `close()` |
| 1 | `ft_archive_creation.py` | File writing | `open('w')`, `write()`, `close()` |
| 2 | `ft_stream_management.py` | Data streams | `sys.stdin`, `sys.stdout`, `sys.stderr` |
| 3 | `ft_vault_security.py` | Context managers | `with open(...) as f:` |
| 4 | `ft_crisis_response.py` | Error handling | `try/except`, `with`, multiple exception types |

---

## Key Concepts

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

### Exception Hierarchy for File Operations
```
Exception
└── OSError
    ├── FileNotFoundError   # file does not exist
    └── PermissionError     # access denied
```
