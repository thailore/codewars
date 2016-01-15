#! usr/bin/env python
# -*- coding: utf-8 -*-

def group_in_10s(*argv):
    if not argv:
        return []
    nums = []
    for num in argv:
        nums.append(num)
    nums.sort()
    y = len(nums) - 1
    max = nums[y] // 10
    grouped = []
    for _ in range(max+1):
        grouped.append([])
    for num in argv:
        x = num // 10
        grouped[x].append(num)
    print(grouped)
    for index, val in enumerate(grouped):
        grouped[index].sort()
        if not grouped[index]:
            grouped[index] = None
    return grouped
