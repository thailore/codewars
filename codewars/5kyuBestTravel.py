#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Given a list of distances ls, number of distances to visit k,
and maximum desired combined distance t, return best sum
of distances fitting the request

"""

import itertools
def choose_best_sum(t, k, ls):
    temp = 0
    for i in set(itertools.combinations(ls,k)):
        if sum(i) <= t and sum(i) > temp:
            temp = sum(i)
    if temp == 0:
        return None
    else:
        return temp
