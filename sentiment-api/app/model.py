from transformers import pipeline
import threading

_model_lock = threading.Lock()
_model = None

def get_pipeline():
    global _model
    if _model is None:
        with _model_lock:
            if _model is None:
                _model = pipeline("sentiment-analysis")
    return _model

def predict(text: str):
    pipeline = get_pipeline()
    output = pipeline(text)[0]
    return {"label": output["label"], "score": float(output["score"])}
