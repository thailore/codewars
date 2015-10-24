#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Spin Words. 
"""

def spin_words(sentence):
    mylist = sentence.split(' ') #split sentence by spaces into a list
    for i in range(len(mylist)): #length of list
        if len(mylist[i]) > 4: #if word is longer than 5 letters
            mylist[i] = mylist[i][::-1] #reverse word
    mylist = ' '.join(mylist) #join list with spaces
    return mylist
