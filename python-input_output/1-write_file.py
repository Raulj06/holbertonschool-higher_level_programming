#!/usr/bin/python3
"""writes to a text file"""


def write_file(filename="", text=""):
    """writes to a text file"""

    with open(filename, 'w') as a_file:
        return a_file.write(text)
