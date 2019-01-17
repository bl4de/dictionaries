#!/usr/bin/python
#
# script for removing duplicates in dictionary

dictionary = open("starter.txt", "r").readlines()
print len(dictionary)
res = set()
for p in dictionary:
    res.add(p.strip().lower())
    
new_dict = list(res)

dictionary = open("starter_filtered.txt", "w+")
for p in new_dict:
    dictionary.write(p + "\n")

