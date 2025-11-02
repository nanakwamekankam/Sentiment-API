# Sentiment-API
Sentiment API (FastAPI + Docker + AWS App Runner): 
Model: HuggingFace sentiment analysis (simple on purpose).
Containerization: Docker + non-root for reproducible builds.
Reliability: /healthz, structured errors, CloudWatch logs.
Observability: /metrics (Prometheus counters + histograms).
