#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/10 14:49                
# @Author  : LT                             
# @File    : HJ9.py                     
# @Software: PyCharm

def numreverse(num):
    numMap = {}
    numLists = []
    for i in num[::-1]:
        if i not in numMap.keys():
            numMap[i] = ''
    for k, v in numMap.items():
        numLists.append(k)
    print(''.join(numLists))

numreverse(input())