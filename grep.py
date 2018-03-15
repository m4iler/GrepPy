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
    if "-v" in sys.argv[1:]:
        print("You don't have RegEx! Using the RE module.", file=sys.stderr)

def get_args(argv):
    try:
        term, path = argv
        return term, path
    except ValueError:
        print(__doc__.strip(), file=sys.stderr)

def main(argv):
    term, path = get_args(argv)
    try:
        with open(path) as f:
            for line in f:
                if re.search(term, line):
                    print(line, end="")
    except FileNotFoundError:
        print("No file found", file = sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
