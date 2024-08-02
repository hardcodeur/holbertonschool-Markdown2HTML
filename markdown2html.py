#!/usr/bin/python3
import sys
import os
"""
    markdown2html.py
    Write a script markdown2html.py that takes an argument 2 strings
"""
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            'Usage: ./markdown2html.py README.md README.html',
            file=sys.stderr
        )
        sys.exit(1)
    else:
        mdFile = sys.argv[1]
        htmlFile = sys.argv[2]

        if not os.path.exists(mdFile):
            print('Missing <filename>', file=sys.stderr)
            sys.exit(1)
        print("")
        exit(0)
