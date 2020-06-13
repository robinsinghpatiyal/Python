# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:58:42 2020

@author: Robin Singh
"""

class PartyAnimal:
    x = 0
    
    def __init__(self):
        print("I am constructed")
        
    def party(self):
        self.x = self.x + 1
        print("Current value of x is ", self.x)
    
    def __del__(self):
        print("I am destructed", self.x)
        
        
#making object
        
ob = PartyAnimal()
ob.