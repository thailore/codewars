#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Narcissistic number is a num which the sum of its
own digits, each raised to the power of the num 
of digits
"""

def narcissistic( value ): 
    val = str(value) #turn number into string
    power = len(val) #set power to length
    sum = 0
    for c in val: #each character in string
        sum += (int(c) ** power) #take each digit and raise to power, add to sum
    if sum == value: #if equals to original value, True
        return True
    else:
        return False
        
