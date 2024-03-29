#!/usr/bin/python3
"""this code writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """This code writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
