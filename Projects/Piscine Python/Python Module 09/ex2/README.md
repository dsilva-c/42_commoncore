# ex2 — Space Crew Management

## Goal

Compose **nested Pydantic models** (`CrewMember` inside `SpaceMission`)
and enforce multi-record safety rules via `@model_validator`. Explores
how validation errors propagate through model hierarchies.

## Files

<div align="center">

| File | Role |
|------|------|
| `space_crew.py` | `Rank` enum + `CrewMember` + `SpaceMission` + `main()` |
| `main.py` | Module-style entry-point |

</div>

## Model design

```
Rank (str Enum)
  cadet | officer | lieutenant | captain | commander

CrewMember
├── member_id:        str   (3-10 chars)
├── name:             str   (2-50 chars)
├── rank:             Rank
├── age:              int   (18-80 years)
├── specialization:   str   (3-30 chars)
├── years_experience: int   (0-50 years)
└── is_active:        bool  (default True)

SpaceMission
├── mission_id:       str           (5-15 chars)
├── mission_name:     str           (3-100 chars)
├── destination:      str           (3-50 chars)
├── launch_date:      datetime
├── duration_days:    int           (1-3650, max 10 years)
├── crew:             list[CrewMember] (1-12 members)
├── mission_status:   str           (default "planned")
└── budget_millions:  float         (1.0-10000.0 M$)
```

## Mission safety rules (model_validator)

<div align="center">

| Rule | Condition |
|------|-----------|
| ID prefix | `mission_id` must start with `"M"` |
| Senior officer | At least one `commander` or `captain` in crew |
| Long-mission experience | `duration_days > 365` → ≥ 50% crew with 5+ years exp. |
| Active crew | Every `CrewMember.is_active` must be `True` |

</div>

## Concepts explained

### Why `list[CrewMember]` instead of `list[dict]`

`SpaceMission.crew` could have been typed `list[dict]` — Python
wouldn't complain, and the mission validator's loops
(`member.rank in senior_ranks`, `member.years_experience >= 5`,
`member.is_active`) could be rewritten as dict lookups
(`member["rank"]`, etc.). But that throws away everything Pydantic
gives you for free:

- **No validation.** A `dict` accepts literally any keys/values; a
  typo like `{"rank": "comander"}` (missing the second `m`) or a
  missing `age` key would silently propagate into `SpaceMission` and
  only blow up later, deep inside business logic, as a `KeyError` or a
  logic bug — not as a clear `ValidationError` at construction time.
- **No coercion.** Passing `age="38"` (a string) into a dict stays a
  string; `CrewMember` coerces it to `int` because `age` is annotated
  `int`.
- **No static typing.** `member.rank` on a typed `CrewMember` is known
  by mypy/Pylance to be a `Rank`; `member["rank"]` on a `dict` is
  typed as `Any` (or whatever the dict's generic value type is), so a
  typo in the key name or a wrong comparison isn't caught until
  runtime.

Declaring `crew: list[CrewMember]` tells Pydantic "every element of
this list must itself satisfy the `CrewMember` schema," so each dict
or object passed in is run through the same field-level machinery
(`Field(ge=18, le=80)` on `age`, the `Rank` enum check, etc.) that a
top-level model gets.

### How validation cascades through nested models

Constructing a `SpaceMission` with a `crew` list happens in a strict
order:

1. **Per-element field validation.** Before `SpaceMission` itself is
   considered built, Pydantic validates each item in `crew` against
   `CrewMember`'s own fields — `member_id` length, `rank` enum
   membership, `age` range, etc. Each element becomes (or fails to
   become) a genuine `CrewMember` instance independently of the
   others.
2. **Mission-level field validation.** Once every crew element passed
   step 1, the `crew` list itself is checked against
   `Field(min_length=1, max_length=12)` — a check on the *list's
   size*, unrelated to what's inside each element (the same
   `min_length`/`max_length` keywords used for string length in ex0
   apply to sequence length here).
3. **`validate_mission_rules` (`mode="after"`).** Only once every
   field on `SpaceMission`, including the fully-validated `crew` list,
   is in place does the mission's own `@model_validator` run. At this
   point `self.crew` is guaranteed to be a `list[CrewMember]` of
   real, individually-valid objects — the validator can write
   `member.rank in senior_ranks` and `member.years_experience >= 5`
   directly, with no risk of a malformed crew member reaching this
   code.

This means a bad crew member is caught and reported **before** the
mission ever gets to check "is there a commander" or "is everyone
active" — the cheaper, purely local checks always run first, and
expensive cross-record logic only runs on data already known to be
individually well-formed.

### Reading a nested `ValidationError`

If crew member index 1 has `age=15` (below the `ge=18` floor), the
resulting `exc.errors()` entry looks like:

```python
[{
    "type": "greater_than_equal",
    "loc": ("crew", 1, "age"),
    "msg": "Input should be greater than or equal to 18",
    "input": 15,
    "ctx": {"ge": 18},
}]
```

`"loc"` is a tuple that walks the exact path through the model
hierarchy: `"crew"` (the field on `SpaceMission`), `1` (the index into
that list), `"age"` (the field on that `CrewMember`). This is the same
`exc.errors()` structure as the flat, single-level errors in ex0 — it
just has more elements in the tuple once models nest, because `"loc"`
records one path segment per level of nesting crossed. Reading it
right-to-left tells you the field; left-to-right tells you how to get
there.

### The two distinct kinds of `list` constraint

```python
crew: list[CrewMember] = Field(min_length=1, max_length=12)
```

`min_length=1, max_length=12` here bounds *how many* `CrewMember`
elements the list may contain (1 to 12 people) — it says nothing about
any individual member. Compare with `station_id: str =
Field(min_length=3, max_length=10)` in ex0, where the same keyword
names bound *string character count*. Pydantic v2 reuses
`min_length`/`max_length` for both `str` and any sized container
(`list`, `set`, `tuple`) — the meaning is inferred from the annotated
type, not from the keyword name. (The v1 aliases `min_items`/
`max_items` for lists still work but are deprecated in favor of the
unified v2 names.)

## Running

```bash
python3 ex2/space_crew.py   # direct execution
python3 -m ex2.main         # module execution
```

## Expected output

```
Space Mission Crew Validation
=========================================
Valid mission created:
Mission: Mars Colony Establishment
ID: M2024_MARS
Destination: Mars
Duration: 900 days
Budget: $2500.0M
Crew size: 3
Crew members:
  - Sarah Connor (commander) - Mission Command
  - John Smith (lieutenant) - Navigation
  - Alice Johnson (officer) - Engineering
=========================================
Expected validation error:
Mission must have at least one Commander or Captain
```
