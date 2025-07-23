# Makefile for Contact Book

# Default Python command
PYTHON = python

# Default run target
run:
	$(PYTHON) main.py

# Run tests (if using pytest)
test:
	pytest

# Remove generated files
clean:
	rm -f *.pyc
	rm -rf __pycache__
	rm -f user_config.txt
	rm -f *_contacts.txt
