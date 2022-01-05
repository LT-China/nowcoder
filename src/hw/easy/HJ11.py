#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def numReverse():
    tmpList = list(input())
    # 方法1：
    # tmpList.reverse()
    # newList = [str(i) for i in tmpList]
    # print(''.join(newList))

    # 方法2：
    print(''.join(tmpList[::-1]))

numReverse()