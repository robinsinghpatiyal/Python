# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:17:55 2020

@author: Robin Singh
"""

class PartyAnimal:
    name = ""
    x = 0
    def __init__(self, z):
        self.name = z
        print(self.name,"constructed")
        
    def party(self):
        self.x = self.x + 1
        print("The count for", self.name, "is", self.x)
        
obj1 = PartyAnimal("Robin")

obj1.party()

obj2 = PartyAnimal("Noddy")

obj2.party()