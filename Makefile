install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 gendiff

check:
	selfcheck test lint

build:
	poetry build

draw:
	poetry run draw
