#!/usr/bin/python3
"""
    markdown2html.py
    Write a script markdown2html.py that takes an argument 2 strings
"""
import sys
import os
import re

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print('Usage: ./markdown2html.py README.md README.html',file=sys.stderr)
        sys.exit(1)
    else: 
        if not os.path.exists(sys.argv[2]):
            print(f'Missing {sys.argv[2]}', file=sys.stderr)
            sys.exit(1)
        else:
            print("")
            sys.exit(0)
    