#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/6 17:42
# @Author  : LT
# @File    : HJ73.py
# @Software: PyCharm

from datetime import datetime
import time

def dateCal(temStr):
    # print(temStr)
    dayValue = datetime.strptime(temStr, '%Y-%m-%d')
    print(dayValue)

    return

while True:
    try:
        dateCal(input())
    except:
        break