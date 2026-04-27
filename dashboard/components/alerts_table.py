"""Alerts table rendering component."""


def render_alerts_table(alerts: list[dict]) -> str:
    """Render alerts as an HTML table."""
    if not alerts:
        return "<p>No alerts available.</p>"

    header = """
    <table border='1' cellpadding='6' cellspacing='0'>
      <thead>
        <tr>
          <th>ID</th><th>Source</th><th>Severity</th><th>Category</th><th>Timestamp</th><th>Description</th>
        </tr>
      </thead>
      <tbody>
    """
    rows = []
    for alert in alerts:
        rows.append(
            "<tr>"
            f"<td>{alert.get('id', '')}</td>"
            f"<td>{alert.get('source', '')}</td>"
            f"<td>{alert.get('severity', '')}</td>"
            f"<td>{alert.get('category', '')}</td>"
            f"<td>{alert.get('timestamp', '')}</td>"
            f"<td>{alert.get('description', '')}</td>"
            "</tr>"
        )

    footer = "</tbody></table>"
    return header + "".join(rows) + footer
