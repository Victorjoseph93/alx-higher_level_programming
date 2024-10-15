#!/usr/bin/python3
"""Task 7 of ALX Project(Python - Input/Output)

This module uses its arguments to modify a JSON file.

"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    theList = load_from_json_file("add_item.json")
except FileNotFoundError:
    theList = []

for string in sys.argv[1:]:
    theList.append(string)

save_to_json_file(theList, "add_item.json")
