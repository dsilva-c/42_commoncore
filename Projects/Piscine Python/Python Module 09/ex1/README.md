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

## Key Pydantic concept

```python
@model_validator(mode="after")
def validate_contact_rules(self) -> AlienContact:
    # all fields are already validated — access via self.*
    if not self.contact_id.startswith("AC"):
        raise ValueError("Contact ID must start with 'AC'")
    return self   # always return self
```

`mode="after"` means the validator receives a fully constructed model
instance.  Always `return self` at the end.  This replaces the
deprecated `@validator` decorator from Pydantic v1.

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
