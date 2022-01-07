#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/7 14:46                
# @Author  : LT                             
# @File    : HJ74-todo.py
# @Software: PyCharm
import shlex

import re

def parameterSplit(strVal):
    tmp = re.split(r"' '|' '\"", strVal)
    # tmpParameter = map()
    # print(tmpParameter)
    print(tmp)

parameterSplit(input())