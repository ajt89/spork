include .env

setup:
	- pipenv install --python=$(PYENV_ROOT)/versions/3.7.10/bin/python --dev

format:
	- pipenv run isort .; \
	pipenv run black .

test:
	- pipenv run unittest-parallel -t . -s tests

test-file:
	- pipenv run unittest tests/$(TEST_FILE)

run:
	- pipenv run bot.py
