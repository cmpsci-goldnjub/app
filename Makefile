BOOTSTRAP_URL=https://bootstrap.pypa.io/bootstrap-buildout.py

.PHONY: default project clean

default: bin/buildout
	python bin/buildout

bin/buildout: bootstrap.py
	mkdir -p var/
	python bootstrap.py

bootstrap.py:
	curl $(BOOTSTRAP_URL) > bootstrap.py

# Destroys existing test database and creates a new one
db:
	echo "Unimplemented"

clean:
	find ./ -name *.pyc -delete
