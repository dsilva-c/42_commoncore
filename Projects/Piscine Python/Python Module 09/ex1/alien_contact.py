"""Exercise 1: Alien Contact Logs — custom validation with model_validator.

Objective: Master custom validation using @model_validator for complex
business rules. Validates alien contact reports with sophisticated rules
that go beyond simple field constraints.

Authorized: pydantic, datetime, enum
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Enumeration of alien contact types."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Pydantic model for alien contact reports.

    Includes custom business-rule validation via model_validator to
    ensure report integrity across different contact types.
    """

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(
        default=None, max_length=500
    )
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_rules(self) -> AlienContact:
        """Enforce business rules for alien contact reports.

        Rules:
        - Contact ID must start with 'AC' (Alien Contact).
        - Physical contact reports must be verified.
        - Telepathic contact requires at least 3 witnesses.
        - Strong signals (> 7.0) should include received messages.
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)"
            )
        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError(
                "Physical contact reports must be verified"
            )
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if (
            self.signal_strength > 7.0
            and self.message_received is None
        ):
            raise ValueError(
                "Strong signals (> 7.0) should include"
                " received messages"
            )
        return self


def main() -> None:
    """Demonstrate AlienContact validation with valid and invalid data."""
    print("Alien Contact Log Validation")
    print("=" * 38)

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.fromisoformat("2024-03-15T22:30:00"),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=False,
    )

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")
    print("=" * 38)

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.fromisoformat("2024-05-20T03:15:00"),
            location="Atacama Desert, Chile",
            contact_type=ContactType.telepathic,
            signal_strength=6.5,
            duration_minutes=30,
            witness_count=1,
            message_received=None,
            is_verified=False,
        )
    except ValidationError as exc:
        print("Expected validation error:")
        for error in exc.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
