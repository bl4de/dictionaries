#!/usr/bin/python
#
# script for removing duplicates in dictionary
import sys
dictionary = open(sys.argv[1], "r").readlines()
print len(dictionary)
res = set()
for p in dictionary:
    res.add(p.strip().lower())
    
new_dict = list(res)

dictionary = open("_filtered.txt", "w+")
for p in new_dict:
    dictionary.write(p + "\n")

