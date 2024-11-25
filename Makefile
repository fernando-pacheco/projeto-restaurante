.PHONY: lint test

lint:
	blue .

test: lint
	pytest -s -x --cov=src -vv