#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Given string, returns pig latin version of string"""

def pig_it(text):
    words = text.split(' ')
    new = []
    for word in words:
        if word.isalpha():
            temp = list(word)
            temp.append(temp.pop(0))
            temp.append('ay')
            new.append(''.join(temp))
        else:
            new.append(word)
    return str(' '.join(new))
