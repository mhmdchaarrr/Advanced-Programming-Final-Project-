# Tell make these aren’t real files:
.PHONY: help install run test lint format clean

# Default task
help:
	@echo "Usage:"
	@echo "  make venv      # makes a virtual environment
	@echo "  make install   # install dependencies"
	@echo "  make run       # run the contact‑book app"
	@echo "  make test      # run the test suite"
	@echo "  make lint      # run flake8 and mypy checks"
	@echo "  make format    # auto‑format code (black)"
	@echo "  make clean     # remove temp/build files"

SHELL    := /bin/bash
.ONESHELL:
VENV     := .venv

.PHONY: venv install run test lint format clean

venv:
	python3 -m venv $(VENV)

install: venv
	source $(VENV)/bin/activate
	pip install -r requirements.txt

run:
	source $(VENV)/bin/activate
	python main.py

test:
	source $(VENV)/bin/activate
	pytest --maxfail=1 --disable-warnings -q

# Lint and type‑check
lint:
	source $(VENV)/bin/activate
	flake8 .
	mypy .

# Auto‑format
format:
	source $(VENV)/bin/activate
	black .

# Clean up caches, __pycache__, pyc files, etc.
clean:
	source $(VENV)/bin/activate
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.py[co]" -delete
	rm -rf .pytest_cache/

