#!/usr/bin/env bash
source env/bin/activate
python3 ./src/Interpreter_LLVM.py "$*"
outfile="${*%.ins}.ll"
outfile_bc="${*%.ins}.bc"
if test -f "$outfile"; then
  llvm-as -o out.bc "$outfile"
  llvm-as -o ./lib/runtime.bc ./lib/runtime.ll
  llvm-link -o "$outfile_bc" ./lib/runtime.bc out.bc
  rm out.bc
fi
echo "$outfile"
