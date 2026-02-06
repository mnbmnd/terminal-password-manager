#!/usr/bin/env fish

set SCRIPT_DIR (dirname (status -f))

python3 $SCRIPT_DIR/main.py $argv
