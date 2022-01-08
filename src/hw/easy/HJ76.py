#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/7 17:42
# @Author  : LT
# @File    : HJ76.py
# @Software: PyCharm

import math

def nicochsTheorem(valNum):
    numLists = []
    newNumLists = []
    tmpLists = []
    num = int(math.pow(valNum, 3))
    tmpSum = 0
    for i in range(1, num + 1):
        # print(++i)
        numLists.append(i)
    # 找出所有质数
    for i in numLists:
        if i % 2 != 0:
            newNumLists.append(i)
    # 等差数列求和
    for tmp in range(1, valNum):
        tmpSum += tmp
        ++tmp
    for i in newNumLists:
        if valNum * i + 2 * tmpSum == num:
            tmpLists.append(str(i))
            tmpnum = i
            for tmp in range(1, valNum):
                tmpnum = tmpnum+ 2
                tmpLists.append(str(tmpnum))
    print('+'.join(tmpLists))
while True:
    try:
        nicochsTheorem(int(input()))
    except:
        break