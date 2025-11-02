IMAGE?=sentiment-api
TAG?=local

build:
	docker build -t $(IMAGE):$(TAG) .

run:
	docker run --rm -p 8080:8080 $(IMAGE):$(TAG)

test:
	pytest -q
