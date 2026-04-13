#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.
    """
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (length, first_char)
