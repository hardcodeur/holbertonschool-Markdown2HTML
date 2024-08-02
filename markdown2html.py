#!/usr/bin/python3
"""
    markdown2html.py
    Write a script markdown2html.py that takes an argument 2 strings
"""
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            'Usage: ./markdown2html.py README.md README.html',
            file=sys.stderr
        )
        sys.exit(1)
    mdFile = sys.argv[1]
    htmlFile = sys.argv[2]
    if not os.path.exists(mdFile):
        print(f'Missing {mdFile}', file=sys.stderr)
        sys.exit(1)
    print("")
    exit(0)
