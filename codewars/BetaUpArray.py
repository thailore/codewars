#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Given an array that represents a number
return array that represents number+1
Ex. [2,3,9] --> [2,4,0]
    [9,9,9] --> [1,0,0,0]
if array is empty, or any number in array is 10+
or negative, return None"""

def up_array(array):
    if not array:
        return None
    for index,val in enumerate(array):
        if val > 9 or val < 0:
            return None

    last_element = len(array) - 1
    if array[last_element] < 9:
        array[last_element] += 1
        return array
    else:
        if set(array) == {9}:
            for index,val in enumerate(array):
                array[index] = 0
            array.insert(0, 1)
            return array
        if array[last_element] >= 9:
            array[last_element] = 0
            array[last_element - 1] += 1
        return array
