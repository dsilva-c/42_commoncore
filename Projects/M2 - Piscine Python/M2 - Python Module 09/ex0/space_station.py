"""Exercise 0: Space Station Data — Pydantic model with field validation.

Objective: Learn basic Pydantic model creation with BaseModel and
Field validation. Demonstrates automatic type coercion, field
constraints, and clear validation error messages.

Authorized: pydantic, datetime
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Pydantic model for space station monitoring data.

    The Observatory monitors hundreds of space stations across the
    galaxy. Each station reports vital statistics including crew size,
    power levels, and operational status.
    """

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    """Demonstrate SpaceStation validation with valid and invalid data."""
    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.fromisoformat("2024-01-15T10:30:00"),
    )

    status = "Operational" if station.is_operational else "Off-line"
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")
    print("=" * 40)

    try:
        SpaceStation(
            station_id="INVALID1",
            name="Bad Station",
            crew_size=25,
            power_level=80.0,
            oxygen_level=90.0,
            last_maintenance=datetime.fromisoformat(
                "2024-01-01T00:00:00"
            ),
        )
    except ValidationError as exc:
        print("Expected validation error:")
        for error in exc.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
