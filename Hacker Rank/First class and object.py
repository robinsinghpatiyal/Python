# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:40:44 2020

@author: Robin Singh
"""

class PartyAnimal: #declaring the class
    x=0
    
    def party(self):   #self is just calling the an (the object declared below :)
        self.x = self.x+1
        print("So far the count is ",self.x)
        
an = PartyAnimal() #an is an object

an.party()
an.party()
an.party()
an.party()