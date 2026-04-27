"""Alerts API placeholder module."""


def list_alerts() -> list[dict]:
    """Return sample alerts for API responses."""
    return [
        {"id": "ALT-001", "message": "Core payment latency spike", "severity": "high"},
        {"id": "ALT-002", "message": "Backup job delayed", "severity": "medium"},
    ]
