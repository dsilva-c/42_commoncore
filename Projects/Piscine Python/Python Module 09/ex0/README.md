# ex0 — Space Station Data

## Goal

Create a **Pydantic `BaseModel`** to validate incoming space station
telemetry, demonstrating automatic type coercion (e.g. string
timestamps → `datetime`) and field-level constraint validation.

## Files

<div align="center">

| File | Role |
|------|------|
| `space_station.py` | `SpaceStation` model + `main()` demonstration |
| `main.py` | Module-style entry-point |

</div>

## Model design

```
SpaceStation
├── station_id:       str   (3-10 chars)
├── name:             str   (1-50 chars)
├── crew_size:        int   (1-20 people)
├── power_level:      float (0.0-100.0 %)
├── oxygen_level:     float (0.0-100.0 %)
├── last_maintenance: datetime
├── is_operational:   bool  (default True)
└── notes:            str | None (max 200 chars)
```

## Concepts explained

### Declarative constraints instead of manual `if` checks

Without Pydantic, validating `SpaceStation` telemetry would mean
writing a constructor (or a stack of `if` statements after the fact)
for every field:

```python
if not (1 <= crew_size <= 20):
    raise ValueError("crew_size out of range")
if not (3 <= len(station_id) <= 10):
    raise ValueError("station_id wrong length")
# ...repeat for every field, every place data enters the system
```

This scales badly: the checks live wherever someone remembered to put
them, they can be skipped by constructing the object a different way,
and every call site that builds a `SpaceStation` has to trust that
whoever wrote it also wrote the checks. `space_station.py` instead
declares the rule *on the field itself*:

```python
crew_size: int = Field(ge=1, le=20)
station_id: str = Field(min_length=3, max_length=10)
```

`Field(...)` attaches metadata that Pydantic's generated `__init__`
consults on **every** construction path — keyword arguments,
`model_validate()`, `model_validate_json()`, etc. There is no code path
that creates a `SpaceStation` instance while bypassing the constraint:
if `crew_size=25` is passed, the object is never created at all. This
is the core difference from a manual `if`: the guarantee is structural
(enforced by the type itself) rather than procedural (enforced by
whichever function happens to call the check). `power_level` and
`oxygen_level` reuse the same `ge=/le=` mechanism for `float` fields,
and `notes` combines `max_length=200` with `default=None` to make an
optional, still-bounded field.

### Automatic type coercion

`last_maintenance: datetime` has no `Field(...)` at all, yet it still
validates: Pydantic inspects the *annotation* and looks for a coercion
path from whatever value is supplied to that Python type. Passing an
already-constructed `datetime.fromisoformat("2024-01-15T10:30:00")`
object needs no coercion — it already satisfies the type. But Pydantic
would accept the raw ISO-8601 string `"2024-01-15T10:30:00"` directly
too, converting it to a `datetime` internally before the field is ever
read, because `datetime` has a registered parsing path in Pydantic
core. The same mechanism converts `"85.5"` to `85.5` for `power_level`
or `"true"`/`1` to `True` for `is_operational`. `main()` passes a real
`datetime` object rather than the ISO string purely so static checkers
(mypy/Pylance) — which have no notion of Pydantic's runtime coercion
and only see the declared parameter type — don't flag the call; at
runtime, either form works identically.

### What a `ValidationError` actually contains

Constraint violations don't raise a bare `ValueError` — Pydantic
raises `pydantic.ValidationError`, a structured, machine-readable
report. Calling `exc.errors()` returns a list of dicts, one per failed
field, e.g. for `crew_size=25`:

```python
[{
    "type": "less_than_equal",
    "loc": ("crew_size",),
    "msg": "Input should be less than or equal to 20",
    "input": 25,
    "ctx": {"le": 20},
}]
```

`"loc"` is a tuple naming the exact field path (useful once models
nest, see ex2), `"msg"` is the human-readable message printed by
`main()`, `"type"` is a stable machine-readable error code you can
branch on without string-matching `"msg"`, and `"ctx"` carries the
constraint's own parameters. Because validation happens once, at
construction, and produces this single structured object listing
*every* failing field at once (not just the first `if` that happened
to trip), callers get a complete picture of what was wrong in one
exception instead of fixing one field, resubmitting, and hitting the
next `if` down the line.

## Running

```bash
# from the module root
python3 ex0/space_station.py   # direct execution
python3 -m ex0.main            # module execution
```

## Expected output

```
Space Station Data Validation
========================================
Valid station created:
ID: ISS001
Name: International Space Station
Crew: 6 people
Power: 85.5%
Oxygen: 92.3%
Status: Operational
========================================
Expected validation error:
Input should be less than or equal to 20
```
