"""FastAPI entry point for the Operational Resilience Engine backend."""

from fastapi import FastAPI

from backend.api.alerts import list_alerts
from backend.services.impact_simulator import simulate_impact
from backend.services.scoring import SEVERITY_WEIGHTS, calculate_risk_score

app = FastAPI(title="Operational Resilience Engine API")


@app.get("/")
def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/alerts")
def get_alerts() -> list[dict]:
    """Return sample alerts."""
    return list_alerts()


@app.get("/risk-score")
def get_risk_score() -> dict:
    """Compute risk score from the currently available alerts."""
    alerts = list_alerts()
    num_alerts = len(alerts)
    avg_severity = (
        sum(SEVERITY_WEIGHTS.get(alert["severity"], SEVERITY_WEIGHTS["low"]) for alert in alerts)
        / max(num_alerts, 1)
    )
    return calculate_risk_score(num_alerts=num_alerts, average_severity=avg_severity)


@app.post("/simulate-impact")
def post_simulate_impact(payload: dict) -> dict:
    """Run impact simulation with request JSON body."""
    scenario = payload.get("scenario", "Unnamed Scenario")
    severity = payload.get("severity", "medium")
    systems = payload.get("systems") or []
    return simulate_impact(scenario=scenario, severity=severity, affected_systems=systems)
