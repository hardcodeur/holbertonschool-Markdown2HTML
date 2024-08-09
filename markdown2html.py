#!/usr/bin/python3
"""
    markdown2html.py
    Write a script markdown2html.py that takes an argument 2 strings
"""
import sys
import os
import re

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html',file=sys.stderr)
        sys.exit(1)
    elif not os.path.exists(sys.argv[2]):
        print(f'Missing {sys.argv[2]}', file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)
    