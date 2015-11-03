#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Identifies the pattern in following numbers and 
returns what the correct value is for number n
 n | score
---+-------
 1 |  50
 2 |  150
 3 |  300
 4 |  500
 5 |  750
"""

def get_score(n):
    sum = 0
    for i in range(n):
        sum += ((i + 1) * 50)
    return sum
    # do your magic here
   