#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Get count of vowels in string
"""

def getCount(inputStr):
    num_vowels = 0
    vowels = ['a','e','i','o','u'] #set vowels
    for i in inputStr: #each character in string
        for value in vowels:
            if i == value: #if is in vowels 
                num_vowels +=1
    
    return num_vowels
