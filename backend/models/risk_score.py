"""RiskScore model module."""

from dataclasses import dataclass


@dataclass
class RiskScore:
    """Represents a calculated risk score output."""

    score: float
    level: str
    rationale: str
