#!/usr/bin/python3
"""Module that defines a function to indent text."""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':' characters."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")

            # skip spaces after punctuation
            i += 1
            while i < n and text[i] == " ":
                i += 1
            continue

        i += 1
