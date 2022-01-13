#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

def newStr(str):
    strlist = list(str)
    strcount = Counter(strlist)
    charaternumsList = []
    charaterremoveList = []

    # 计算所有元素的个数
    for v, n in strcount.items():
        # print(v, n, type(n))
        charaternumsList.append(n)
    mincharnums = min(charaternumsList)
    # 找出需要删除的元素
    for i in strlist:
        # print(i)
        if strlist.count(i) == mincharnums:
            charaterremoveList.append(i)
    # 删除元素
    for i in charaterremoveList:
        strlist.remove(i)

    print(''.join(strlist))

while True:
    try:
        newStr(input())
    except:
        break