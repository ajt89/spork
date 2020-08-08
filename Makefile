include .env
export

clean:
	- rm -rf .venv

setup:
	- python3 -m venv .venv; \
	. .venv/bin/activate; \
	pip install -r requirements-dev.txt; \
	pip install -r requirements.txt

update:
	- . .venv/bin/activate; \
	pip install -r requirements-dev.txt; \
	pip install -r requirements.txt

format:
	- . .venv/bin/activate; \
	isort .; \
	black .

test:
	- . .venv/bin/activate; \
	unittest-parallel -t . -s tests

test-file:
	- . .venv/bin/activate; \
	python -m unittest tests/$(TEST_FILE)

run:
	- . .venv/bin/activate; \
	python bot.py

