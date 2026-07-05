"""Exercise 2: Space Crew Management — nested Pydantic models.

Objective: Master nested Pydantic models and complex data relationships.
Validates space missions and their crew against safety and operational
requirements before launch approval.

Authorized: pydantic, datetime, enum
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Enumeration of crew member ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Pydantic model for individual space crew members."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Pydantic model for space missions with nested crew validation.

    Validates that each mission meets safety and operational criteria
    before being approved for launch.
    """

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> SpaceMission:
        """Enforce safety and operational mission requirements.

        Rules:
        - Mission ID must start with 'M'.
        - Must have at least one Commander or Captain.
        - Long missions (> 365 days) need 50% experienced crew
          (5+ years).
        - All crew members must be active.
        """
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        senior_ranks = {Rank.commander, Rank.captain}
        has_senior = any(
            member.rank in senior_ranks for member in self.crew
        )
        if not has_senior:
            raise ValueError(
                "Mission must have at least one Commander"
                " or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1
                for member in self.crew
                if member.years_experience >= 5
            )
            required = len(self.crew) * 0.5
            if experienced_count < required:
                raise ValueError(
                    "Long missions (> 365 days) require 50%"
                    " experienced crew (5+ years experience)"
                )

        inactive = [m for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Demonstrate SpaceMission nested validation with crew details."""
    print("Space Mission Crew Validation")
    print("=" * 41)

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2024-06-01T08:00:00"),
        duration_days=900,
        crew=[
            CrewMember(
                member_id="SC001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=38,
                specialization="Mission Command",
                years_experience=12,
            ),
            CrewMember(
                member_id="JS002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=32,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="AJ003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=29,
                specialization="Engineering",
                years_experience=6,
            ),
        ],
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"  - {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )
    print("=" * 41)

    try:
        SpaceMission(
            mission_id="M2024_VENUS",
            mission_name="Venus Atmosphere Study",
            destination="Venus",
            launch_date=datetime.fromisoformat(
                "2024-09-01T12:00:00"
            ),
            duration_days=180,
            crew=[
                CrewMember(
                    member_id="TK001",
                    name="Tom Kim",
                    rank=Rank.officer,
                    age=27,
                    specialization="Science Officer",
                    years_experience=3,
                ),
            ],
            budget_millions=500.0,
        )
    except ValidationError as exc:
        print("Expected validation error:")
        for error in exc.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
