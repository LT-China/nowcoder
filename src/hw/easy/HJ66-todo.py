#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 16:26
# @Author  : LT
# @File    : HJ66-todo.py
# @Software: PyCharm

import re

cmdMap = {'reset': 'reset what',
          'reset board': 'board fault',
          'board add': 'where to add',
          'board delete': 'no board at all',
          'reboot backplane': 'impossible',
          'backplane abort': 'install first',
          'he he': 'unknown command'}

def cmdMatch():
    cmdStr = input()

    return

while True:
    try:
        cmdMatch()
    except:
        break