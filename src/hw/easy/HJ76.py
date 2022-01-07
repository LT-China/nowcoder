#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/7 17:42                
# @Author  : LT                             
# @File    : HJ76.py                     
# @Software: PyCharm

import math

numLists = []
newNumLists = []
def nicochsTheorem(valNum):
    num = int(math.pow(valNum, 3))
    for i in range(1, num + 1):
        # print(++i)
        numLists.append(i)
    for i in numLists:
        if i % 2 != 0:
            newNumLists.append(i)
    for i in newNumLists:
        if i * valNum + 2 * (valNum - 1) == num:
            print(i)


nicochsTheorem(int(input()))