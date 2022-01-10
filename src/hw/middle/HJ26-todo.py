#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/10 16:32                
# @Author  : LT                             
# @File    : HJ26-todo.py
# @Software: PyCharm

def strSorted(tmpstr):
    tempStrLists = []
    for i in tmpstr:
        if i.isalpha():
            # TODO
            return
        else:
            # TODO
            return
    newStr = sorted(tmpstr, key=lambda c: (c.lower(), c.islower()))
    print(newStr)

strSorted(input())