"""Impact view rendering component."""


def render_impact_view(result: dict) -> str:
    """Render impact simulation details as simple HTML."""
    if not result:
        return "<p>No impact simulation data.</p>"

    return (
        "<div>"
        f"<p><strong>Scenario:</strong> {result.get('scenario', 'n/a')}</p>"
        f"<p><strong>Estimated Loss:</strong> ${result.get('estimated_loss', 'n/a')}</p>"
        f"<p><strong>Recovery Time (hours):</strong> {result.get('recovery_time_hours', 'n/a')}</p>"
        "</div>"
    )
