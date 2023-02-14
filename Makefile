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

amend-and-push:
	git add .
	git commit --amend --no-edit
	git push --force

dev:
	poetry run flask --app gendiff:app run

PORT ?= 8000
start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) gendiff:app

ALL: lint install coverage-missing build package-install