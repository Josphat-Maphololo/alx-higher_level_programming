#!/usr/bin/python3

"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

0x0B-python-input_output/1-write_file.py

#!/usr/bin/python3
