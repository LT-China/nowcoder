#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/10 15:16                
# @Author  : LT                             
# @File    : HJ10.py                     
# @Software: PyCharm

def strCal(tmpstr):
    strset = set()
    for i in tmpstr:
        strset.add(i)
    print(len(strset))

strCal(input())
