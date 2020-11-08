SHELL := /bin/bash
all:
    python3 -m venv env
    source env/bin/activate
    pip install antlr4-python3-runtime
    cp src/insc_jvm.sh insc_jvm
    chmod u+x insc_jvm
    cp src/insc_llvm.sh insc_llvm
    chmod u+x insc_llvm
 