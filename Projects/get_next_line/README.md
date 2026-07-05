<img width="2000" height="500" alt="get_next_line_cover" src="cover.png" />

<div align="center">

# 📄 M1 – get_next_line

![42 get_next_line](https://img.shields.io/badge/Porto-get__next__line-00babc?style=for-the-badge&logo=42&logoColor=white&labelColor=000000)
<br/>
<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" style="margin-right:6px"/>
<img src="https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white" style="margin-right:6px"/>

<p align="center">
  <img width="141" height="150" alt="get_next_line_bonus_max" src="badge.png" />
</p>

This project is part of the **42cursus** at 42 Porto.  
The goal is to program a function that returns a line read from a file descriptor. This project introduces the concept of **static variables** in C and adds a highly useful function to your toolkit for future projects.

</div>

---

## 🎯 Objectives

- Learn how to manipulate **static variables** (persisting data between function calls).
- Understand **file descriptors** and standard input/output operations.
- Practice stack vs. heap memory management and prevent memory leaks.
- Create a reusable function that works across different buffer sizes and file types.
- Provide clean, Norm-compliant C code.

---

## 🧱 Project structure

```text
get_next_line/
├── tester/                      # Custom gnl tester (separate project, see tester/README.md)
├── Makefile                     # Compilation rules
├── README.md                    # this file
├── en.subject.pdf               # get_next_line subject
├── get_next_line.c              # Main logic (reading loop)
├── get_next_line.h              # Header for mandatory part
├── get_next_line_bonus.c        # Bonus logic (multi-fd support)
├── get_next_line_bonus.h        # Header for bonus part
├── get_next_line_utils.c        # Helper functions (strjoin, strlen, etc.)
└── get_next_line_utils_bonus.c  # Bonus helpers
```

---

## 📝 The function

### 📖 Mandatory part

`char *get_next_line(int fd);`

<div align="center">

| Parameter | Description |
| :--- | :--- |
| `fd` | The file descriptor to read from. |

</div>

- **Return Value:** Read line: correct behavior; `NULL`: there is nothing else to read, or an error occurred.
- **Description:** Reads from a file descriptor (`fd`) and returns the next line, including the newline character (`\n`) if present.

### 🌟 Bonus part

- **Single Static Variable**: The logic is implemented using only one static variable per file descriptor, ensuring minimal memory footprint.
- **Multiple File Descriptors**: Can manage multiple file descriptors simultaneously (e.g., reading from `fd 3`, then `fd 4`, then back to `fd 3`) without losing the reading state of any file.

### 🔧 Utilities (internal)

- `ft_strlen`: Calculates the length of a string.
- `ft_strchr`: Locates the first occurrence of a character (specifically `\n`) in a string.
- `ft_strjoin`: Concatenates the static buffer with the newly read buffer.
- `ft_extract_line`: Isolates the line to be returned from the buffer.
- `ft_update_buffer`: Updates the static variable to keep the remaining text after the newline.

---

## 🛠️ Building the project

This project includes a Makefile for convenience, though the subject strictly asks for source files.

```bash
# build mandatory part
make

# build with bonus functions
make bonus

# remove object files
make clean

# remove objects + library
make fclean

# full rebuild
make re
```

This produces `get_next_line.a` (if compiled as a library) or object files ready for linking.

---

## 📦 Using gnl in another project

1. Copy the source files and header into your project (or include this folder).
2. Include the header in your source files:

```c
#include "get_next_line.h"
```

3. Compile your code with the GNL sources. **Crucial:** You must define the `BUFFER_SIZE` flag:

```bash
# Example: compiling main.c with GNL
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 main.c get_next_line.c get_next_line_utils.c -o my_gnl_program
```

> [!NOTE]
> You can change `BUFFER_SIZE` to any value (e.g., `1`, `42`, `9999`, `10000000`) to test robustness.

---

## 🧪 Testing

There is a dedicated tester in:

```text
get_next_line/tester/
```

It runs functional tests, checks edge cases (empty files, no newlines), and performs Valgrind checks for memory leaks.  
See [`tester/README.md`](tester/README.md) for usage instructions.

---

## ✅ Code style & requirements

- Follows **42 Norm**.
- Compiled with:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=xx
```

- **No Libft:** You are not allowed to use your existing Libft library. All helper functions must be implemented directly in the project files.
- No forbidden functions (`lseek`, `fseek`, etc.).
- All dynamically allocated memory must be properly freed by the caller.
- **Heap Allocation:** The buffer is allocated on the heap (using `malloc`) to prevent stack overflow when using very large `BUFFER_SIZE` values.

---

## 🛡️ Defense Notes

- **Why `static`?** A single `read()` call has no notion of "line" — it returns whatever bytes happen to be sitting in the kernel buffer, which can be less than one line (a line split across two reads) or more than one line's worth (several `\n`-terminated lines plus a partial one in the same chunk). `static char *buffer;` in `get_next_line.c` is what survives between calls: it holds everything already read but not yet returned. Without it, every call would start from a fresh empty string and any leftover data read past the first `\n` would simply be lost.
- **How "complete" is defined:** after every `read()`, `ft_read_file` calls `ft_strchr(buffer, '\n')` and stops reading only once a `\n` is found (or `read` returns `0`/`-1`). Extraction itself (`ft_extract_line`) does its own manual scan (`while (buffer[i] && buffer[i] != '\n') i++;`), so the "is this a line yet" check and the "where does the line end" check are two separate manual/`ft_strchr` scans over the same buffer — be ready to point at both.
- **BUFFER_SIZE = 1 vs. huge:** the read loop (`ft_read_file`) doesn't care about the size — it just keeps calling `read(fd, buf, BUFFER_SIZE)` and appending via `ft_strjoin` until it sees a `\n` or hits EOF. With `BUFFER_SIZE=1`, this means one `read()` syscall per byte, appended one byte at a time — correct but slow. With a `BUFFER_SIZE` larger than the whole file, a single `read()` can return the entire file content (or several lines) at once; the extra lines aren't lost because `ft_update_buffer` splits off everything after the first `\n` and stores it back into the static `buffer` for the *next* call, so no second `read()` is needed until that leftover is exhausted.
- **EOF vs. error — not distinguished.** On `read() == -1`, `ft_read_file` frees the current buffer and returns `NULL`; back in `get_next_line`, that `NULL` buffer is freed again (a no-op, `free(NULL)` is safe) and the static pointer is reset to `NULL`, then the function returns `NULL` — exactly the same code path and return value as true EOF with no data left. This implementation does **not** distinguish a read error from "nothing left to read": both surface identically as `NULL` to the caller. If an evaluator asks "how would I tell the two apart from outside," the honest answer is: you can't, from the return value alone.
- **Static buffer lifecycle at EOF.** When the last read returns `0` and there's no leftover data (`buffer[0] == '\0'`), `get_next_line` frees `buffer` and sets the static pointer back to `NULL` before returning. Same thing happens one call earlier for a final line with no trailing `\n`: `ft_update_buffer` finds no `\n` in what's left, frees the buffer and returns `NULL`, so the static pointer is `NULL` again after that last line is handed back. This matters because it means calling `get_next_line` again on the same fd after it already returned `NULL` is safe — the static starts clean (`malloc`'s a fresh one-byte buffer) rather than reusing a stale/dangling pointer. It will just immediately hit EOF again and return `NULL`.
- **Bonus mechanism: array of buffers indexed by fd, not a linked list.** `get_next_line_bonus.c` declares `static char *bufs[FD_MAX];` (with `FD_MAX` defaulting to 1024 in the bonus header) and indexes it directly with `bufs[fd]`. There's a bounds check (`fd >= FD_MAX` returns `NULL`), but no dynamic lookup structure — it's a flat array, one slot per possible fd value.
- **Why the mandatory single static breaks with multiple fds.** Trace: read fd 3 → partial line sits in the one `static char *buffer`. Read fd 4 → the same static variable is reused, so `ft_read_file` appends fd 4's bytes onto fd 3's leftover as if they were a continuation of the same stream — the two fds' data gets concatenated into one corrupted "line," and fd 3's partial line is gone. Read fd 3 again afterward → there is no fd-3 state left to resume from; the static buffer now contains a mix of fd-4 data. The bonus version avoids this because `bufs[3]` and `bufs[4]` are separate array slots — each fd's leftover persists independently, so interleaving fd 3 → fd 4 → fd 3 works correctly.
- **BUFFER_SIZE supply chain.** Both headers define `BUFFER_SIZE` only if not already defined (`# ifndef BUFFER_SIZE` / `# define BUFFER_SIZE 42`), so the project's own `Makefile` builds `get_next_line.a` with the default of 42 (it passes no `-D` flag). The subject's actual contract is that whoever links this into another project supplies `-D BUFFER_SIZE=xx` on the compiler invocation, and the code must work for *any* positive value without recompilation assumptions — which is why every buffer allocation in the source (`malloc(sizeof(char) * (BUFFER_SIZE + 1))`) uses the macro rather than a hardcoded number, and why `fd < 0 || BUFFER_SIZE <= 0` is checked defensively at the top of `get_next_line` rather than assuming a sane value was passed.
- **Heap, not stack, for the read buffer.** `buf` in `get_next_line` is `malloc`'d (`BUFFER_SIZE + 1` bytes) rather than declared as a local array, specifically so a huge `BUFFER_SIZE` (e.g. `10000000`) doesn't blow the stack — a detail worth mentioning if asked why the read buffer isn't just `char buf[BUFFER_SIZE + 1];`.

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
            </td>
        </tr>
    </tbody>
</table>

</div>

---

## 📝 License & credits

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
