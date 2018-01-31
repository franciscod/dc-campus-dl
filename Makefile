.PHONY: run
run:
	pipenv run python dl.py

.PHONY: clean
clean:
	rm -r materias/
