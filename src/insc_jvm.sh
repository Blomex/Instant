#!/usr/bin/env bash

if source env/bin/activate; \
	python3 ./src/Interpreter.py "$@"; \
then
  # shellcheck disable=SC2145
  java -jar ./lib/jasmin.jar -d $(dirname -- "$@") "${@%.ins}.j"
fi

