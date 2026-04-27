"""ImpactResult model module."""

from dataclasses import dataclass
"""ImpactResult model placeholder module."""

from dataclasses import dataclass, field


@dataclass
class ImpactResult:
    """Represents the result of a scenario impact simulation."""

    scenario: str
    estimated_loss: float
    affected_systems: list[str]
    recovery_time_hours: float
    """Represents the result of an impact simulation."""

    scenario: str
    impact_level: str
    details: list[str] = field(default_factory=list)
