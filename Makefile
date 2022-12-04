install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

coverage-missing:
	poetry run pytest --cov-report term-missing --cov=gendiff

lint:
	poetry run flake8 gendiff

check: selfcheck test lint

build:
	poetry build

draw:
	poetry run draw

selfcheck:
	poetry check

ALL: lint install coverage-missing build package-install