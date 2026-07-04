<div align="center">

# 🧪 get_next_line tester

![42 get_next_line Tester](https://img.shields.io/badge/Porto-get__next__line_Tester-00babc?style=for-the-badge&logo=42&logoColor=white&labelColor=000000)
<br/>
<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" style="margin-right:6px"/>
<img src="https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white" style="margin-right:6px"/>
<img src="https://img.shields.io/badge/Valgrind-2E3C45?style=for-the-badge&logo=valgrind&logoColor=white" style="margin-right:6px"/>

A comprehensive test suite for the **get_next_line** project (Mandatory + Bonus).  
This tester verifies file reading, standard input handling, buffer size robustness, and memory management.

</div>

> ⚠️ **Important:** This tester is **not standalone**. It requires your `get_next_line` source files in the parent directory.

---

## 📌 What this tester does?

- Runs grouped tests for:
  - **Basic Reading:** Single line, multiple lines, empty files.
  - **Edge Cases:** Files without newlines, large files (1000+ lines).
  - **Standard Input:** Piped input (`echo | ./tester`) and Manual input.
  - **Buffer Robustness:** Tests with `BUFFER_SIZE=1` (slow) and `BUFFER_SIZE=10000000` (heap check).
  - **Bonus:** Handling multiple file descriptors simultaneously (alternating reads).
- Prints nicely formatted, colorized output with PASS/FAIL status.
- Can be run under Valgrind to check for memory leaks.

---

## 📂 Folder structure

```text
tester/
├── Makefile                     # builds the tester executable
├── tester.h                     # tester header
├── tester.c                     # main entry point (mode selector)
├── tester_tests.c               # basic file tests (invalid fd, empty, etc.)
├── tester_tests2.c              # edge case tests (no newline, large files)
├── tester_tests3.c              # stdin tests (manual & automated)
├── tester_bonus.c               # bonus entry point
├── tester_bonus_tests.c         # bonus logic (multi-fd)
├── create_test_files.c          # helper to generate .txt files
├── test_files/                  # auto-generated text files
└── README.md                    # this file
```

---

## ⚙️ Setup (required before building)

This tester expects the gnl project folder structure:

- `.../M1 - get_next_line/`        ← Project root (contains `get_next_line.c`, `.h`, etc.)
- `.../M1 - get_next_line/tester/` ← This tester folder

The Makefile automatically looks for source files in `../`.  
Ensure your project files are named exactly: `get_next_line.c`, `get_next_line_utils.c`, `get_next_line.h` (and `_bonus` versions).

---

## 🚀 Build & run

Run these commands from inside the `tester/` directory.

### 1️⃣ Basic tests (mandatory)
Runs the standard file reading tests with the default `BUFFER_SIZE=42`.

```bash
make test
```

### 2️⃣ Standard input (pipes)
The subject strictly requires gnl to read from standard input. This command pipes a string into the tester to verify it.

```bash
make test_stdin
```

### 3️⃣ Buffer size variation
Test the robustness of your function against extreme buffer sizes.

```bash
# Slow reading (1 byte at a time)
make test_small

# Huge buffer (10MB - checks for stack overflow/heap usage)
make test_huge
```

### 4️⃣ Bonus tests
Checks strict alternation between multiple file descriptors (e.g., read fd3, then fd4, then fd3).

```bash
make bonus
```

### 5️⃣ Manual mode (interactive)
Want to type input yourself? Run this mode, type text, press **ENTER**, and use **Ctrl+D** to signal EOF.

```bash
./tester manual
```

---

## 🧪 Memory checking with Valgrind

The Makefile provides ready‑to‑use targets to check for leaks.

### 📝 Check mandatory
```bash
make leaks
```

### 🔍 Check bonus
```bash
make leaks_bonus
```

Valgrind should report **0 leaks** and **0 errors** when the tester finishes running.

---

## 🧾 Tester expectations

The tests assume that:

- **Norm Compliance:** Your project follows the 42 Norm (files are valid).
- **Behavior:**
  - `get_next_line` returns the line **including** the `\n` (unless EOF is reached without one).
  - Returns `NULL` when there is nothing left to read or on error.
- **Memory:**
  - The buffer is allocated on the heap (using `malloc`) to survive the `make test_huge` check.
  - All memory is freed before the function returns `NULL`.

---

## 🛠️ Tech stack

<div align="center">

<table width="100%">
    <thead>
        <tr>
            <th width="20%">Category</th>
            <th width="80%">Technologies</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center"><b>Core</b></td>
            <td>
                <img src="https://img.shields.io/badge/-C-A8B9CC?logo=c&logoColor=white" alt="C">
            </td>
        </tr>
        <tr>
            <td align="center"><b>Build System</b></td>
            <td>
                <img src="https://img.shields.io/badge/-Makefile-20639B?logo=gnu-make&logoColor=white" alt="Makefile">
            </td>
        </tr>
        <tr>
            <td align="center"><b>Tools</b></td>
            <td>
                <img src="https://img.shields.io/badge/-Valgrind-2E3C45" alt="Valgrind">
                <img src="https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white" alt="Git">
            </td>
        </tr>
    </tbody>
</table>

</div>

---

## 🐞 Troubleshooting

- **`get_next_line.h: No such file or directory`**
  ➜ Ensure the tester is inside the `M1 - get_next_line/tester/` folder.

- **Stack Overflow / Segfault on `make test_huge`**
  ➜ You are likely declaring `char buffer[BUFFER_SIZE]` on the stack. Switch to `malloc`.

- **`valgrind: command not found`**
  ➜ Install Valgrind (`sudo apt install valgrind` or `brew install valgrind`).

---

Happy debugging! 🚀
