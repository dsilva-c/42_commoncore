# ex1 — Alien Contact Logs

## Goal

Use **`@model_validator(mode='after')`** to implement custom business
rules that run after Pydantic's built-in field validation.  Validates
multi-field relationships and domain-specific constraints for alien
contact reports.

## Files

<div align="center">

| File | Role |
|------|------|
| `alien_contact.py` | `ContactType` enum + `AlienContact` model + `main()` |
| `main.py` | Module-style entry-point |

</div>

## Model design

```
ContactType (str Enum)
  radio | visual | physical | telepathic

AlienContact
├── contact_id:       str         (5-15 chars)
├── timestamp:        datetime
├── location:         str         (3-100 chars)
├── contact_type:     ContactType
├── signal_strength:  float       (0.0-10.0)
├── duration_minutes: int         (1-1440, max 24 h)
├── witness_count:    int         (1-100 people)
├── message_received: str | None  (max 500 chars)
└── is_verified:      bool        (default False)
```

## Business rules (model_validator)

<div align="center">

| Rule | Condition |
|------|-----------|
| ID prefix | `contact_id` must start with `"AC"` |
| Physical verification | `physical` contacts must have `is_verified=True` |
| Telepathic witnesses | `telepathic` contacts need ≥ 3 witnesses |
| Strong signal message | `signal_strength > 7.0` requires a message |

</div>

## Concepts explained

### Why cross-field rules can't live in `Field(...)`

`Field(ge=…, le=…)` constrains one field in isolation — it has no
notion of *another* field's value. But "a `physical` contact must have
`is_verified=True`" and "`telepathic` contacts need ≥ 3 witnesses" are
rules about the *relationship* between `contact_type` and another
field. `AlienContact` needs a hook that runs after individual fields
are validated but before construction finishes, with access to the
whole object. That hook is `@model_validator(mode="after")`.

### `mode="after"` vs `mode="before"`

Pydantic v2 offers both:

- `mode="before"` runs first, before any field validation, and
  receives the **raw input** (typically a `dict`) — useful for
  reshaping or defaulting raw data ahead of type coercion, but at that
  point you don't yet have a `ContactType` enum member or a coerced
  `float`; you only have whatever the caller passed in (a string, a
  number, anything).
- `mode="after"` runs last, once every field has individually passed
  its own `Field(...)` constraints *and* been coerced to its declared
  type, and receives `self` — a fully-typed `AlienContact` instance.

`validate_contact_rules` uses `mode="after"` specifically because its
checks need typed data: `self.contact_type == ContactType.physical` is
an enum comparison, `self.witness_count < 3` is an integer comparison,
`self.signal_strength > 7.0` is a float comparison. None of that is
reliable against raw, not-yet-coerced input — a `mode="before"`
validator would still be looking at whatever the caller passed (a
string `"telepathic"`, a stringified number, etc.) and would have to
redo type conversion itself. `mode="after"` lets the validator assume
Pydantic already did that work correctly.

### Tracing the telepathic-witness rule end-to-end

`main()`'s second call constructs:

```python
AlienContact(
    contact_id="AC_2024_002",
    contact_type=ContactType.telepathic,
    witness_count=1,
    ...
)
```

Construction proceeds in two phases:

1. **Field phase.** Pydantic checks each field's own constraint:
   `contact_id` length is fine, `witness_count=1` satisfies
   `Field(ge=1, le=100)` (1 is a valid witness *count*, just not
   enough for *this* contact type — that distinction is exactly why
   this can't be a `Field` constraint), `contact_type="telepathic"` is
   coerced to `ContactType.telepathic`. All fields pass individually,
   so Pydantic proceeds to build the model instance.
2. **Model phase.** `validate_contact_rules(self)` now runs with `self`
   fully populated. It reaches
   `if self.contact_type == ContactType.telepathic and self.witness_count < 3:`,
   which is `True`, and raises
   `ValueError("Telepathic contact requires at least 3 witnesses")`.

Pydantic catches that `ValueError` and wraps it into a
`ValidationError` reported by the outer `except` in `main()` — a
validator body raises plain `ValueError`, never `ValidationError`
itself; Pydantic does the wrapping so all error reporting (field-level
and model-level) goes through the same `exc.errors()` shape.

### Why `return self` is mandatory

```python
@model_validator(mode="after")
def validate_contact_rules(self) -> AlienContact:
    ...
    return self
```

In `mode="after"`, whatever the validator function returns **becomes**
the final model instance — Pydantic doesn't assume you meant `self` if
you return something else. Returning `None` (e.g. forgetting the
`return self` line, since a Python function with no `return`
implicitly returns `None`) means the constructor's result is `None`
instead of an `AlienContact`, which Pydantic detects as invalid and
raises a `TypeError` at construction time. Returning a different
object entirely would silently substitute it as the "validated"
instance. Practically: every branch that doesn't raise must fall
through to `return self` at the very end, exactly once.

### Why this replaces the v1 `@validator`

Pydantic v1's `@validator` decorator ran per-field, received raw
values (not model instances), and needed `@root_validator` as a
separate, differently-shaped API for cross-field checks. Pydantic v2
unifies both cases under `@model_validator`: `mode="before"` covers
what `@root_validator(pre=True)` did, and `mode="after"` covers both
per-field post-checks and cross-field business rules like the ones
here, with one consistent decorator and a typed `self` instead of a
loosely-typed `values` dict. `@validator` and `@root_validator` still
work in v2 for backward compatibility but are deprecated — this
exercise uses `@model_validator` exclusively.

### The enum's role before the validator ever runs

`ContactType(str, Enum)` means an unrecognized string such as
`contact_type="beaming"` fails at the **field phase**, before
`validate_contact_rules` is even reached — Pydantic rejects it as an
invalid enum member with its own `ValidationError`, so the model
validator can safely assume `self.contact_type` is always one of the
four defined members.

## Running

```bash
python3 ex1/alien_contact.py   # direct execution
python3 -m ex1.main            # module execution
```

## Expected output

```
Alien Contact Log Validation
======================================
Valid contact report:
ID: AC_2024_001
Type: radio
Location: Area 51, Nevada
Signal: 8.5/10
Duration: 45 minutes
Witnesses: 5
Message: 'Greetings from Zeta Reticuli'
======================================
Expected validation error:
Telepathic contact requires at least 3 witnesses
```
