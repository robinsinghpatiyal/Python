# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:52:56 2020

@author: Robin Singh
"""

import json

data = '''
{
 "name" : "Robin",
 "phone": {
         "type" : 'intl",
         "number" : "9876543210"
         },
 "email" : {
         "hide" : "yes"
         }
}'''
 
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])