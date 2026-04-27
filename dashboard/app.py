"""Dashboard FastAPI application."""

import json
from urllib.error import URLError
from urllib.request import urlopen

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from dashboard.components.alerts_table import render_alerts_table
from dashboard.components.impact_view import render_impact_view
from dashboard.components.risk_chart import render_risk_chart

BACKEND_BASE_URL = "http://localhost:8000"

app = FastAPI(title="Operational Resilience Dashboard")


def _fetch_json(path: str) -> dict | list:
    """Fetch JSON from backend endpoint and return decoded body."""
    url = f"{BACKEND_BASE_URL}{path}"
    try:
        with urlopen(url, timeout=2) as response:
            return json.loads(response.read().decode("utf-8"))
    except (URLError, TimeoutError, json.JSONDecodeError):
        return {}


@app.get("/", response_class=HTMLResponse)
def homepage() -> str:
    """Render dashboard homepage populated from backend endpoints."""
    alerts = _fetch_json("/alerts")
    risk_score = _fetch_json("/risk-score")

    alerts_html = render_alerts_table(alerts if isinstance(alerts, list) else [])
    risk_html = render_risk_chart(risk_score if isinstance(risk_score, dict) else {})

    # Impact section is included for layout completeness; data can be wired to POST /simulate-impact.
    impact_html = render_impact_view({})

    return f"""
    <html>
      <head>
        <title>Operational Resilience Dashboard</title>
      </head>
      <body>
        <h1>Operational Resilience Dashboard</h1>

        <section>
          <h2>Current Risk</h2>
          {risk_html}
        </section>

        <section>
          <h2>Active Alerts</h2>
          {alerts_html}
        </section>

        <section>
          <h2>Impact Simulation</h2>
          {impact_html}
        </section>
      </body>
    </html>
    """
"""Dashboard app placeholder module."""


def render_dashboard() -> str:
    """Return placeholder dashboard content."""
    return "Operational Resilience Dashboard"


if __name__ == "__main__":
    print(render_dashboard())
