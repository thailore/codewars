#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Check to see if first half of number entered
as string is equal to second half
Ex:
003111 --> 0+0+3 = 1+1+1
02011 --> 0+2 = 1+1 """

def luck_check(string):
    if len(string) % 2 == 0:
        mid = len(string) // 2
        first_half = list(string[:mid])
        second_half = list(string[mid:])
        for index, val in enumerate(first_half):
            first_half[index] = int(first_half[index])
        for index, val in enumerate(second_half):
            second_half[index] = int(second_half[index])
        if sum(first_half) == sum(second_half):
            return True
        else:
            return False
        
    else:
        mid = len(string) // 2
        first_half = list(string[:mid])
        second_half = list(string[mid+1:])
        for index, val in enumerate(first_half):
            first_half[index] = int(first_half[index])
        print(first_half)
        for index, val in enumerate(second_half):
            second_half[index] = int(second_half[index])
        print(second_half)
        if sum(first_half) == sum(second_half):
            return True
        else:
            return False
