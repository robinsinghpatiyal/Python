# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:43:13 2020

@author: Robin Singh
"""

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
print(counts)