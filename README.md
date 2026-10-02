# Adaptive LLM Batching Gateway

A production-oriented FastAPI reference service for grouping LLM requests into bounded batches. The demo keeps the batching logic deterministic and dependency-free so it runs locally without cloud credentials.

## Architecture
- FastAPI API layer with health and execution endpoints
- Stateful bounded batch accumulator
- Deterministic request transformation for local testing
- Docker and GitHub Actions CI
- Designed to evolve toward provider-specific async queues, token-aware limits, deadlines, and backpressure

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Then POST `{"value":"hello"}` to `/v1/run`.

## Production extensions
Replace the in-memory accumulator with an async queue, add token/request limits, max-wait deadlines, provider adapters, retries, metrics, and distributed coordination.
