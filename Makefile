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

make lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
