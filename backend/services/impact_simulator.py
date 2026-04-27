"""Impact simulation service module."""

from dataclasses import asdict

from backend.models.impact_result import ImpactResult

SEVERITY_MULTIPLIER = {
    "low": 0.75,
    "medium": 1.0,
    "high": 1.5,
}


def simulate_impact(scenario: str, severity: str, affected_systems: list[str]) -> dict:
    """Run a simple scenario engine and return impact estimates."""
    severity_key = severity.lower()
    multiplier = SEVERITY_MULTIPLIER.get(severity_key, SEVERITY_MULTIPLIER["medium"])
    systems_count = max(len(affected_systems), 1)

    base_loss = 25000.0
    estimated_loss = round(base_loss * multiplier * systems_count, 2)
    recovery_time_hours = round(2.0 * multiplier * systems_count, 1)

    result = ImpactResult(
        scenario=scenario,
        estimated_loss=estimated_loss,
        affected_systems=affected_systems,
        recovery_time_hours=recovery_time_hours,
    )
    return asdict(result)
