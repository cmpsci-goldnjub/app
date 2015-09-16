BOOTSTRAP_URL=https://bootstrap.pypa.io/bootstrap-buildout.py

.PHONY: default project clean

default: bin/buildout
	python bin/buildout

bin/buildout: bin/bootstrap.py
	mkdir -p var/
	python bin/bootstrap.py

bin/bootstrap.py:
	mkdir -p bin/
	curl $(BOOTSTRAP_URL) > bin/bootstrap.py

# Destroys existing test database and creates a new one
db:
	rm -f var/db/*.db
	python bin/django makemigrations
	python bin/django migrate --no-initial-data
	python bin/django migrate
	python bin/django loaddata project/fixtures/initial_data.yaml

clean:
	find ./ -name *.pyc -delete
