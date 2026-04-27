"""ImpactResult model placeholder module."""

from dataclasses import dataclass, field


@dataclass
class ImpactResult:
    """Represents the result of an impact simulation."""

    scenario: str
    impact_level: str
    details: list[str] = field(default_factory=list)
