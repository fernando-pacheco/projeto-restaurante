ISORT_OPTIONS = --profile black --line-length 79

.PHONY: lint test
lint:
	blue . && isort . $(ISORT_OPTIONS)
test: lint
	pytest -s -x --cov=src -vv
build:
	docker compose up --build
db:
	docker compose up --force-recreate db