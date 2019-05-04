#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
FULLPATH="$DIR/AsciiPrintCommand.py"
present=$(grep "$FULLPATH" $HOME/.gdbinit 2> /dev/null)
if [[ -z "$present" ]]; then
    echo "source $FULLPATH"  >> ~/.gdbinit
fi
