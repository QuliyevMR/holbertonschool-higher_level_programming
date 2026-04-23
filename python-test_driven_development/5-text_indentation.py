#!/usr/bin/python3
"""Module that defines text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    line = ""

    for char in text:
        if char in separators:
            print(line.strip())
            print()
            line = ""
        else:
            line += char

    if line:
        print(line.strip())
