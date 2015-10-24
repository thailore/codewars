#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
takes the strength of an earthquake 
in form of 2D array representing shockwaves
and age of a building and determines
if the building is safe
"""

def strong_enough( earthquake, age ):
    sum = 0
    k = 1
    strength = 1000 #initial strength of building
    for i in range(age): #calculates decay of strength
        strength = strength - (strength*0.01)
    for i in range(len(earthquake)): #length of array 
        for j in range(len(earthquake[i])): #access each element in 2D
            sum = sum + earthquake[i][j] #add value
        k = k * sum #multiply by value
        sum = 0 
    
    if k < strength:
        return "Safe!"
    else:
        return "Needs Reinforcement!"
