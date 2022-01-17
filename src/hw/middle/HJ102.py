#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

def strcountsort(str):
    countres = Counter(str)
    # -x[1] 先遍历按照value的大小从大到小排序，然后x[0]再按照key 的大小排序
    '''
        def strcountsort():
        tmp = [('a', 6), ('c', 2), ('b', 2), ('d', 1), ('e', 4)]
        a = sorted(tmp, key=lambda x: x[0])
        b = sorted(tmp, key=lambda x: -x[1])
        c = sorted(tmp, key=lambda x: x[1])
        print(a)
        print(b)
        print(c)
        strcountsort()
    '''
    newstrsort = sorted(countres.items(), key=lambda x: (-x[1], x[0]))
    print(''.join([item[0] for item in newstrsort]))

while True:
    try:
        strcountsort(input())
    except:
        break

