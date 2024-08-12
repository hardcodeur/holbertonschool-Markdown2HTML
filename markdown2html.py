#!/usr/bin/python3
"""
    markdown2html.py
    Write a script markdown2html.py that takes an argument 2 strings
"""
import sys
import os
import re


def boldOrItalicCheker(str):
    # bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1<\\b>', str)
    # italic
    text = re.sub(r'__(.+?)__', r'<em>\1</em>', str)
    return text


if __name__ == "__main__":
    # error nb arg
    if len(sys.argv) != 3:
        print(
            'Usage: ./markdown2html.py README.md README.html',
            file=sys.stderr
        )
        sys.exit(1)
    mdFileUrl = sys.argv[1]
    htmlFileUrl = sys.argv[2]
    if not os.path.exists(mdFileUrl):
        print(f'Missing {mdFileUrl}', file=sys.stderr)
        sys.exit(1)
    mdFile = open(mdFileUrl)
    mdContend = mdFile.read()
    mdElements = mdContend.split('\n')
    htmlElements = []
    # Trigger
    inList = False
    isUl = False
    isOl = False
    isP = False
    for mdElement in mdElements:
        # Title checker
        titleMatchPattern = re.match(r'^(\#+)\s(.*)$', mdElement)
        if titleMatchPattern:
            titleLv = len(titleMatchPattern.group(1))
            titleText = boldOrItalicCheker(titleMatchPattern.group(2))
            if titleLv <= 6:
                titleHmtl = f"<h{titleLv}>{titleText}</h{titleLv}>"
                htmlElements.append(titleHmtl)
        # List checker
        listMatchPattern = re.match(r'^([-*])\s(.*)$', mdElement)
        if listMatchPattern:
            listType = listMatchPattern.group(1)
            liText = boldOrItalicCheker(listMatchPattern.group(2))
            liHtml = f"<li>{liText}</li>"
            if not inList:
                inList = True
                if listType == "-":
                    isUl = True
                    startBaliseHtml = "<ul>"
                elif listType == "*":
                    isOl = True
                    startBaliseHtml = "<ol>"
                htmlElements.extend([startBaliseHtml,liHtml])
            else:
                htmlElements.append(liHtml)
        # paragraphe checker
        paragrapheMatchPattern = re.match(r'^(?!\s*#)(?!\s*[-*])(.*?)(?=\n\s*\n|$)', mdElement)
        if paragrapheMatchPattern:
            paragraphe = boldOrItalicCheker(paragrapheMatchPattern.group(1))
            print(paragraphe)
            if not inList:
                inList = True
                isP = True
                startBaliseHtml = "<p>"
                htmlElements.extend([startBaliseHtml,paragraphe])
            elif isP:
                if paragraphe == "\n" or paragraphe == "":
                    inList = False
                    isP= False
                    endBaliseHtml = "</p>"
                    htmlElements.append(endBaliseHtml)
                htmlElements.append(paragraphe)
    if inList:
        inList = False
        if isUl:
            isUl = False
            endBaliseHtml = "</ul>"
        elif isOl:
            isOl = False
            endBaliseHtml = "</ol>"
        elif isP:
            isP= False
            endBaliseHtml = "</p>"
        htmlElements.append(endBaliseHtml)
    # Write html file
    if len(htmlElements) > 0:
        htmlContend = '\n'.join(htmlElements)
        htmlFile = open(htmlFileUrl, "w")
        htmlFile.write(htmlContend)
        htmlFile.close()
    exit(0)