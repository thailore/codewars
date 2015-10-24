#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Receive credit card number 
return ####-####-####-1234
cooresponding to cc num
"""

# return masked string
def maskify(cc):
    length = len(cc) #get length of number
    new = "" #new string
    for i in range(length-4):
        new +="#" #set first 12 numbers to be a hashtag
    new += cc[-4::] #add last 4 digits of nummber to string
    return new
