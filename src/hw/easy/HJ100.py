#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/10 11:30                
# @Author  : LT                             
# @File    : HJ100.py                     
# @Software: PyCharm

def sums(num):
    print(int((3 * num + 1) * num / 2))

while True:
    try:
        sums(int(input()))
    except:
        break