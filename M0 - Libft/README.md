<img width="2000" height="1000" alt="cover-libft-bonus.png" src="https://raw.githubusercontent.com/ayogun/42-project-badges/refs/heads/main/covers/cover-libft-bonus.png" />

# 📚 M0 – Libft

<p align="center">
  <img src="https://github.com/leogaudin/42_project_badges/raw/main/badges/libft_bonus_max.webp" alt="libft_bonus_max.webp">
</p>

This project is part of the **42cursus** at 42 Porto.  
The goal is to re‑implement a subset of the C standard library, plus some extra utility functions, and to build a static library (`libft.a`) that you can reuse in later projects.

---

## 🎯 Objectives

- Re‑implement commonly used C standard library functions.
- Learn how to organize code into a reusable static library.
- Practice memory management, pointer manipulation, and edge‑case handling.
- Provide clean, Norm-compliant C code.

---

## 🧱 Project Structure

```text
M0 - Libft/
├── libft.h              # Main header with all function prototypes
├── Makefile             # Builds libft.a
├── ft_*.c               # All libft function implementations
└── tester/              # libft tester (separate project, see tester/README.md)
```

---

## 📝 Implemented Functions

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

## 📦 Using libft in another project

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

## 📈 Final grade

<img width="1101" height="117" alt="image" src="https://github.com/user-attachments/assets/3c048ce4-5f40-4b5f-8e5d-2fd8f32d4e87" />
