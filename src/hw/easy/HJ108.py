#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2022/1/10 12:49                
# @Author  : LT                             
# @File    : HJ108.py                     
# @Software: PyCharm

import math
def leastCommonMultiple():
    num1, num2 = map(int, input().split())
    lcm = num1 * num2 / math.gcd(num1, num2)
    print(int(lcm))

leastCommonMultiple()