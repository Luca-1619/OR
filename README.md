# Operational Resilience Engine

Initial project scaffold for an Operational Resilience Engine.

## Structure

- `backend/`: Backend services, APIs, domain models, and utilities.
- `dashboard/`: Dashboard entrypoint and UI components.

All files currently include minimal placeholder code to support iterative development.

## Backend API (FastAPI)

Install dependencies and run the API:

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Available endpoints:

- `GET /` health check
- `GET /alerts`
- `GET /risk-score`
- `POST /simulate-impact`
