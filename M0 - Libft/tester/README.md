# 🧪 Libft Tester

A comprehensive test suite for the **Libft** project (35 mandatory + 9 bonus functions).  
This tester builds and runs unit-style tests and includes Makefile targets to run Valgrind for memory leak detection.

> ⚠️ **Important:** this tester is **not standalone**.  
> It requires your Libft implementation:
> - all `ft_*.c` files
> - `libft.h`  
> to be available to the tester (see **Setup**).

---

## 📌 What this tester does

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

You have two options:

### Option 1 – Copy libft files next to the tester (simple)

From inside `tester/`:

```bash
cp ../libft.h .
cp ../ft_*.c .
```

Adjust the path (`../`) if your libft is in a different location.

### Option 2 – Keep libft separate and adjust Makefile

- Leave your libft project where it is.
- Open `tester/Makefile`.
- Set `LIBFT_DIR` to point to your libft directory and make sure it either:
  - builds `libft.a` there and links against it, or
  - compiles the sources from that directory.

---

## 🚀 Build & run

From inside the `tester/` folder:

```bash
# build the tester executable
make

# run all tests
make run
# or directly:
./tester
```

The tester will:

- print a header
- run all test groups (character, string, memory, copy, allocation, additional, output, bonus)
- print a summary with:
  - total tests
  - passed
  - failed
  - success rate
  - final message (all passed or some failed)

Exit code:

- `0` if all tests passed
- `1` if one or more tests failed

---

## 🧪 Memory checking with Valgrind

The Makefile provides ready‑to‑use targets.

### 📝 Generate a Valgrind log

```bash
make valgrind-log
```

- Builds the tester (with normal `CFLAGS`)
- Runs it under Valgrind with:
  - `--leak-check=full`
  - `--show-leak-kinds=all`
  - `--track-origins=yes`
- Writes output to `valgrind.log`

View the log:

```bash
cat valgrind.log
```

### 🔍 Strict check (fail on leaks)

```bash
make valgrind-check
```

This will:

1. `make clean`
2. Rebuild with debug flags (`-g -O0`)
3. Run Valgrind with `--error-exitcode=1`  
   → If Valgrind reports leaks/errors, the command returns a non‑zero exit code.

After that, you can return to a normal (optimized) build with:

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

## 🐞 Troubleshooting

- **`libft.h: No such file or directory`**  
  ➜ Copy `libft.h` into this folder or update `LIBFT_DIR` in the Makefile.

- **Linker errors like `undefined reference to 'ft_strlen'`**  
  ➜ Ensure all `ft_*.c` files are either:
  - in this folder and compiled, or  
  - compiled into `libft.a` in `LIBFT_DIR` and linked by the tester Makefile.

- **`valgrind: command not found`**  
  ➜ Install Valgrind:
  ```bash
  # Debian/Ubuntu
  sudo apt install valgrind

  # Fedora
  sudo dnf install valgrind

  # macOS (Homebrew, may be limited depending on OS version)
  brew install valgrind
  ```

- **Some tests fail**  
  ➜ Read the printed test description and expected output; fix the corresponding Libft function and re-run:
  ```bash
  make re
  ./tester
  ```

---

Happy debugging and have fun breaking (and fixing) your libft! 🎉
