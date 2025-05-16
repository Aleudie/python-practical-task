#!/usr/bin/env python3

import sys
import argparse

"""
Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised.
"""

parser = argparse.ArgumentParser(description='Accepts a file name and outputs its extension')
parser.add_argument('filename', help='Any file name, including extension')
args = parser.parse_args()

filename_splited = args.filename.split('.')
extension = filename_splited[-1]

if len(filename_splited) < 2 or extension == '':
    raise ValueError("No extension found in the provided filename")

print(f"The file extension is: {extension}")