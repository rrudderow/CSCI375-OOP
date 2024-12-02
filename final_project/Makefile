DOCS = docs

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

.PHONY: create-docs
create-docs:
	# creates .md in docs
	pdoc -o ./docs *.py
	@echo "html docs created and saved in $(DOCS)"

.PHONY: test
run-test:
	pytest --verbose --color=yes --cov --cov-report term --cov-report html tests/

.PHONY: uml
uml:
	plantuml uml/inventory.plantuml

.PHONY: clean
clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .pytest_cache` 
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf *.pyc