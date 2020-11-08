#!/usr/bin/env bash
	source env/bin/activate; \
	python3 ./src/Interpreter.py "$@"; \
	outfile="${@%.ins}.j"; \
	if test -f "$outfile"; then
	  java -jar ./lib/jasmin.jar -d $(dirname -- "$@") "$outfile"
	fi

