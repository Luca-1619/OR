"""Alerts API module."""

from dataclasses import asdict

from backend.models.alert import Alert


def list_alerts() -> list[dict]:
    """Return realistic sample alerts for API responses."""
    alerts = [
        Alert(
            id="ALT-1001",
            source="payments-gateway",
            severity="high",
            description="Transaction timeout rate exceeded 7% for 10 minutes.",
            timestamp="2026-04-27T18:05:00Z",
            category="availability",
        ),
        Alert(
            id="ALT-1002",
            source="identity-service",
            severity="medium",
            description="Authentication latency above SLO threshold.",
            timestamp="2026-04-27T18:12:00Z",
            category="performance",
        ),
        Alert(
            id="ALT-1003",
            source="data-warehouse",
            severity="low",
            description="ETL freshness delayed by 15 minutes.",
            timestamp="2026-04-27T18:20:00Z",
            category="data-quality",
        ),
        Alert(
            id="ALT-1004",
            source="network-edge",
            severity="high",
            description="Packet loss spike detected in us-east region.",
            timestamp="2026-04-27T18:24:00Z",
            category="network",
        ),
        Alert(
            id="ALT-1005",
            source="vendor-api",
            severity="medium",
            description="Third-party dependency returned elevated 5xx errors.",
            timestamp="2026-04-27T18:31:00Z",
            category="third-party",
        ),
    ]
    return [asdict(alert) for alert in alerts]
"""Alerts API placeholder module."""


def list_alerts() -> list[dict]:
    """Return sample alerts for API responses."""
    return [
        {"id": "ALT-001", "message": "Core payment latency spike", "severity": "high"},
        {"id": "ALT-002", "message": "Backup job delayed", "severity": "medium"},
    ]
