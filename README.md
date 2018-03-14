## Ascii Print Command

This gdb extension allows mixed ascii-hex printing of strings, as described in [this Stackoverflow question](https://stackoverflow.com/q/16031100/391161).

Suppose one had the following buffer in a C program.

    char* buf = "Hello World \x1c"

One can source the file `AsciiPrintCommand.py` in their `$HOME/.gdb_init` file, and then invoke the following command.

    ascii-print buf
    "Hello World \x1c"
