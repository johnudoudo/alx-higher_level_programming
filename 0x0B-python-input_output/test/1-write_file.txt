#!/usr/bin/python3
"""
This code contain the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """this will returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
    """
    return the text writtenin write_file
    """
