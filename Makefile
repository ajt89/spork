include .env

setup:
	- python3 -m pipenv install --python=$(PYENV_ROOT)/versions/3.9.12/bin/python --dev

format:
	- python3 -m pipenv run isort .; \
	python3 -m pipenv run black .

type-check:
	- python3 -m pipenv run mypy --namespace-packages .

test:
	- python3 -m pipenv run unittest-parallel -t . -s tests --class-fixtures

test-file:
	- python3 -m pipenv run python -m unittest tests/$(TEST_FILE)

run:
	- python3 -m pipenv run python bot.py
