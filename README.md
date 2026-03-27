# Sample App

FastAPI application with health check endpoints.

## Run locally

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Endpoints

- `GET /` - Status
- `GET /healthz` - Liveness probe
- `GET /readyz` - Readiness probe
