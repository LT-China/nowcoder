#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 16:17
# @Author  : LT
# @File    : HJ62.py
# @Software: PyCharm

def count1Num(tmp):
    print(str(bin(tmp)).count('1'))

while True:
    try:
        count1Num(int(input()))
    except:
        break