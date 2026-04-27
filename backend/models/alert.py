"""Alert model placeholder module."""

from dataclasses import dataclass


@dataclass
class Alert:
    """Represents an operational alert."""

    id: str
    message: str
    severity: str = "low"
