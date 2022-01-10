#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/10 15:25                
# @Author  : LT                             
# @File    : HJ14.py
# @Software: PyCharm

def alphabetSort(count):
    alphabetlists = []
    for i in range(0, count):
        alphabetlists.append(input())
    for i in sorted(alphabetlists):
        print(i)

alphabetSort(int(input()))