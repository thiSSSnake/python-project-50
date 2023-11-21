install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

selfcheck:
	poetry check

check: selfcheck test lint

gendiff:
	poetry run gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

.PHONY: install test lint selfcheck check build