.PHONY: lint test

lint:
	blue .

test: lint
	pytest -s -x --cov=src -vv

build:
	docker compose up --build

db:
	docker compose up --force-recreate db