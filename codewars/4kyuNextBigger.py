#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Get next bigger number with same digits"""

def next_bigger(number):
    num = list(str(number))
    test_num = tuple(num)
    test_num = list(test_num)
    print(num)
    print(test_num)
    greater = []
    for index, val in enumerate(num):
        print(index, val)
        if index+1 == len(num):
            test_num[index], test_num[0] = test_num[0], test_num[index]
        else:
            test_num[index], test_num[index+1] = test_num[index+1], test_num[index]
        
        test_num = int(''.join(test_num))
        if test_num > number:
            greater.append(test_num)
        test_num = tuple(num)
        test_num = list(test_num)
    greater = sorted(greater)
    print(greater)
    return greater[0]
