<img width="2000" height="500" alt="Libft_cover" src="cover.png" />

<div align="center">

# 📚 M0 – Libft

![42 Libft](https://img.shields.io/badge/Porto-Libft-00babc?style=for-the-badge&logo=42&logoColor=white&labelColor=000000)
<br/>
<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" style="margin-right:6px"/>
<img src="https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white" style="margin-right:6px"/>

<p align="center">
  <img width="141" height="150" alt="Libft_bonus_max" src="badge.png" />
</p>

This project is part of the **42cursus** at 42 Porto.  
The goal is to re‑implement a subset of the C standard library, plus some extra utility functions, and to build a static library (`libft.a`) that can be reused in later projects.

</div>

---

## 🎯 Objectives

- Re‑implement commonly used C standard library functions.
- Learn how to organize code into a reusable static library.
- Practice memory management, pointer manipulation, and edge‑case handling.
- Provide clean, Norm-compliant C code.

---

## 🧱 Project structure

```text
Libft/
├── tester/              # Custom Libft tester (separate project, see tester/README.md)
├── Makefile             # Builds libft.a
├── README.md            # This file
├── en.subject.pdf       # Libft subject
├── ft_*.c               # All libft function implementations
└── libft.h              # Main header with all function prototypes
```

---

## 📝 Implemented functions

### 🔡 Character checks & transforms

- `ft_isalpha`: Returns non‑zero if the character is an alphabetic letter (A–Z or a–z)
- `ft_isdigit`: Returns non‑zero if the character is a digit ('0'–'9')  
- `ft_isalnum`: Returns non‑zero if the character is alphanumeric (letter or digit)  
- `ft_isascii`: Returns non‑zero if the value is a valid 7‑bit ASCII code (0–127)  
- `ft_isprint`: Returns non‑zero if the character is printable (space through '~')  
- `ft_toupper`: Converts a lowercase letter to uppercase; returns the argument unchanged otherwise  
- `ft_tolower`: Converts an uppercase letter to lowercase; returns the argument unchanged otherwise  

### 🧵 String functions

- `ft_strlen`: Returns the number of characters before the terminating NUL in a string  
- `ft_strchr`: Returns a pointer to the first occurrence of a character in a string (or NUL terminator pointer if searching for '\0')  
- `ft_strrchr`: Returns a pointer to the last occurrence of a character in a string (or NULL if not found)  
- `ft_strncmp`: Compares up to n characters of two strings and returns <0, 0 or >0 like `strncmp`  
- `ft_strnstr`: Searches for a substring limited to the first `len` bytes of the haystack; returns pointer to match or NULL  
- `ft_strlcpy`: Safely copies a C string into a sized buffer, guaranteeing NUL-termination when dstsize > 0; returns length of source  
- `ft_strlcat`: Safely appends a string to a sized buffer, guaranteeing NUL-termination when space allows; returns initial dst length + src length 
- `ft_strdup`: Allocates and returns a fresh duplicate of the given string (caller must free)  
- `ft_substr`: Allocates and returns a substring from `s` starting at `start` of maximum `len` characters (caller must free)  
- `ft_strjoin`: Allocates and returns a new string which is the concatenation of `s1` and `s2` (caller must free)  
- `ft_strtrim`: Allocates and returns a copy of `s1` with characters in `set` trimmed from start and end (caller must free)  
- `ft_split`: Splits a string by a delimiter into a NULL‑terminated array of strings; each element and the array are dynamically allocated (caller must free all)  
- `ft_strmapi`: Allocates and returns a new string resulting from applying a function to each character of `s` (caller must free)  
- `ft_striteri`: Iterates over a string passing index and char * to a function allowing in‑place modification (no allocation)  

### 💾 Memory functions

- `ft_memset`: Fills `len` bytes at `b` with the byte value `c` and returns `b` (no allocation)  
- `ft_bzero`: Sets `n` bytes to zero at `s` (convenience wrapper over memset)  
- `ft_memcpy`: Copies `n` bytes from `src` to `dst`. Assumes non‑overlapping regions (use memmove for overlap)  
- `ft_memmove`: Copies `len` bytes from `src` to `dst` safely handling overlapping areas (no allocation)  
- `ft_memchr`: Searches the first `n` bytes of memory for byte `c`; returns pointer to match or NULL  
- `ft_memcmp`: Compares first `n` bytes of two memory areas returning <0, 0 or >0 like `memcmp`  
- `ft_calloc`: Allocates `count * size` bytes and zeroes them; returns pointer or NULL on failure (caller must free)  

### 🔁 Conversions

- `ft_atoi`: Parses an integer from a string, skipping whitespace and accepting an optional sign; stops at first non‑digit  
- `ft_itoa`: Converts an integer `n` to its string representation, allocates the returned string (handles negatives safely); caller must free  

### 🖨️ File‑descriptor output

- `ft_putchar_fd`: Writes a single character to the given file descriptor  
- `ft_putstr_fd`: Writes a string to the given file descriptor (no trailing newline)  
- `ft_putendl_fd`: Writes a string followed by a newline to the given file descriptor  
- `ft_putnbr_fd`: Writes the decimal representation of an integer to the given file descriptor (handles negative numbers)  

### ➕ Bonus – Linked list API

Uses the following structure:

```c
typedef struct s_list
{
    void            *content;
    struct s_list   *next;
}   t_list;
```

- `ft_lstnew`: Allocates a new list node with `content` pointer set (node allocated; content ownership unchanged)  
- `ft_lstadd_front`: Inserts the node `new` at the beginning of the list (no allocation)  
- `ft_lstsize`: Returns the number of nodes in the list (no allocation)  
- `ft_lstlast`: Returns the last node of the list or NULL if list is empty (no allocation)  
- `ft_lstadd_back`: Adds the node `new` to the end of the list (no allocation)  
- `ft_lstdelone`: Deletes a single node: calls `del` on `lst->content` (if provided) then frees the node memory  
- `ft_lstclear`: Deletes and frees the entire list: uses `del` on each content, frees nodes and sets head to NULL  
- `ft_lstiter`: Iterates the list applying function `f` to each node's content (no allocation)  
- `ft_lstmap`: Maps the list into a new list by applying `f` to each content. On allocation failure cleans up already created nodes using `del` (new list nodes and contents are allocated by `f` or `ft_lstnew` — caller must free the returned list)  

---

## 🛠️ Building the library

From inside `Libft/`:

```bash
# build mandatory part
make

# build with bonus (linked list) functions
make bonus

# remove object files
make clean

# remove objects + libft.a
make fclean

# full rebuild
make re
```

This produces:

```text
libft.a   # static library containing all compiled functions
```

---

## 📦 Using Libft in another project

1. Copy `libft.a` and `libft.h` into your project, or add this directory as a submodule/subfolder.
2. Include the header in your source files:

```c
#include "libft.h"
```

3. Link the library when compiling:

```bash
# Example: libft in current directory
cc -Wall -Wextra -Werror main.c -L. -lft -o my_program

# Example: libft in path/to/Libft
cc -Wall -Wextra -Werror main.c -L"/path/to/Libft" -I"/path/to/Libft" -lft -o my_program
```

---

## 🧪 Testing

There is a dedicated tester in:

```text
Libft/tester/
```

It runs functional tests and Valgrind checks on all libft functions.  
See [`tester/README.md`](tester/README.md) for usage instructions.

---

## ✅ Code style & requirements

- Follows **42 Norm**.
- Compiled with:

```bash
cc -Wall -Wextra -Werror
```

- No forbidden functions beyond project subject.
- All dynamically allocated memory must be properly freed by the caller.

---

## 🛡️ Defense Notes

- **Why does `ft_strlcpy`/`ft_strlcat` return the size they *tried* to produce, not what they actually wrote?** This matches real BSD `strlcpy`/`strlcat` semantics: the return value lets the caller detect truncation by comparing it against `dstsize` (`if (ft_strlcpy(dst, src, sizeof(dst)) >= sizeof(dst))` means truncation occurred). Here `ft_strlcpy` always returns `ft_strlen(src)` regardless of `dstsize`, and `ft_strlcat` returns `dst_len + src_len` (the "would-be" total length) even when it copies fewer bytes — including the early-return case where `dstsize <= dst_len`, where it returns `dstsize + src_len` per the real `strlcat` spec for a dst that isn't even NUL-terminated within `dstsize`.
- **`ft_memcpy` vs `ft_memmove`**: `ft_memcpy` copies forward byte-by-byte with no overlap check at all — if source and destination overlap, behavior is undefined, matching real `memcpy`. `ft_memmove` explicitly compares pointers (`d < s` copies forward, `d > s` copies backward from the end) so that overlapping regions are copied without one region's data getting overwritten before it's read. Be ready to explain *why* the direction matters: if `dst` is ahead of `src` and you copied forward, you'd overwrite source bytes before reading them.
- **`ft_split`'s cleanup on partial failure**: if a `ft_substr` call fails partway through building the array, `ft_split` calls `free_split(result, i)` where `i` is the index that just failed — this frees indices `0..i-1` (the previously-succeeded allocations) plus the array itself, then returns `NULL`. The failed slot itself was never assigned, so it's correctly excluded from the free loop. This is the standard "free what you've built so far" pattern evaluators probe for.
- **NULL handling — crash vs. graceful**: `ft_strdup(NULL)` will segfault here, because it calls `ft_strlen(s1)` unconditionally with no NULL guard — this matches real glibc `strdup`, which also has undefined behavior (typically a crash) on NULL. `ft_split(NULL, c)` and `ft_substr(NULL, ...)` do guard explicitly (`if (!s) return (NULL)`), so know which functions in this implementation defend against NULL and which intentionally mirror libc's "your problem" contract — this asymmetry is a natural evaluator question.
- **Bonus: `ft_lstdelone` ordering.** It calls `del(lst->content)` *before* `free(lst)`, and never touches `lst->next` after freeing — `ft_lstclear` saves `(*lst)->next` into a `temp` variable *before* calling `ft_lstdelone`, precisely to avoid reading a freed node's `next` pointer. Getting this order backwards (freeing the node first, or reading `->next` after `ft_lstdelone`) is the single most common bonus bug.
- **Bonus: `ft_lstmap`'s cleanup on failure.** If `ft_lstnew` fails for a node built partway through the list, the code calls `del(new_content)` on the content that was just created (so it isn't leaked) and then `ft_lstclear(&new_list, del)` to free every node already appended to the new list. One real gotcha to flag to an evaluator: this direct `del(new_content)` call is *not* NULL-checked, unlike `ft_lstdelone`'s internal `if (del)` guard — passing `del == NULL` to `ft_lstmap` works fine on the happy path but will crash if a `ft_lstnew` allocation fails mid-list. Worth knowing as a known edge case even though the subject assumes `del` is always provided.
- **Why every allocating function needs a Valgrind pass, not just a manual read-through**: `ft_split`, `ft_substr`, `ft_strjoin`, `ft_strtrim`, `ft_itoa`, `ft_strdup`, `ft_calloc`, and the bonus list functions all `malloc`. "0 leaks, 0 errors" from Valgrind confirms every reachable allocation was freed on both the success and failure paths that were actually exercised by the tests — it does **not** verify that a function returns the *correct* value, that `ft_strlcat`'s size math is off-by-one-free, or that an untested error path (e.g. a `malloc` failure deep in `ft_split`) is actually leak-free. Valgrind only reports on code paths your test suite actually triggers.
- **`ft_calloc`'s overflow guard**: `total_size = count * size` can silently wrap around on huge inputs before the multiplication is checked; the guard `if (size && (total_size / size != count)) return (NULL)` catches overflow by dividing back and comparing, but only detects it *after* the (already-overflowed) multiplication happened — this is the standard way to check for multiplication overflow in C without wider integer types, and evaluators sometimes ask "why divide back instead of comparing sizes directly."
- **42 Norm shapes the code even where it hurts idiomatic C**: no more than one variable declaration per line and one statement per line, no `for` loops (only `while`), no ternary operator, no multiple assignments in a single expression, functions capped at ~25 lines, and at most 4 (mandatory part) or 5 (bonus) function arguments. This is why `ft_split` and `ft_itoa` split logic into small `static` helper functions (`count_words`, `word_len`, `count_digits`) instead of inlining — Norm's line/complexity limits force decomposition that wouldn't otherwise be necessary in plain C.
- **`ft_atoi`'s whitespace skipping**: it skips `' '` and characters in the `9`–`13` range (`\t\n\v\f\r`) matching `isspace`, before checking for a single optional `+`/`-` sign. Be ready to explain why only one sign character is consumed (real `atoi` also only consumes one) and that overflow beyond `INT_MAX`/`INT_MIN` is undefined behavior here just as in the real function — this implementation does not clamp or detect it.

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
                <img src="https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white" alt="Git">
                <img src="https://img.shields.io/badge/-Shell-4EAA25?logo=gnu-bash&logoColor=white" alt="Shell">
            </td>
        </tr>
    </tbody>
</table>

</div>

---

## 📝 License & credits

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
