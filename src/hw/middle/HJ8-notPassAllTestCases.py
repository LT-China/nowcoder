#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/10 14:14                
# @Author  : LT                             
# @File    : HJ8-notPassAllTestCases.py
# @Software: PyCharm

# 测试用例没有全部通过
def tableRecMerge():
    mapTab = {}
    count = int(input())
    for i in range(0, count):
        x, y = input().split()
        if x in mapTab.keys():
            mapTab[x] = int(mapTab[x]) + int(y)
        else:
            mapTab[x] = y
    for key, value in mapTab.items():
        print(str(key)+' '+str(value))

tableRecMerge()