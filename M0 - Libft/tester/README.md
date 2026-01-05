<div align="center">
  
# 🧪 Libft Tester

![42 Libft Tester](https://img.shields.io/badge/42-Libft_Tester-00babc?style=for-the-badge&logo=42)
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white)
![Valgrind](https://img.shields.io/badge/Valgrind-2E3C45?style=for-the-badge&logo=valgrind&logoColor=white)

A comprehensive test suite for the **Libft** project (35 mandatory + 9 bonus functions).  
This tester builds and runs unit-style tests and includes Makefile targets to run Valgrind for memory leak detection.

</div>

> ⚠️ **Important:** This tester is **not standalone**. It requires the Libft implementation.

---

## 📌 What this tester does?

- Runs grouped tests for:
  - character functions
  - string functions
  - memory functions
  - copy/concat (`strlcpy`, `strlcat`)
  - allocation & duplication (`calloc`, `strdup`, etc.)
  - advanced string functions (`substr`, `split`, `itoa`, `strmapi`, …)
  - output functions (`*_fd`)
  - bonus list functions
- Prints nicely formatted, colorized output with PASS/FAIL status.
- Can be run under Valgrind to check for:
  - leaks
  - invalid reads/writes
  - use of uninitialized memory

---

## 📂 Folder structure

```text
tester/
├── Makefile                     # builds the tester executable
├── tester.h                     # tester header
├── tester_utils_part1.c         # counters, result helpers
├── tester_utils_part2.c         # printing helpers, ft_upper_char
├── tester_utils_part3.c         # memory-check messaging, free_split, summary helpers
├── tester_utils_part4.c         # global counters access & summary
├── test_main.c                  # entry point, runs all test groups
├── test_character_part1.c       # isalpha, isdigit, isalnum, isascii, isprint
├── test_character_part2.c       # toupper, tolower
├── test_string_part1.c          # strlen, strchr, strrchr, strncmp, strnstr
├── test_string_part2.c          # strchr (not found), atoi
├── test_memory_part1.c          # memset, bzero, memcpy
├── test_memory_part2.c          # memmove, memchr, memcmp
├── test_memory_part3.c          # grouped memory tests
├── test_copy.c                  # strlcpy, strlcat
├── test_allocation.c            # calloc, strdup
├── test_additional_part1.c      # substr, strjoin, strtrim, split
├── test_additional_part2.c      # itoa, strmapi
├── test_additional_functions.c  # advanced group wrapper
├── test_output_part1.c          # putchar_fd, putstr_fd, putendl_fd
├── test_output_part2.c          # putnbr_fd variations
├── test_bonus_part1.c           # lstnew, lstadd_front
├── test_bonus_part2.c           # lstsize, lstlast, lstadd_back, lstiter
├── test_bonus_part3.c           # lstdelone, lstmap, lstclear
└── README.md                    # this file
```

---

## ⚙️ Setup (required before building)

This tester expects the Libft project folder:

- .../M0 - Libft/        ← Libft project root (contains `libft.h` and `libft.a` after building)  
- .../M0 - Libft/tester/ ← this tester folder

What the tester needs at build time:
- `libft.h` (header) available to the compiler via `-I$(LIBFT_DIR)`
- `libft.a` (static archive) available to the linker via `-L$(LIBFT_DIR) -lft`

Follow these steps:

1) Build Libft (once)
```bash
cd "/path/to/M0 - Libft"
make            # produces libft.a
```

2) Ensure `LIBFT_DIR` points to the `M0 - Libft` directory
- Either edit `tester/Makefile` and set:
  ```makefile
  LIBFT_DIR = "/path/to/M0 - Libft"
  ```
- Or plan to pass `LIBFT_DIR` on the `make` command line when building the tester (no Makefile edit required).

Minimal checklist
- Run `make` inside `M0 - Libft` to produce `libft.a`.
- Ensure `LIBFT_DIR` will point to the `M0 - Libft` path when you build the tester.

---

## 🚀 Build & run (tester)

After completing the Setup steps above, build and run the tester from the `tester/` directory.

Build the tester executable (single command)
```bash
# If LIBFT_DIR is set in the Makefile:
cd "/path/to/M0 - Libft/tester"
make

# Or pass LIBFT_DIR explicitly when invoking make:
cd "/path/to/M0 - Libft/tester"
make LIBFT_DIR = "/path/to/M0 - Libft"
```

Run tests
```bash
# run the tester executable
./tester

# or use the Makefile shortcut
make run
```

What to expect?
- Colorized output grouped by test category
- A final summary with:
  - total tests
  - passed
  - failed
  - success rate
- Exit codes:
  - `0` if all tests passed
  - `1` if one or more tests failed

Valgrind targets (examples)
```bash
# quick log (writes valgrind.log)
make valgrind-log

# strict check (fails on leaks)
make valgrind-check
```

---

## 🧪 Memory checking with Valgrind

The Makefile provides ready‑to‑use targets.

### 📝 Generate a Valgrind log
```bash
make valgrind-log
cat valgrind.log
```

### 🔍 Strict check (fail on leaks)
```bash
make valgrind-check
# returns non-zero if Valgrind finds leaks/errors
```

Restore normal build
```bash
make valgrind-check-rebuild
```

---

## 🧾 Allocation & free behavior (what the tester expects)

The tests assume that:

- Functions like `ft_strdup`, `ft_substr`, `ft_strjoin`, `ft_strtrim`, `ft_split`, `ft_itoa`, `ft_strmapi`, and `ft_calloc`:
  - allocate memory correctly,
  - return `NULL` on failure,
  - can be safely freed with `free()`.

- `ft_split`:
  - returns a NULL‑terminated array of strings,
  - each string and the array itself can be freed (the tester uses `free_split`).

- Linked list functions:
  - `ft_lstnew` allocates nodes,
  - `ft_lstdelone` and `ft_lstclear` free nodes and their contents correctly using the provided `del` function,
  - `ft_lstmap` cleans up properly on allocation failures (no leaks on partial map).

Valgrind should report **0 leaks** when:

- all tests pass, and  
- the tester finishes running.

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
                <img src="https://img.shields.io/badge/-Shell-4EAA25?logo=gnu-bash&logoColor=white" alt="Shell Script">
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

- **`libft.h: No such file or directory`**  
  ➜ Ensure `LIBFT_DIR` points to the folder that contains `libft.h`.

- **Linker errors like `undefined reference to 'ft_strlen'`**  
  ➜ Ensure `libft.a` exists in `LIBFT_DIR` and contains the expected symbols (`ar t libft.a`, `nm libft.a`).

- **`valgrind: command not found`**  
  ➜ Install Valgrind:
  ```bash
  # Debian/Ubuntu
  sudo apt install valgrind

  # Fedora
  sudo dnf install valgrind

  # macOS (Homebrew; availability may vary)
  brew install valgrind
  ```

- **Some tests fail**  
  ➜ Read the printed test description and expected output; fix the corresponding Libft function and re-run:
  ```bash
  make re
  ./tester
  ```

---

Happy debugging and have fun breaking (and fixing) your Libft! 🎉
