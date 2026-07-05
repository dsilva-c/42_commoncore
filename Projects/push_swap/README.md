<img width="2000" height="500" alt="push_swap_cover" src="cover.png" />

<div align="center">

# 🔄 M2 – push_swap

![42 push_swap](https://img.shields.io/badge/Porto-push_swap-00babc?style=for-the-badge&logo=42&logoColor=white&labelColor=000000)
<br/>
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-20639B?style=for-the-badge&logo=make&logoColor=white)

<p align="center">
  <img width="141" height="150" alt="push_swap_bonus_max" src="badge.png" />
</p>

This project is part of the **42cursus** at 42 Porto.  
The goal is to sort a stack of integers using a limited set of operations, with the smallest number of moves possible. This project introduces **sorting algorithms**, **algorithm complexity**, and **optimization**.

</div>

---

## 🎯 Objectives

- Implement an efficient sorting algorithm using two stacks and a restricted set of operations.
- Understand and apply concepts of **algorithm complexity** (Big O notation).
- Practice cost analysis and optimization to minimize the number of operations.
- Handle edge cases and error management robustly.
- Provide clean, Norm-compliant C code.

---

## 🧱 Project structure

```text
push_swap/
├── push_swap.h              # Main header with struct and prototypes
├── Makefile                 # Builds push_swap (mandatory) and checker (bonus)
├── main.c                   # Entry point for push_swap
├── handle_errors.c          # Input validation and error handling
├── stack_init.c             # Stack initialization and push preparation
├── stack_utils.c            # Stack utility functions (len, find min/max, etc.)
├── push.c                   # pa / pb operations
├── swap.c                   # sa / sb / ss operations
├── rotate.c                 # ra / rb / rr operations
├── rev_rotate.c             # rra / rrb / rrr operations
├── sort_three.c             # Sorting algorithm for 3 elements
├── sort_stacks.c            # Main sorting algorithm (Turk sort)
├── init_a_to_b.c            # Node initialization for a → b phase
├── init_b_to_a.c            # Node initialization for b → a phase
├── ft_split.c               # Custom split for string argument handling
├── ft_utils.c               # ft_atol helper
├── checker.c                # Bonus: checker program
├── get_next_line.h          # GNL header (used by checker)
├── get_next_line.c          # GNL main logic (used by checker)
├── get_next_line_utils.c    # GNL helpers (used by checker)
├── tester/                  # Push_swap tester (see tester/README.md)
└── README.md                # this file
```

---

## 📝 Available operations

The program uses two stacks (**a** and **b**) and the following operations:

### 🔄 Swap

<div align="center">

| Operation | Description |
| :--- | :--- |
| `sa` | Swap the first two elements at the top of stack **a** |
| `sb` | Swap the first two elements at the top of stack **b** |
| `ss` | `sa` and `sb` at the same time |

</div>

### ⬆️ Push

<div align="center">

| Operation | Description |
| :--- | :--- |
| `pa` | Push the top element of **b** onto **a** |
| `pb` | Push the top element of **a** onto **b** |

</div>

### 🔃 Rotate

<div align="center">

| Operation | Description |
| :--- | :--- |
| `ra` | Rotate **a** up: first element becomes last |
| `rb` | Rotate **b** up: first element becomes last |
| `rr` | `ra` and `rb` at the same time |

</div>

### 🔄 Reverse Rotate

<div align="center">

| Operation | Description |
| :--- | :--- |
| `rra` | Reverse rotate **a**: last element becomes first |
| `rrb` | Reverse rotate **b**: last element becomes first |
| `rrr` | `rra` and `rrb` at the same time |

</div>

---

## 🧠 The algorithm

This implementation uses the **Turk sort** algorithm, a cost-based approach:

1. **Push to B**: Push all elements except 3 from stack **a** to stack **b**, targeting the closest smaller value in **b** for each element.
2. **Sort three**: Sort the remaining 3 elements in **a** using at most 2 operations.
3. **Push back to A**: Push elements from **b** back to **a**, each time finding its correct target position.
4. **Final rotation**: Rotate **a** to bring the minimum to the top.

The cost analysis accounts for simultaneous rotations (`rr` / `rrr`) when both the source and target nodes are on the same side of their respective stacks, using `max(cost_a, cost_b)` instead of `cost_a + cost_b`.

### ⚡ Performance

<div align="center">

| Stack size | Average moves | Threshold for max grade |
| :--- | :--- | :--- |
| 3 | ≤ 2 | 3 |
| 5 | ≤ 12 | 12 |
| 100 | ~560 | < 700 |
| 500 | ~5100 | < 5500 |

</div>

---

## ➕ Bonus – Checker

The bonus part implements a `checker` program that:

1. Takes the same arguments as `push_swap`.
2. Reads sorting instructions from standard input (one per line).
3. Applies them to the stack.
4. Prints `OK` if the stack is sorted after all operations, `KO` otherwise.
5. Prints `Error` on invalid input (bad arguments or unknown instruction).

```bash
# Verify push_swap output with checker
./push_swap 3 2 1 | ./checker 3 2 1
# Output: OK
```

---

## 🛠️ Building the project

From inside the project root:

```bash
# build mandatory part (push_swap)
make

# build bonus part (checker)
make bonus

# remove object files
make clean

# remove objects + binaries
make fclean

# full rebuild
make re

# check for memory leaks with Valgrind
make valgrind ARGS="4 67 3 87 23"
```

This produces:

```text
push_swap   # the sorting program
checker     # the bonus checker program
```

---

## 🚀 Usage

```bash
# Multiple arguments
./push_swap 4 67 3 87 23

# Single string argument
./push_swap "4 67 3 87 23"

# Count the number of operations
./push_swap 4 67 3 87 23 | wc -l

# Verify with checker
./push_swap 4 67 3 87 23 | ./checker 4 67 3 87 23

# Generate random numbers and test
ARG=$(shuf -i 1-500 -n 100 | tr '\n' ' '); ./push_swap $ARG | wc -l

# Generate random negative numbers and test
ARG=$(shuf -i 1-500 -n 100 | sed 's/^/-/' | tr '\n' ' '); ./push_swap $ARG | wc -l
```

---

## ⚠️ Error handling

The program handles the following error cases by writing `Error\n` to stderr:

- Non-numeric arguments
- Duplicate numbers
- Numbers exceeding `INT_MAX` or below `INT_MIN`
- Invalid signs (`+` or `-` alone)

No arguments or an empty string argument produces no output.

---

## 🧪 Testing

There is a dedicated tester in:

```text
push_swap/tester/
```

It runs identity tests, small sort tests, error handling tests, performance benchmarks (100 and 500 elements), and bonus checker tests.  
See [`tester/README.md`](tester/README.md) for usage instructions.

---

## ✅ Code style & requirements

- Follows **42 Norm**.
- Compiled with:

```bash
cc -Wall -Wextra -Werror
```

- No forbidden functions beyond project subject.
- All dynamically allocated memory is properly freed (verified with Valgrind — 0 leaks). Use `make valgrind ARGS="..."` to check.
- Uses a doubly-linked list for efficient stack operations.

---

## 🛡️ Defense Notes

- **"Why not quicksort/mergesort?"** The constraint isn't algorithmic complexity, it's the operation set. There is no "compare index 3 and index 47, then swap them" primitive — only `sa`/`sb`/`ss` (swap the top two), `pa`/`pb` (move the top of one stack to the other), and rotations (`ra`/`rb`/`rr`, `rra`/`rrb`/`rrr`) that only ever touch the top or bottom of a stack. Any classic array-based sort assumes random access and arbitrary swaps; here you can only ever act on what's currently on top. That's why the whole design (Turk sort) is built around funneling elements through a second stack with targeted pushes and rotations instead of comparing arbitrary pairs directly.
- **How `push_cost` is computed** (`init_a_to_b.c`, `cost_analysis_a`): for each node in `a`, `cost_a` is its distance to the top counting forward if it's in the top half (`above_median`) or backward from the bottom if it's in the bottom half; `cost_b` is the same distance computed for its `target_node` in `b`. If `a`'s node and its target in `b` are on the **same side** (`above_median` equal), the code uses `max(cost_a, cost_b)` (line `a->push_cost = cost_a; if (cost_b > cost_a) a->push_cost = cost_b;`); otherwise it uses `cost_a + cost_b`. Be ready to explain why `max` is valid only in the same-side case: `rr`/`rrr` rotate both stacks in one instruction, so rotating `a` and `b` together "pays for" both movements simultaneously — you're not spending separate ra/rb ops, just one `rr` per step, so the total cost is bounded by whichever stack needs more rotations, not the sum. When the two nodes are on opposite sides, one needs a forward rotation and the other a reverse rotation, which can't be combined into a single `rr`/`rrr`, so the costs add.
- **`rotate_both` / `rev_rotate_both`** (`sort_stacks.c`) are the code that actually cashes in on that `max` cost: they loop calling `rr` (or `rrr`) until either `a` reaches the cheapest node or `b` reaches its target, then `prep_for_push` finishes rotating whichever stack is lagging alone, and finally `pb` pushes. This is only correct because `move_a_to_b` gates it behind `cheapest_node->above_median == cheapest_node->target_node->above_median` — the same condition used in the cost calculation.
- **Why `sort_three` doesn't reuse the general algorithm**: with exactly 3 elements there are only 6 possible orderings, so `sort_three.c` just locates the max via `find_max`, rotates it to the top (`ra`) or bottom (`rra`) depending on where it sits, then does a single `sa` if the remaining top two are still inverted — at most 2 operations, no cost analysis, no second stack involved. Running the general push-to-b machinery on 3 elements would cost more instructions for no benefit; a fixed decision path is strictly cheaper and simpler to prove correct for a case this small.
- **Doubly-linked list vs. array** (`push_swap.h`, `stack_init.c`): `t_stack_node` carries `prev`/`next` plus per-node metadata (`index`, `push_cost`, `above_median`, `cheapest`, `target_node`). Push (`pa`/`pb`) and pop are O(1) at the head with pointer relinking — no shifting of subsequent elements the way an array-backed stack would require on every insert/delete at the front. It also lets each node own its own cached cost/target data directly, rather than needing parallel arrays indexed alongside a numeric array representation.
- **Error handling specifics** (`handle_errors.c`, `stack_init.c`, `main.c`): `error_syntax` rejects anything that isn't a bare `+`/`-`/digit start, a lone sign with no following digit, or any non-digit character elsewhere in the token. `error_duplicate` walks the stack so far and rejects a repeated value. `init_stack_a` uses `ft_atol` (returns `long`) and rejects any value `> INT_MAX` or `< INT_MIN` before the cast to `int` — this is what catches overflow beyond `int` range even though the final stored value is an `int`. All three paths call `free_errors`, which frees the partially built stack, writes `Error\n` to **stderr**, and exits with status 1. Separately, `main.c` returns `0` silently for no arguments or an empty string argument — that's a no-op, not an error, and matches the README's "Error handling" section.
- **Checker independence** (`checker.c`): it rebuilds the same stack from the same argv, then reads operations line-by-line via `get_next_line`, dispatching each to the *same* op functions (`sa`, `pb`, `rr`, etc., called with `print = false`) via `parse_command`. Any line that doesn't match one of the 11 known instructions exactly falls through to `free_errors`. After the input is exhausted, it prints `OK` only if `stack_sorted(*a)` is true **and** `stack_len(*b) == 0` (nothing left stranded in `b`) — otherwise `KO`. The point of a separate checker is that it never trusts `push_swap`'s internal reasoning (cost tables, target nodes, etc.) — it only trusts the literal operation stream on stdout, replayed through minimal, independently-verifiable logic. If `push_swap` had a bug in its sorting logic but happened to print a plausible-looking trace, the checker would still catch it because it actually re-executes every instruction.
- **Performance thresholds** (see the Performance table above): moves are counted with `wc -l` on `push_swap`'s stdout. For 100 elements the grading threshold is under 700 moves, for 500 elements under 5500. Exceeding a threshold isn't a crash or wrong-answer case, it's a grading penalty — the check is purely on move count. If a submission is right at the edge, the two places to look first are whether `cost_analysis_a`'s `above_median` split is well balanced (an uneven split degrades the `max` cost saving) and whether `min_on_top`'s final rotation is walking the shorter direction, since both directly move the count for large `n`.

---

## 🛠️ Tech stack

<div align="center">

<table width="100%">
    <thead>
        <tr>
            <th width="80%">Category</th>
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
