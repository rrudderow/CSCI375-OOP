.PHONY: all
all: check-style check-type unittest local_test clean
	@echo "All done."

.PHONY: check-style
check-style:
	@echo "Checking style with flake8"
	flake8 .

.PHONY: check-type
check-type:
	@echo "run mypy"
	mypy --disallow-untyped-defs --strict .

.PHONY: unittest
unittest:
	@echo "run pytest"
	pytest --verbose --color=yes --cov --cov-report term-missing --cov-report html .

.PHONY: local_test
local_test:
	@echo "run kattis testing"
	kattis test

.PHONY: html-doc
html-doc:
	pydoc -w ./*py

.PHONY: uml
uml:
	plantuml uml/inventory.plantuml

.PHONY: clean
clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache` 
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf *.pyc