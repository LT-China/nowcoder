#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/6 17:42
# @Author  : LT
# @File    : HJ73.py
# @Software: PyCharm

import datetime

def dateCal(temStr):
    tmpDate= datetime.datetime.strptime('-'.join(temStr.split()), '%Y-%m-%d').date()
    print(int(tmpDate.strftime('%j')))

while True:
    try:
        dateCal(input())
    except:
        break