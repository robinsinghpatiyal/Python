# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 23:53:24 2020

@author: Robin Singh
"""

import json
import urllib

count = 0
sum = 0
url = input("Enter Url - ")

data = urllib.request.urlopen(url).read()

print (data)

info = json.loads(data.decode("utf-8"))

for i in info['comments']:
    count = count+1
    sum = sum + i['count']
print ("Sum : ",sum  ) 
print ("count : ",count)