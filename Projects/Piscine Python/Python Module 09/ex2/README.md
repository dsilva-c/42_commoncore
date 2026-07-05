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

## Key Pydantic concept: nested models

Pydantic automatically validates each `CrewMember` when constructing
the parent `SpaceMission`.  If any crew member fails its own field
constraints, `ValidationError` is raised before the mission
`model_validator` even runs.

```python
crew: list[CrewMember] = Field(min_length=1, max_length=12)
```

`min_length` / `max_length` on a `list` field validates the *list
size*, not the string content.

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
