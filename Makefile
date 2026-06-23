PYTHON := python3
FLAKE8 := $(PYTHON) -m flake8

.PHONY: flake8 clean

flake8:
	@$(FLAKE8) ex*/*.py && echo "flake8: all clean"

clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name '*.pyc' -delete
