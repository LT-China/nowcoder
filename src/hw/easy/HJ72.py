#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 16:56
# @Author  : LT
# @File    : HJ72.py
# @Software: PyCharm

def way2buyChicken(tempNum):
    for cookNum in range(0, 20):
        # print('1---------')
        for henNum in range(0, 33):
            # print('2--------')
            chickNum = tempNum - cookNum - henNum
            # print('cookNum:%d-henNum:%d-chickNum%d' % (cookNum, henNum, chickNum))
            if cookNum * 5 + henNum * 3 + chickNum * 1/3 == tempNum:
                print('cookNum:%d-henNum:%d-chickNum%d' % (cookNum, henNum, chickNum))


way2buyChicken(int(input()) * 100)