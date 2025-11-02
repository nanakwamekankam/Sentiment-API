from fastapi import FastAPI, HTTPException
from app.schemas import PredictIn, PredictOut
from app.model import predict
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import PlainTextResponse
import time

app = FastAPI(title="Sentiment API", version="1.0.0")

REQ_CT = Counter("requests_total", "Total API requests", ["endpoint", "status"])
LAT_HIST = Histogram("request_latency_seconds", "Request latency", ["endpoint"])

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictOut)
def predict_route(body: PredictIn):
    start = time.time()
    try:
        result = predict(body.text)
        REQ_CT.labels(endpoint="/predict", status="200").inc()
        return PredictOut(**result)
    except Exception as e:
        REQ_CT.labels(endpoint="/predict", status="500").inc()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        LAT_HIST.labels(endpoint="/predict").observe(time.time() - start)

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)
