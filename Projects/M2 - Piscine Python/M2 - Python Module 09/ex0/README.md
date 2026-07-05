# ex0 — Space Station Data

## Goal

Create a **Pydantic `BaseModel`** to validate incoming space station
telemetry, demonstrating automatic type coercion (e.g. string
timestamps → `datetime`) and field-level constraint validation.

## Files

| File | Role |
|------|------|
| `space_station.py` | `SpaceStation` model + `main()` demonstration |
| `main.py` | Module-style entry-point |

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

## Key Pydantic concepts

- **`BaseModel`** — inherit to get validated, immutable data objects.
- **`Field(...)`** — attach `min_length`, `max_length`, `ge`, `le`
  constraints declaratively.
- **Automatic coercion** — passing `"2024-01-15T10:30:00"` to a
  `datetime` field works without manual parsing.  Pydantic converts
  compatible types at model construction time.
- **`ValidationError`** — raised on invalid input; iterate
  `exc.errors()` for structured error details.

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
