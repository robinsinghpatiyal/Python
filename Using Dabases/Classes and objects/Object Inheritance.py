# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:29:17 2020

@author: Robin Singh
"""

class PartyAnimal:
    x = 0
    
    def __init__ (self):
        print("the constructor is initialized")
        
    def party(self):
        self.x = self.x + 1
        print("Count is ", self.x)
        
class NewPartAnimal(PartyAnimal):
    pts = 0
    
    def __init__ (self):
        print("another constructor is initialized")
        
    def secondParty(self):
        self.party()
        self.pts = self.pts +7
        print("the count is ",self.x," And the points are ", self.pts)
        
        
obj = NewPartAnimal()
obj.secondParty()