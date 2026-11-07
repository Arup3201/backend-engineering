.PHONY: check

check:
	ruff check .
	mypy main-project/app
	pytest -q