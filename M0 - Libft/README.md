# 📚 M0 – libft

<img src="https://github.com/leogaudin/42_project_badges/raw/main/badges/PROJECT_NAME.webp"/>

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

- `ft_isalpha`  
- `ft_isdigit`  
- `ft_isalnum`  
- `ft_isascii`  
- `ft_isprint`  
- `ft_toupper`  
- `ft_tolower`  

### 🧵 String functions

- `ft_strlen`  
- `ft_strchr`  
- `ft_strrchr`  
- `ft_strncmp`  
- `ft_strnstr`  
- `ft_strlcpy`  
- `ft_strlcat`  
- `ft_strdup`  
- `ft_substr`  
- `ft_strjoin`  
- `ft_strtrim`  
- `ft_split`  
- `ft_strmapi`  
- `ft_striteri`  

### 💾 Memory functions

- `ft_memset`  
- `ft_bzero`  
- `ft_memcpy`  
- `ft_memmove`  
- `ft_memchr`  
- `ft_memcmp`  
- `ft_calloc`  

### 🔁 Conversions

- `ft_atoi`  
- `ft_itoa`  

### 🖨️ File‑descriptor output

- `ft_putchar_fd`  
- `ft_putstr_fd`  
- `ft_putendl_fd`  
- `ft_putnbr_fd`  

### ➕ Bonus – Linked list API

Uses the following structure:

```c
typedef struct s_list
{
    void            *content;
    struct s_list   *next;
}   t_list;
```

Implemented list functions:

- `ft_lstnew`  
- `ft_lstadd_front`  
- `ft_lstsize`  
- `ft_lstlast`  
- `ft_lstadd_back`  
- `ft_lstdelone`  
- `ft_lstclear`  
- `ft_lstiter`  
- `ft_lstmap`  

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
gcc -Wall -Wextra -Werror main.c -L. -lft -o my_program

# Example: libft in ./M0 - Libft/
gcc -Wall -Wextra -Werror main.c -L"M0 - Libft" -I"M0 - Libft" -lft -o my_program
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
gcc -Wall -Wextra -Werror
```

- No forbidden functions beyond project subject.
- All dynamically allocated memory must be properly freed by the caller.
