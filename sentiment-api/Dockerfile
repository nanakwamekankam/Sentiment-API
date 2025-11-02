# FROM python:3.11-slim
FROM python:3.11-slim-bookworm


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps for torch/transformers wheels if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential curl --fix-missing && \
#     rm -rf /var/lib/apt/lists/*

# RUN rm -rf /var/lib/apt/lists/* \
#  && apt-get clean \
#  && apt-get update \
#  && apt-get install -y --no-install-recommends build-essential curl \
#  && rm -rf /var/lib/apt/lists/*

# RUN apt-get clean && \
#     rm -rf /var/lib/apt/lists/* && \
#     apt-get update && \
#     apt-get install -y --no-install-recommends curl && \
#     rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app ./app

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
