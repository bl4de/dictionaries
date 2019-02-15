#!/usr/bin/python
#
# script for removing duplicates in dictionary

import sys

dictionary = open(sys.argv[1], "r").readlines()
res = set()
for p in dictionary:
    # remove trailing /:
    if p[0] == '/':
        p = p[1:]
    # add uniqe entry to dictionary
    res.add(p.strip().lower())
    
new_dict = list(res)

dictionary = open("_filtered.txt", "w+")
for p in new_dict:
    dictionary.write(p + "\n")

