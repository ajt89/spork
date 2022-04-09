include .env

setup:
	- python3 -m pipenv install --python=$(PYENV_ROOT)/versions/3.7.10/bin/python --dev

format:
	- python3 -m pipenv run isort .; \
	python3 -m pipenv run black .

test:
	- python3 -m pipenv run unittest-parallel -t . -s tests

test-file:
	- python3 -m pipenv run unittest tests/$(TEST_FILE)

run:
	- python3 -m pipenv run bot.py
