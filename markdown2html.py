#!/usr/bin/python3
"""
    markdown2html.py
    Write a script markdown2html.py that takes an argument 2 strings
"""
import sys
import os
import re

if __name__ == "__main__":
    
    mdFileUrl=sys.argv[1]
    htmlFileUrl=sys.argv[2]

    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            print('Usage: ./markdown2html.py README.md README.html',file=sys.stderr)
        elif os.path.exists(mdFileUrl):
            print(f'Missing {mdFileUrl}', file=sys.stderr)
        sys.exit(1)
    else:
        exit(0)