"""Alert model module."""
"""Alert model placeholder module."""

from dataclasses import dataclass


@dataclass
class Alert:
    """Represents an operational resilience alert."""

    id: str
    source: str
    severity: str
    description: str
    timestamp: str
    category: str
    """Represents an operational alert."""

    id: str
    message: str
    severity: str = "low"
