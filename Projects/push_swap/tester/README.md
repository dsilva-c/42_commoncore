<div align="center">

# 🧪 push_swap Tester

![42 push_swap Tester](https://img.shields.io/badge/Porto-push_swap_Tester-00babc?style=for-the-badge&logo=42&logoColor=white&labelColor=000000)
<br/>
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white)
![Valgrind](https://img.shields.io/badge/Valgrind-2E3C45?style=for-the-badge&logo=valgrind&logoColor=white)

A comprehensive test suite for the **push_swap** project (Mandatory + Bonus).  
This tester verifies sorting correctness, error handling, performance benchmarks, and the bonus checker program.

</div>

> ⚠️ **Important:** This tester is **not standalone**. It requires the `push_swap` and `checker` binaries built from the parent directory.

---

## 📌 What this tester does?

- Runs grouped tests for:
  - **Identity Tests:** Already sorted inputs (should produce no output).
  - **Small Sort Tests:** 2, 3, and 5 element sorting with move count verification.
  - **Error Handling:** Duplicates, non-numeric input, overflow/underflow, invalid signs.
  - **Performance (100 elements):** 5 random runs, verifies < 700 moves and correct sorting.
  - **Performance (500 elements):** 5 random runs, verifies < 5500 moves and correct sorting.
  - **Bonus Checker:** Tests the checker program with correct sorts, wrong ops, invalid commands.
- Prints nicely formatted, colorized output with PASS/FAIL status.
- Provides a final summary with total tests, passed, failed, and success rate.

---

## 📂 Folder structure

```text
tester/
├── Makefile              # builds the tester executable
├── tester.h              # tester header (colors, prototypes, results struct)
├── tester.c              # main entry point, binary check, test orchestration
├── tester_print.c        # color-coded header and test result printing
├── tester_print2.c       # summary printing (success rate, final message)
├── tester_utils.c        # utility functions (move count, verify sort, gen args)
├── tester_tests.c        # identity, small sort, and error handling tests
├── tester_tests2.c       # performance tests (100 and 500 elements)
├── tester_bonus.c        # bonus checker tests (OK, KO, Error scenarios)
└── README.md             # this file
```

---

## ⚙️ Setup (required before building)

This tester expects the push_swap project folder structure:

- `.../push_swap/`        ← Project root (contains `Makefile`, source files)
- `.../push_swap/tester/` ← This tester folder

The tester's `Makefile` automatically calls `make` and `make bonus` in the parent directory to ensure `push_swap` and `checker` are up-to-date before running.

### Minimal checklist

- Ensure the project source files are in the parent directory.
- The tester will build everything for you when you run `make run`.

---

## 🚀 Build & run

Run these commands from inside the `tester/` directory.

### 1️⃣ Build and run all tests (recommended)
Automatically builds `push_swap` and `checker`, then runs the full test suite.

```bash
make run
```

### 2️⃣ Build the tester only
If you've already built `push_swap` and `checker` yourself:

```bash
make
./tester
```

### 3️⃣ What to expect

- Colorized output grouped by test category
- A final summary with:
  - total tests
  - passed / failed
  - success rate
- Exit codes:
  - `0` if all tests passed
  - `1` if one or more tests failed

---

## 🧪 Memory checking with Valgrind

The Makefile provides a ready-to-use target to check for memory leaks in `push_swap`.

```bash
make leaks
```

This runs Valgrind on `push_swap` with both multi-argument and string-argument input formats.  
Valgrind should report **0 leaks** and **0 errors**.

---

## 🧾 Tester expectations

The tests assume that:

- **Norm Compliance:** Your project follows the 42 Norm (all files pass `norminette`).
- **Behavior:**
  - `push_swap` outputs operations to stdout (one per line).
  - No output is produced when the stack is already sorted.
  - `Error\n` is written to stderr for invalid inputs.
  - `checker` reads operations from stdin and prints `OK`, `KO`, or `Error`.
- **Performance:**
  - 100 random elements sorted in < 700 moves (for max grade).
  - 500 random elements sorted in < 5500 moves (for max grade).
- **Memory:**
  - All dynamically allocated memory is properly freed (0 leaks under Valgrind).

---

## 🛠️ Tech stack

<div align="center">

<table width="100%">
    <thead>
        <tr>
            <th width="80%">Category</th>
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

- **`../push_swap not found!`**  
  ➜ Ensure the tester is inside the `push_swap/tester/` folder and run `make run` (it builds automatically).

- **`../checker not found` (bonus tests skipped)**  
  ➜ Run `make bonus` in the parent directory, or use `make run` which does it for you.

- **Performance tests failing (too many moves)**  
  ➜ Review your cost analysis in `init_a_to_b.c`. Ensure simultaneous rotations (`rr`/`rrr`) use `max(cost_a, cost_b)` instead of `cost_a + cost_b`.

- **`valgrind: command not found`**  
  ➜ Install Valgrind:
  ```bash
  # Debian/Ubuntu
  sudo apt install valgrind

  # macOS (Homebrew; availability may vary)
  brew install valgrind
  ```

---

Happy debugging! 🚀
