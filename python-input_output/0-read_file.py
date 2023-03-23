#!/usr/bin/python3
"""module for opening file"""


def read_file(filename="""):
    """function- opens and read passed by name"""
    with open(filename, encording="utf-8") as f:
       out_data = f.read()
       print("{}".format(out_data), end="")
