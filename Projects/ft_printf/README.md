<img width="2000" height="500" alt="ft_printf cover" src="cover.png" />

<div align="center">

# 🖨️ M1 – ft_printf

![42 ft_printf](https://img.shields.io/badge/Porto-ft__printf-00babc?style=for-the-badge&logo=42&logoColor=white&labelColor=000000)
<br/>
<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" style="margin-right:6px"/>
<img src="https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white" style="margin-right:6px"/>

<p align="center">
  <img width="141" height="150" alt="ft_printf_bonus_max" src="badge.png" />
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
ft_printf/
├── includes/
│   ├── ft_printf.h         # Mandatory prototypes
│   └── ft_printf_bonus.h   # Bonus flags and struct
├── libft/                  # Dependency on Libft project
├── srcs/
│   ├── mandatory/          # Core conversion logic
│   │   └── ft_*.c
│   └── bonus/              # Flag parsing and bonus print functions
│       └── ft_*.c
├── tester/                 # Custom ft_printf tester (separate project, see tester/README.md)
├── Makefile                # Builds libftprintf.a (includes mandatory & bonus)
├── README.md               # This file
└── en.subject.pdf          # ft_printf subject

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
ft_printf/tester/
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

## 🛡️ Defense Notes

- **`%p` format — does it match real `printf`?** `ft_putptr`/`ft_print_pointer_bonus` print `"0x"` followed by lowercase hex digits, and `"(nil)"` for a `NULL` pointer — this matches glibc's behavior exactly (glibc special-cases `NULL` as `(nil)` rather than `0x0`). Be ready to show `ft_puthex`/`ft_putptr_rec` use the lowercase table `"0123456789abcdef"` regardless of case — `%p` has no uppercase variant in the subject.
- **Why do `%d` and `%i` behave identically?** Both branches in `ft_handle_format`/`ft_handle_conversion` call the exact same function (`ft_print_number` / `ft_print_number_bonus`). There is no behavioral difference for output — the `d`/`i` distinction only matters for `scanf`, where `%i` auto-detects base (0x/0 prefixes) and `%d` forces base 10.
- **How is `INT_MIN` handled without overflow?** Negating `INT_MIN` as an `int` is undefined behavior, since `-INT_MIN` doesn't fit in a signed 32-bit int. Both `ft_putnbr` (mandatory) and `ft_init_num_vars` (bonus) sidestep this by copying `n` into a `long nb` *before* negating (`nb = n; if (nb < 0) nb = -nb;`). Since `long` is wider, `-INT_MIN` fits comfortably. This is the single most common gotcha evaluators probe for.
- **What does `ft_printf` return, and why does it matter?** It returns the total character count, accumulated from every `write()`'s return value (which is itself the byte count written, or -1 on failure) — not just a fixed increment per conversion. It returns `-1` immediately if `format` is `NULL`. This mirrors real `printf`'s contract: return chars written, or negative on error, since callers (e.g. code checking `if (printf(...) < 0)`) rely on it.
- **Mechanics of `va_list`/`va_arg`:** the compiler knows, from the type passed to `va_arg(args, T)`, how many bytes/registers to advance the argument cursor by — there's no runtime type information stored anywhere. If the format string says `%d` but the caller actually passed a `long`, `va_arg(args, int)` reads the wrong width and desyncs every argument after it — this is why the subject restricts which conversions must be supported (no `%ld`, `%lld`, etc. in mandatory) and why format-string mismatches in real `printf` are a classic security bug (uninitialized reads, stack corruption).
- **Why call `va_end` if nothing seems to break without it?** On most modern ABIs (e.g. x86-64 System V) `va_end` is a no-op, but the standard requires it to balance `va_start`, because on other architectures `va_start` can reserve resources (allocate a save area, adjust a stack pointer) that only `va_end` releases. Skipping it is undefined behavior even where it happens to work.
- **A subtle portability detail worth mentioning:** `ft_handle_format`/`ft_handle_conversion` take `va_list args` "by value" as a function parameter, then call `va_arg` on that local copy. On x86-64 Linux, `va_list` is actually defined as a 1-element array of a struct, so passing it to a function decays to a pointer and the callee's `va_arg` calls do advance the caller's cursor too — which is exactly why this code works. That behavior is an implementation detail of this specific ABI, not something the C standard guarantees; on an ABI where `va_list` is a plain struct, this pattern would silently break (the callee would advance its own copy and the caller's list would never move).
- **Char-by-char output, not buffered.** Every character goes through its own `write(1, &c, 1)` syscall (`ft_putchar`, `ft_putchar_count`) — there is no internal buffer. This keeps the logic simple and the return-value bookkeeping trivial (each `write` return is summed directly), but it's far more syscall-heavy than glibc's buffered `stdio`, which batches writes into a single flush. Worth acknowledging as a known tradeoff if asked "is this how real printf does it?"
- **Zero-padding vs. precision vs. left-justify — the interaction that's easy to get wrong:** the `0` flag is silently dropped whenever `-` (left-justify) or a precision (`.`) is present — see `ft_parse_flags` (`if (flags->minus) flags->zero = 0;`) and `ft_init_num_vars`/`ft_init_hex_vars` (`if (flags->dot) flags->zero = 0;`). This matches real `printf`: `%05.3d` zero-pads to width, but the precision decides *digit* padding while `0` only decides *field* padding — combining both without disabling `0` under precision would double-pad. Also note `%.0d` with value `0` prints nothing at all (`numlen`/`hexlen` forced to `0` when precision is `0` and the value is `0`), matching glibc exactly.
- **Sign flag precedence:** `+` and space (`' '`) both only apply to non-negative numbers, and `+` wins if both are set (checked in that order in `ft_print_sign`) — negative numbers always get `-` regardless of either flag. This ordering (negative sign, then `+`, then space) is worth reciting if asked to trace a specific format string by hand.
- **What's deliberately not supported:** there's no `*` (dynamic width/precision from an extra `va_arg`) and no length modifiers (`l`, `ll`, `h`) — only the exact conversions listed in the subject. Trying to combine unsupported specifiers isn't handled defensively beyond what the parser recognizes; be ready to explain that this is a scope decision driven by the subject, not an oversight.

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
