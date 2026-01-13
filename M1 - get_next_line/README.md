<img width="2000" height="500" alt="get_next_line_cover" src="https://github.com/user-attachments/assets/66cbff91-70f2-40b6-938f-8e002afd6eeb" />

<div align="center">

# 📄 M1 – get_next_line

![42 get_next_line](https://img.shields.io/badge/Porto-get__next__line-00babc?style=for-the-badge&logo=42&logoColor=white&labelColor=000000)
<br/>
<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" style="margin-right:6px"/>
<img src="https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white" style="margin-right:6px"/>

<p align="center">
  <img width="141" height="150" alt="get_next_line_bonus_max" src="https://github.com/user-attachments/assets/21464c7a-686c-4272-9d07-d19d833afabe" />
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
M1 - get_next_line/
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

| Parameter | Description |
| :--- | :--- |
| `fd` | The file descriptor to read from. |

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

## 📦 Using GNL in another project

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
M1 - get_next_line/tester/
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

---

## 📈 Final grade

<img width="1101" height="117" alt="getnextline_grade" src="https://github.com/user-attachments/assets/6962df64-94ab-4390-bbb5-dc7ee8714f63" />
