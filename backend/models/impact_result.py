"""ImpactResult model module."""

from dataclasses import dataclass


@dataclass
class ImpactResult:
    """Represents the result of a scenario impact simulation."""

    scenario: str
    estimated_loss: float
    affected_systems: list[str]
    recovery_time_hours: float
