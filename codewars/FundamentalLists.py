#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Takes list of strings. If string is exactly 4 characters
long, adds to friends list. returns friends
"""

def friend(x):
    friends=[]
    for item in x:
        if len(item) == 4:
            friends.append(item)
    return friends
            
   