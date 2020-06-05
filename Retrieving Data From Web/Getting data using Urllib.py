# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:32:58 2020

@author: Robin Singh
"""

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())