#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/10 13:04                
# @Author  : LT                             
# @File    : HJ15.py                     
# @Software: PyCharm

def hex2dec(temVar):
    print(int(temVar, 16))

while True:
    try:
        hex2dec(input())
    except:
        break