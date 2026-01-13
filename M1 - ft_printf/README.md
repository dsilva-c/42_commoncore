<img width="2000" height="500" alt="ft_printf cover" src="https://github.com/user-attachments/assets/7cd90cdd-08c4-45b0-b32f-2486c5a50828" />

<div align="center">

# 🖨️ M1 – ft_printf

![42 ft_printf](https://img.shields.io/badge/Porto-ft__printf-00babc?style=for-the-badge&logo=42&logoColor=white&labelColor=000000)
<br/>
<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" style="margin-right:6px"/>
<img src="https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white" style="margin-right:6px"/>

<p align="center">
  <img width="141" height="150" alt="ft_printf_bonus_max" src="https://github.com/user-attachments/assets/b0fc7ac9-624b-4541-ac0c-7a270367468e" />
</p>


This project is part of the **42cursus** at 42 Porto.  
The goal is to re-implement the core functionality of the standard C library function `printf()`.

</div>

---

## 🎯 Objectives

- Re-implement the standard C library function **`printf`** (including the bonus part).
- Gain a deeper understanding of variadic functions (`stdarg.h`).
- Practice complex parsing logic (handling flags, width, and precision).
- Ensure the code is **Norm-compliant** and robust against edge cases.

---

## 🧱 Project structure

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

## 📝 Implemented conversions & flags

### ➡️ Mandatory conversions

The function correctly handles the following specifiers:

- `c`: Single character
- `s`: String of characters (handles `(null)` pointer)
- `p`: Pointer address (prefixed with `0x)
- `d` / `i`: Signed decimal integer (handles `INT_MIN` safely)
- `u`: Unsigned decimal integer
- `x` / `X`: Hexadecimal integer (lowercase / uppercase)
- `%`: Literal percent sign


### ➕ Bonus flags & features

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

<img width="1101" height="117" alt="ftprintf_grade" src="https://github.com/user-attachments/assets/e883c3a2-d366-46e8-94bc-ff15766b429d" />
