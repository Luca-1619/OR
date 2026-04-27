"""FastAPI entry point for the Operational Resilience Engine backend."""

from fastapi import FastAPI

from backend.api.alerts import list_alerts
from backend.services.impact_simulator import simulate_impact
from backend.services.scoring import calculate_risk_score

app = FastAPI(title="Operational Resilience Engine API")


@app.get("/")
def health_check() -> dict:
    """Simple health check endpoint."""
    return {"status": "ok"}


@app.get("/alerts")
def get_alerts() -> dict:
    """Return sample alerts."""
    return {"alerts": list_alerts()}


@app.get("/risk-score")
def get_risk_score() -> dict:
    """Return placeholder risk score."""
    return {"risk_score": calculate_risk_score()}


@app.post("/simulate-impact")
def post_simulate_impact() -> dict:
    """Return placeholder impact simulation results."""
    return {"result": simulate_impact()}
