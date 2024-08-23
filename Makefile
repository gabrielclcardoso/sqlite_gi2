VPATH = .venv/bin/

.venv:
	python3 -m venv .venv

setup: .venv
	$(VPATH)pip install -r requirements.txt

install: .venv
	$(VPATH)pip install $(pkg) && $(VPATH)pip freeze > requirements.txt;

.PHONY: install setup
