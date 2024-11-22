.PHONY: lint test

lint:
	blue . && isort .

test: lint
	pytest -s -x --cov=src -vv