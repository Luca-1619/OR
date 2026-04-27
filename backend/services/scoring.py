"""Risk scoring service module."""

from dataclasses import asdict
import random

from backend.models.risk_score import RiskScore

SEVERITY_WEIGHTS = {
    "low": 1,
    "medium": 2,
    "high": 3,
}


def calculate_risk_score(
    num_alerts: int,
    average_severity: float,
    volatility_factor: float | None = None,
) -> dict:
    """Calculate a weighted risk score between 0 and 100."""
    if volatility_factor is None:
        volatility_factor = random.uniform(0.8, 1.2)

    alert_component = min(num_alerts * 8, 50)
    severity_component = min((average_severity / SEVERITY_WEIGHTS["high"]) * 35, 35)
    volatility_component = min(max((volatility_factor - 0.8) / 0.4 * 15, 0), 15)

    score = round(min(alert_component + severity_component + volatility_component, 100), 2)

    if score >= 70:
        level = "high"
    elif score >= 40:
        level = "medium"
    else:
        level = "low"

    rationale = (
        f"Computed from {num_alerts} alerts, average severity {average_severity:.2f}, "
        f"and volatility factor {volatility_factor:.2f}."
    )

    return asdict(RiskScore(score=score, level=level, rationale=rationale))
