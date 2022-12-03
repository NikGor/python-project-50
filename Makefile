install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=src --cov-report xml

coverage-missing:
	poetry run pytest --cov-report term-missing --cov=src

lint:
	poetry run flake8 src

check:
	selfcheck test lint

build:
	poetry build

draw:
	poetry run draw

selfcheck:
	poetry check
