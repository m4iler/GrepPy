#!/usr/bin/env python3
"""
USAGE: grep.py PATTERN FILE
Finds string in file (similar to grep)
Can handle RegEx


"""
import sys
try:
    import regex as re
except ModuleNotFoundError:
    import re
    print("You don't have RegEx! Using the RE module.", file=sys.stderr)


def grep(f, term):
    for line in f:
        if re.search(term, line):
            print(line, end="")


def get_args(argv):
    if len(argv) < 2:
        print(__doc__.strip(), file=sys.stderr)

    return argv[0], argv[1:]


def main(argv):
    term, paths = get_args(argv)
    for path in paths:
        try:
            with open(path) as f:
                grep(f, term)
        except FileNotFoundError:
            print("No file found", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
