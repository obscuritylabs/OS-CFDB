# Configurable Variables

VENV := .venv

# Computed Variables (Don't touch or modify!!!)

FILES := $(shell find src tests -name "*.py" -o -name "*.js")
VENVTOUCHFILE := $(VENV)/touchfile
LINTTOUCHFILE := $(VENV)/lint-touchfile
TESTTOUCHFILE := $(VENV)/test-touchfile
HOOKTOUCHFILE := .git/hooks/touchfile

# Primary Targets

.PHONY: all
all:| lint test

.PHONY: lint
lint: $(LINTTOUCHFILE)

$(LINTTOUCHFILE): $(FILES) $(HOOKTOUCHFILE)
	poetry run pre-commit run --all-files
	@touch $@

.PHONY: test
test: $(TESTTOUCHFILE)

$(TESTTOUCHFILE): $(FILES) $(VENVTOUCHFILE)
	poetry run pytest
	@touch $@

.PHONY: clean
clean:
	git clean -dfX

.PHONY: run
run:
	poetry run uvicorn src.os_cfdb.main:app --reload --port 8000

# Secondary Targets

$(HOOKTOUCHFILE): $(VENVTOUCHFILE) .pre-commit-config.yaml
	poetry run pre-commit install --install-hooks -t pre-commit -t commit-msg
	@touch $@

poetry.lock: pyproject.toml
	poetry lock --no-update --no-interaction && touch poetry.lock

$(VENVTOUCHFILE): poetry.lock
	poetry install --no-interaction
	@touch $@
