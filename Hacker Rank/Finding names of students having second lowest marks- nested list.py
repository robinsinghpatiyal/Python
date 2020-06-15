# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 00:05:32 2020

@author: Robin Singh
"""

dic = {}
for _ in range (int(input())):
    Name = input()
    Grade = float(input())
    dic[Name] = Grade

v = dic.values()

second = sorted(list(set(v)))[1]
# Remoing duplicte grades by using set data type , changing it to list, sorting in ascending order and taking the second lowest grade.

sec_low = []

for key,value in dic.items():
    if value == second:
        sec_low.append(key)
sec_low.sort()

for i in sec_low:
    print (i)