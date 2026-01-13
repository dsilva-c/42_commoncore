<div align="center">

# 🧪 ft_printf tester

![42 ft_printf Tester](https://img.shields.io/badge/42Porto-ft__printf_Tester-00babc?style=for-the-badge&logo=42)
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white)
![Valgrind](https://img.shields.io/badge/Valgrind-2E3C45?style=for-the-badge&logo=valgrind&logoColor=white)

This is a dedicated tester project for the **ft_printf** project, designed to rigorously verify the implementation of all mandatory conversions, bonus flags, and complex edge cases by comparing the output and return value of your `ft_printf` against the system's `printf`.

</div>

> ⚠️ **Important:** This tester requires the **complete** `ft_printf` **implementation** (including the bonus part) to be built and linked correctly.

---

## 🎯 Testing scope

The tester covers the full required scope of the `ft_printf` subject:

### ➡️ Mandatory functionality

### ➕ Bonus flag combinations

---

## 📂 Folder structure

```text
tester/
├── Makefile                     # builds the tester executable
├── tester.h                     # tester header
├── tester.c                     # main execution and overall test aggregation
├── tester_print.c               # color-coded output and summary printing functions
├── test_mandatory*.c            # tests for core conversions and basic functionality
├── test_bonus*.c                # tests for width, precision, and flag combinations
├── test_hardcore.c              # specific tests for precedence and edge cases
└── README.md                    # this file
```

---

## ⚙️ Setup and building

This tester expects the ft_printf project folder:

- .../M1 - ft_printf/        ← ft_printf project root (contains `Makefile` and `libftprintf.a` after building)
- .../M1 - ft_printf/tester/ ← this tester folder

Build Steps

1) Build `libftprintf.a` (ensure `make bonus` is run):
```bash
cd "/path/to/M1 - ft_printf"
make bonus      # produces libftprintf.a
```

2) Build the Tester: The tester's `Makefile` automatically calls `make -C .. bonus` to ensure the library is up-to-date before linking.

From inside the `tester/` directory:
```bash
# Build the tester executable (links libftprintf.a)
make
```

---

## 🚀 Build & run (tester)

After completing the Setup steps above, build and run the tester from the `tester/` directory.

Run tests
```bash
# run the tester executable
./tester

# or use the Makefile shortcut
make run
```
---

## 🧪 Memory checking with Valgrind

Memory leaks are a common source of bugs in `ft_printf`. Valgrind is essential for checking invalid reads/writes related to string formatting and pointer handling.
```bash
# Run the tester under Valgrind
make leaks
```

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
                <img src="https://img.shields.io/badge/-Valgrind-2E3C45" alt="Valgrind">
                <img src="https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white" alt="Git">
            </td>
        </tr>
    </tbody>
</table>

</div>

---

## 🐞 Troubleshooting

- **`libftprintf.a: No such file or directory`**  
  ➜ Ensure you ran `make bonus` in the main `ft_printf` project directory.
- **Linker errors like undefined reference to `ft_print_number_bonus`**  
  ➜ Ensure the `Makefile` in the project root successfully compiles all bonus source files before creating `libftprintf.a`.
- **Test Fails (e.g., Trailing %, %05%)**
   ➜ These are often synchronization failures. Check your `ft_printf_bonus.c` and `test_bonus.c` for the final required return value synchronization patches.

---

Happy debugging and congratulations on reaching the final stage! 🎉
