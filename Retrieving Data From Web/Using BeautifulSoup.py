# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:24:08 2020

@author: Robin Singh
"""


import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

url = input("Enter the url")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of he anchor tags

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    
    
    
    
    



import urllib
from bs4 import BeautifulSoup

url = input("Enter the url")

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tag = soup('span')

count = 0
sums = 0

for i in tag:
	x=int(i.text)
	count = count+1
	sums = sums + x
print (count)
print (sums)