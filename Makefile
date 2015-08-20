BOOTSTRAP_URL=https://bootstrap.pypa.io/bootstrap-buildout.py

.PHONY: default project clean very-clean

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

very-clean: clean
	@# This may vary depending where buildout sticks stuff.
	rm -f bootstrap.py
	rm -rf bin/
	rm -rf var/
