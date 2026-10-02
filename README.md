# Adaptive LLM Batching Gateway

Bounded micro-batching for inference requests.

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

POST `{"value":"demo"}` to `/v1/run`.

Local runnable reference; production integrations belong behind explicit adapters.
