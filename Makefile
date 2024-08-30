VPATH = .venv/bin/

.venv:
	python3 -m venv .venv

onda_do_trigo.db:
	$(VPATH)python3 populate.py

setup: .venv
	$(VPATH)pip install -r requirements.txt

install: .venv
	$(VPATH)pip install $(pkg) && $(VPATH)pip freeze > requirements.txt;

populate: .venv
	$(VPATH)python3 populate.py

query: onda_do_trigo.db
	$(VPATH)python3 query.py

.PHONY: install setup
