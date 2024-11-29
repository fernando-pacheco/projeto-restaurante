ISORT_OPTIONS = --profile black --line-length 79

cleanup:
	clear
lint: cleanup
	blue . && isort . $(ISORT_OPTIONS)
test: cleanup lint
	pytest -s -x --cov=src -vv
build: cleanup
	docker compose up --build
db: cleanup
	docker compose up --force-recreate db