<img width="2000" height="500" alt="Libft_cover" src="https://github.com/user-attachments/assets/70798e46-3f78-478f-bcb2-1b7b147833fc" />

<div align="center">

# 📚 M0 – Libft

![42 Libft](https://img.shields.io/badge/42Porto-Libft-00babc?style=for-the-badge&logo=42)
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white)

<p align="center">
  <img width="141" height="150" alt="Libft_bonus_max" src="https://github.com/user-attachments/assets/bba11192-f193-4882-9ab0-9928e4a46f4f" />
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
M0 - Libft/
├── libft.h              # Main header with all function prototypes
├── Makefile             # Builds libft.a
├── ft_*.c               # All libft function implementations
├── tester/              # libft tester (separate project, see tester/README.md)
└── README.md            # this file
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

From inside `M0 - Libft/`:

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

# Example: libft in path/to/M0 - Libft
cc -Wall -Wextra -Werror main.c -L"/path/to/M0 - Libft" -I"/path/to/M0 - Libft" -lft -o my_program
```

---

## 🧪 Testing

There is a dedicated tester in:

```text
M0 - Libft/tester/
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

---

## 📈 Final grade

<img width="1101" height="117" alt="image" src="https://github.com/user-attachments/assets/3c048ce4-5f40-4b5f-8e5d-2fd8f32d4e87" />
