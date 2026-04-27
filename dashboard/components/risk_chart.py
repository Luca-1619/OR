"""Risk chart rendering component."""


def render_risk_chart(score: dict) -> str:
    """Render risk score and level as simple HTML."""
    if not score:
        return "<p>Risk score unavailable.</p>"

    return (
        "<div>"
        f"<p><strong>Risk Score:</strong> {score.get('score', 'n/a')}</p>"
        f"<p><strong>Level:</strong> {score.get('level', 'n/a')}</p>"
        f"<p><strong>Rationale:</strong> {score.get('rationale', 'n/a')}</p>"
        "</div>"
    )
"""Risk chart component placeholder module."""


def render_risk_chart() -> str:
    """Return placeholder risk chart."""
    return "Risk chart placeholder"
