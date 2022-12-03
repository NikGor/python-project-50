install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=src --cov-report=term-missing

lint:
	poetry run flake8 gendiff

check:
	selfcheck test lint

build:
	poetry build

draw:
	poetry run draw
