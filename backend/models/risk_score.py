"""RiskScore model placeholder module."""

from dataclasses import dataclass


@dataclass
class RiskScore:
    """Represents a calculated risk score."""

    entity_id: str
    score: float
    rationale: str = "placeholder"
