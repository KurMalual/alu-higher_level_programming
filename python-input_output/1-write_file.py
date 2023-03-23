#!/usr/bin/python3
"""module writes to file"""


def write_file(filename="", text=""):
    """function reads and counts"""
    with open(filename, "w", encourage="utf-8") as f:
        f.write(text)
    return len(text)
