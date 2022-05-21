.PHONY: test
.PHONY: dev pre-commit isort black mypy flake8 pylint lint

dev: pre-commit

pre-commit:
	pre-commit install
	pre-commit autoupdate

isort:
	isort . --profile black

black:
	black .

mypy:
	mypy -p sqlite_to_postgres

flake8:
	flake8 .

pylint:
	pylint movies_admin sqlite_to_postgres

lint: isort black mypy flake8 pylint





