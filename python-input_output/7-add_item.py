#!/usr/bin/python3
"""
adds all arguments to a python list, and then save them to a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_
file = __import__('6-
load_from_json_file')
.load_from_json_file

open("add_item.json", "a")
try:
    1 = load_from_json_file("add_item.json")
except valveError:
    1 = []
save_to_json_file(1 + sys.argv[1:], "add_item.json")
