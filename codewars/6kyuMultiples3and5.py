#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Number is a passed into function solution. 
Sum of the multiples of 3 and 5 less than the
number is returned
"""

def solution(number):
    sum = 0
    for i in range(number):
        if i%3 == 0 or i%5==0:
            sum += i
    return sum