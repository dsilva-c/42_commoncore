<img width="2000" height="1000" alt="image" src="https://raw.githubusercontent.com/ayogun/42-project-badges/refs/heads/main/covers/cover-ft_printf-bonus.png" />

# 📚 M1 – ft_printf

<p align="center">
  <img src="https://github.com/leogaudin/42_project_badges/raw/main/badges/ft_printf_bonus_max.webp" alt="ft_printf_bonus_max.webp">
</p>


This project is part of the **42cursus** at 42 Porto.  
The goal is to re-implement the core functionality of the standard C library function `printf()`.

---

## 🎯 Objectives

- Re-implement the standard C library function **`printf`** (including the bonus part).
- Gain a deeper understanding of variadic functions (`stdarg.h`).
- Practice complex parsing logic (handling flags, width, and precision).
- Ensure the code is **Norm-compliant** and robust against edge cases.

---

## 🧱 Project Structure

```text
M1 - ft_printf/
├── includes/
│   ├── ft_printf.h         # Mandatory prototypes
│   └── ft_printf_bonus.h   # Bonus flags and struct
├── srcs/
│   ├── mandatory/          # Core conversion logic
│   └── bonus/              # Flag parsing and bonus print functions
├── Makefile                # Builds libftprintf.a (includes mandatory & bonus)
├── libft/                  # Dependency on Libft project
└── README.md               # this file

```

---

## 📝 Implemented Conversions & Flags

### ➡️ Mandatory Conversions

The function correctly handles the following specifiers:

- `c`: Single character
- `s`: String of characters (handles `(null)` pointer)
- `p`: Pointer address (prefixed with `0x)
- `d` / `i`: Signed decimal integer (handles `INT_MIN` safely)
- `u`: Unsigned decimal integer
- `x` / `X`: Hexadecimal integer (lowercase / uppercase)
- `%`: Literal percent sign


### ➕ Bonus Flags & Features

The function correctly handles all bonus flags and field modifiers:

- `.` (Precision): Max characters for strings, minimum digits for integers
- **Minimum Field Width**
- `-` (Minus): Left-justify
- `0` (Zero): Zero-padding (ignored when precision is set)
- ` ` (Space): Adds a leading space to positive numbers
- `+` (Plus): Adds a `+` to positive numbers (overrides space)
- `#` (Hash): Adds `0x` / `0X` for non-zero hex numbers

---

## 🛠️ Building the library

This project produces a static library: `libftprintf.a`:

From the project root:

```bash
# build only the mandatory part
make

# build the complete library (Mandatory + Bonus Flags)
make bonus

# remove object files
make clean

# remove objects + libftprintf.a
make fclean

# full rebuild
make re
```

---

## 📦 Using ft_printf in another project

1. Copy `libftprintf.a and the `includes` folder into your project.
2. Link it along with `libft.a`:

```bash
cc -Wall -Wextra -Werror main.c -L. -lftprintf -lft -o my_program
```

---

## 🧪 Testing

There is a dedicated tester in:

```text
M1 - ft_printf/tester/
```

It runs functional tests and Valgrind checks.  
See [`tester/README.md`](tester/README.md) for usage instructions.

---

## ✅ Code style & requirements

- Follows **42 Norm**.
- Successfully passes strict compilation checks:

```bash
cc -Wall -Wextra -Werror
```

- Logic for flag precedence and safety checks (e.g., handling **trailing** `%` and **NULL pointers**) is robust.

---

## 📈 Final grade
