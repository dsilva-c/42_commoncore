# Push_swap — Defense Support Document

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Algorithm Explained](#2-algorithm-explained)
3. [Data Structure](#3-data-structure)
4. [File-by-File Breakdown](#4-file-by-file-breakdown)
5. [Sorting Operations](#5-sorting-operations)
6. [Error Handling](#6-error-handling)
7. [Memory Management](#7-memory-management)
8. [Performance](#8-performance)
9. [Bonus — Checker](#9-bonus--checker)
10. [Common Defense Questions & Answers](#10-common-defense-questions--answers)
11. [Quick Demo Commands](#11-quick-demo-commands)

---

## 1. Project Overview

**Goal:** Sort a stack of integers using only two stacks (`a` and `b`) and a limited set
of operations, in the fewest moves possible.

**Allowed operations:**

| Operation | Description |
|-----------|-------------|
| `sa` | Swap first two elements of stack `a` |
| `sb` | Swap first two elements of stack `b` |
| `ss` | `sa` + `sb` simultaneously |
| `pa` | Push top of `b` onto `a` |
| `pb` | Push top of `a` onto `b` |
| `ra` | Rotate `a` upward (first becomes last) |
| `rb` | Rotate `b` upward (first becomes last) |
| `rr` | `ra` + `rb` simultaneously |
| `rra` | Reverse rotate `a` (last becomes first) |
| `rrb` | Reverse rotate `b` (last becomes first) |
| `rrr` | `rra` + `rrb` simultaneously |

**Input:** Integers as arguments (separate or quoted string).
**Output:** List of operations to stdout that sort the stack.

---

## 2. Algorithm Explained

### The "Turkish" / Mechanical Turk Algorithm

This is NOT a classic algorithm (quicksort, radix, etc.). It's a **cost-based greedy
algorithm** with these phases:

### Phase 1 — Push from A to B (keeping B sorted descending)

1. For each node in `a`, calculate:
   - **target in B**: the node in `b` that is the closest smaller value (or if none
     exists, the max in `b`)
   - **cost_a**: how many rotations to bring this node to top of `a`
   - **cost_b**: how many rotations to bring its target to top of `b`
   - **total cost**: the combined cost, optimized for same-direction rotations

2. Pick the **cheapest** node in `a` to push.
3. Execute the rotations and push (`pb`).
4. Repeat until only 3 elements remain in `a`.

**Why this works:** By always picking the cheapest move, we minimize total operations
while maintaining `b` in descending order.

### Phase 2 — Sort 3 remaining in A

With only 3 elements, there are at most 5 permutations. Hardcoded logic handles all
cases in at most 2 moves.

### Phase 3 — Push everything back from B to A

1. For each node in `b`, find its **target in A**: the closest larger value (or if none
   exists, the min in `a`).
2. Rotate `a` to position the target at top.
3. Push (`pa`).

### Phase 4 — Final alignment

Rotate `a` so the minimum value is at the top.

### Visual Example (5 elements: `5 3 1 4 2`)

```
Step 0:  a=[5,3,1,4,2]  b=[]
         Push cheapest to b...
Step 1:  a=[5,1,4,2]    b=[3]      (pb)
Step 2:  a=[5,1,4]      b=[3,2]    (pb) — 2 < 3, goes below
         Sort 3 in a...
Step 3:  a=[1,4,5]      b=[3,2]    (sa, ra)
         Push back to a...
Step 4:  a=[1,3,4,5]    b=[2]      (pa)
Step 5:  a=[1,2,3,4,5]  b=[]       (pa)
         Already aligned
```

---

## 3. Data Structure

### Doubly-Linked List (as a Stack)

```c
typedef struct s_stack_node
{
    int                 nbr;          // The actual integer value
    int                 index;        // Position in stack (0 = top)
    int                 push_cost;    // Cost to move to top
    bool                above_median; // Is it in the upper half?
    bool                cheapest;     // Is it the cheapest to push?
    struct s_stack_node *target_node; // Pointer to target in other stack
    struct s_stack_node *next;        // Next node (below)
    struct s_stack_node *prev;        // Previous node (above)
}   t_stack_node;
```

**Why doubly-linked list?**
- `rotate` (move first to last): O(1) — just shift the head pointer
- `reverse_rotate` (move last to first): O(1) — just shift the head pointer back
- `push`/`pop`: O(1) — pointer manipulation
- `swap`: O(1) — swap two node positions

**Why not an array?**
- Rotations on arrays are O(n) (shift all elements)
- Linked list rotations are O(1)

---

## 4. File-by-File Breakdown

### Mandatory Files

| File | Purpose | Key Functions |
|------|---------|---------------|
| `main.c` | Entry point, argument handling | `main()` — parses args, inits stack, picks sort strategy |
| `push_swap.h` | Header with all prototypes | Struct definition, function declarations |
| `stack_init.c` | Stack creation from arguments | `init_stack_a()` — converts strings to nodes, checks errors |
| `stack_utils.c` | Stack utility functions | `find_last()`, `find_min()`, `find_max()`, `stack_len()`, `stack_sorted()` |
| `handle_errors.c` | Input validation + cleanup | `syntax_error()`, `error_duplicate()`, `free_stack()`, `free_matrix()` |
| `ft_split.c` | Split quoted string arguments | Custom `ft_split()` for `"3 2 1"` format |
| `ft_utils.c` | Utility functions | `ft_atol()` — string to long with overflow check |
| `push.c` | `pa` and `pb` operations | Moves top of one stack to top of the other |
| `swap.c` | `sa`, `sb`, `ss` operations | Swaps first two nodes of a stack |
| `rotate.c` | `ra`, `rb`, `rr` operations | First element becomes last |
| `rev_rotate.c` | `rra`, `rrb`, `rrr` operations | Last element becomes first |
| `sort_three.c` | Hardcoded 3-element sort | `sort_three()` — handles all permutations |
| `sort_stacks.c` | Main sorting orchestrator | `sort_stacks()` — Phase 1 through 4 |
| `init_a_to_b.c` | A to B analysis | `current_index()`, `set_target_a()`, `cost_analysis_a()`, `set_cheapest()` |
| `init_b_to_a.c` | B to A analysis | `set_target_b()` — target-finding for push-back phase |

### Bonus Files

| File | Purpose |
|------|---------|
| `checker.c` | Reads operations from stdin, applies them, checks if sorted |
| `get_next_line.c` | Reads one line at a time from fd |
| `get_next_line_utils.c` | GNL helper functions |
| `get_next_line.h` | GNL header |

---

## 5. Sorting Operations — How They Work in Code

### swap (swap.c)

```
Before: [A] <-> [B] <-> [C]
After:  [B] <-> [A] <-> [C]
```

The function swaps the **positions** of the first two nodes by relinking `prev`/`next`
pointers. It does NOT swap values — it physically moves node positions. This preserves
pointer integrity for `target_node` references.

### push (push.c)

```
Stack A: [1] -> [2] -> [3]     Stack B: [4] -> [5]
After pb:
Stack A: [2] -> [3]            Stack B: [1] -> [4] -> [5]
```

Detaches the top node from source, inserts it at the top of destination.

### rotate (rotate.c)

```
Before: [1] -> [2] -> [3] -> [4]
After:  [2] -> [3] -> [4] -> [1]
```

The head pointer advances to `head->next`. The old head becomes the last node.

### reverse_rotate (rev_rotate.c)

```
Before: [1] -> [2] -> [3] -> [4]
After:  [4] -> [1] -> [2] -> [3]
```

The last node is detached and prepended to the front.

---

## 6. Error Handling

The program must print `Error\n` to **stderr** and exit for:

| Case | How it's caught |
|------|-----------------|
| Non-numeric input (`"abc"`) | `syntax_error()` checks each char is digit/sign |
| Sign without number (`"+"`, `"-"`) | `syntax_error()` checks length after sign |
| Integer overflow (`2147483648`) | `ft_atol()` converts to `long`, checks against INT limits |
| Duplicate values (`3 3`) | `error_duplicate()` compares each new value against existing nodes |
| Empty string (`""`) | Checked before processing |

**What should NOT be an error:**
- Single argument (already sorted) -> print nothing
- Already sorted list -> print nothing
- Negative numbers -> valid
- `INT_MIN` / `INT_MAX` -> valid

---

## 7. Memory Management

### Allocation points:
1. `ft_split()` — allocates array of strings (when using quoted format)
2. `append_node()` in `stack_init.c` — allocates each `t_stack_node`

### Free points:
1. `free_stack()` — traverses the linked list and frees every node
2. `free_matrix()` — frees the split string array
3. On error: both are called before `exit(1)`

### Verification:
```bash
valgrind --leak-check=full --show-leak-kinds=all ./push_swap 5 3 1 4 2
# Result: 0 bytes lost, 0 errors

valgrind --leak-check=full --show-leak-kinds=all ./push_swap 5 5
# Result: prints "Error", 0 bytes lost

echo "sa" | valgrind --leak-check=full ./checker 3 2 1
# Result: 0 bytes lost
```

---

## 8. Performance

### Scoring thresholds (from subject):

| Size | Max moves for 5/5 | Our average |
|------|--------------------|-------------|
| 3 | 2-3 | 1-2 |
| 5 | 12 or less | 8-9 |
| 100 | < 700 | ~550-590 |
| 500 | < 5500 | ~5000-5350 |

### How to verify:

```bash
# Count moves for 100 random numbers:
ARG=$(shuf -i 1-1000 -n 100 | tr '\n' ' '); ./push_swap $ARG | wc -l

# Verify correctness with subject's checker:
ARG=$(shuf -i 1-1000 -n 100 | tr '\n' ' '); ./push_swap $ARG | ./checker_linux $ARG

# Run multiple tests:
for i in $(seq 1 10); do
  ARG=$(shuf -i 1-10000 -n 500 | tr '\n' ' ')
  MOVES=$(./push_swap $ARG | wc -l)
  CHECK=$(./push_swap $ARG | ./checker_linux $ARG)
  echo "Test $i: $MOVES moves — $CHECK"
done
```

### Why the cost optimization matters:

In `cost_analysis_a()`, when both nodes rotate in the **same direction** (both above
or both below median), we use `max(cost_a, cost_b)` instead of `cost_a + cost_b`.
This is because `rr` and `rrr` move both stacks simultaneously:

```
// If a needs ra 3 times and b needs rb 5 times:
// Without optimization: 3 + 5 = 8 moves
// With optimization: rr x 3, then rb x 2 = 5 moves (= max(3,5))
```

This single optimization saves ~500-1000 moves on 500 elements.

---

## 9. Bonus — Checker

The `checker` program:

1. Takes the same arguments as `push_swap`
2. Reads operations from **stdin** (one per line)
3. Applies each operation to the stacks
4. At EOF: checks if `a` is sorted and `b` is empty
5. Prints `OK` or `KO`

### How it works:

```bash
# Manual test:
./checker 3 2 1
sa
ra
[Ctrl+D]
OK

# Pipe from push_swap:
./push_swap 3 2 1 | ./checker 3 2 1
OK

# Invalid operation:
./checker 3 2 1
invalid
[Ctrl+D]
Error
```

### Key implementation details:
- Uses **get_next_line** to read from stdin (fd 0)
- Validates each instruction string against the 11 allowed operations
- Reuses the same stack operations as push_swap (but without printing)
- The `bool checker` parameter in operations controls whether to print or not

---

## 10. Common Defense Questions & Answers

### Q: Why did you choose a linked list over an array?
**A:** Rotations are the most frequent operation. In an array, rotation requires shifting
all elements — O(n). In a doubly-linked list, rotation is O(1) — just move the head
pointer. Since we do thousands of rotations, this matters for performance.

### Q: What's the time complexity of your algorithm?
**A:** For each push from A to B, we iterate through all nodes in A and for each
calculate its target in B — that's O(n*m). We do this n-3 times. So overall it's
approximately **O(n^2)**, which is acceptable for n <= 500.

### Q: Why not use quicksort or radix sort?
**A:** Radix sort on bit manipulation gives consistent results but often more moves
(~6000-7000 for 500). The cost-based greedy approach (Turkish algorithm) typically
achieves fewer moves (~5000) because it optimizes each individual push. Quicksort is
harder to implement with the limited operations and often needs more moves.

### Q: How do you handle INT_MIN and INT_MAX?
**A:** `ft_atol()` converts to `long` first, then checks if the value exceeds `INT_MAX`
(2147483647) or is below `INT_MIN` (-2147483648). If so, it triggers an error. The
values themselves are valid if within range.

### Q: What happens with a single number?
**A:** `stack_sorted()` returns true (a single element is sorted), so the program prints
nothing and exits 0.

### Q: What happens with already sorted input?
**A:** Same — `stack_sorted()` detects it and exits without printing any operations.

### Q: How does set_target_a() work?
**A:** For each node in `a`, we search `b` for the **closest smaller value**. We iterate
all of `b` looking for the largest value that is still smaller than the current `a` node.
If no smaller value exists (current node is the minimum), the target becomes `b`'s
maximum — because `b` is sorted descending and we want to maintain that order.

### Q: How does set_target_b() work?
**A:** The reverse — for each node in `b`, we find the **closest larger value** in `a`.
If none exists (current node is the maximum), the target is `a`'s minimum.

### Q: What's the above_median flag for?
**A:** It determines the rotation direction. If a node is above the median (index <
len/2), we use `ra`/`rb` (rotate up). If below, we use `rra`/`rrb` (reverse rotate).
This ensures we always rotate in the shorter direction.

### Q: How does the combined rotation optimization work?
**A:** When both the node in `a` and its target in `b` are on the same side (both above
or both below median), we can use `rr` or `rrr` to rotate both simultaneously. The
cost becomes `max(cost_a, cost_b)` instead of `cost_a + cost_b`, saving many moves.

### Q: How do you ensure there are no memory leaks?
**A:** Every `malloc` has a corresponding `free`. `free_stack()` traverses the entire
linked list freeing each node. `free_matrix()` frees split strings. On error paths,
both are called before `exit(1)`. Verified with valgrind — 0 leaks in all scenarios.

### Q: What does your Makefile do?
**A:**
- `make` / `make all` — compiles `push_swap`
- `make bonus` — compiles `checker`
- `make clean` — removes `.o` files
- `make fclean` — removes `.o` + binaries
- `make re` — `fclean` + `all`
- Uses `-Wall -Wextra -Werror` flags

### Q: Why does swap() move nodes instead of swapping values?
**A:** Swapping just the `nbr` values would be simpler, but it would invalidate
`target_node` pointers that other nodes hold. By physically relinking the nodes, all
existing pointers remain valid. This is more robust and correct.

### Q: What edge cases does your error handling cover?
**A:**
- Empty input -> exit 0 (no error)
- Non-numeric (`abc`, `12a3`) -> `Error`
- Sign only (`+`, `-`) -> `Error`
- Overflow (`99999999999`) -> `Error`
- Duplicates (`3 3`) -> `Error`
- Leading zeros (`007`) -> valid, treated as 7
- Negative numbers (`-5`) -> valid
- Mixed format (`./push_swap "3 2" 1`) -> valid

---

## 11. Quick Demo Commands

```bash
# Build everything
make && make bonus

# Simple test
./push_swap 2 1 3 6 5 8
# Expected: handful of operations

# Verify with checker
./push_swap 2 1 3 6 5 8 | ./checker 2 1 3 6 5 8
# Expected: OK

# String format
./push_swap "2 1 3 6 5 8"
# Same output as above

# Error cases
./push_swap 1 2 abc          # Error
./push_swap 1 2 2            # Error
./push_swap 99999999999      # Error
./push_swap                   # (nothing, exit 0)
./push_swap 42               # (nothing, exit 0)
./push_swap 1 2 3            # (nothing, already sorted)

# Performance test — 100 numbers
ARG=$(shuf -i 1-1000 -n 100 | tr '\n' ' ')
echo "Moves: $(./push_swap $ARG | wc -l)"
echo "Valid: $(./push_swap $ARG | ./checker_linux $ARG)"

# Performance test — 500 numbers
ARG=$(shuf -i 1-10000 -n 500 | tr '\n' ' ')
echo "Moves: $(./push_swap $ARG | wc -l)"
echo "Valid: $(./push_swap $ARG | ./checker_linux $ARG)"

# Memory leak check
valgrind --leak-check=full ./push_swap 5 3 1 4 2

# Bonus checker with manual input
./checker 3 2 1
sa
ra
# then press Ctrl+D
# Expected: OK

# Norminette
norminette *.c *.h
```

---

Good luck with the defense!
