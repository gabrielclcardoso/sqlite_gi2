VPATH = .venv/bin/

.venv:
	python3 -m venv .venv

setup: .venv
	$(VPATH)pip install -r requirements.txt

install: .venv
	$(VPATH)pip install $(pkg) && $(VPATH)pip freeze > requirements.txt;

populate: .venv
	$(VPATH)python3 populate.py

.PHONY: install setup
