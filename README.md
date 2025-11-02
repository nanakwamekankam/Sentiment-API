# Sentiment-API
Sentiment API (FastAPI + Docker + AWS App Runner):

Model: HuggingFace sentiment analysis (simple on purpose).

Containerization: Docker + non-root for reproducible builds.

Reliability: /healthz, structured errors, CloudWatch logs.

Observability: /metrics (Prometheus counters + histograms).

Future work: 

Deployment: AWS App Runner from ECR, HTTPS, autoscaling.

CI/CD: GitHub Actions builds, pushes, deploys on merge to main.

Canary deploys (two App Runner services + weighted DNS).

Feature flags / A/B.

Model registry (MLflow) + signed artifacts in ECR.

Tracing (OpenTelemetry) to X-Ray.
