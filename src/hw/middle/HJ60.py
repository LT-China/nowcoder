#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def getPrimeFunc(num):
    primeNumLists = []
    primeMap = {}
    for i in filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0], range(2, num + 1)):
        primeNumLists.append(i)
    for i in primeNumLists:
        for j in primeNumLists:
            if i != j and i + j == num:
                if i > j:
                    primeMap[i - j] = str(j) + '-' + str(i)
                else:
                    primeMap[j - i] = str(i) + '-' + str(j)
            elif i == j and i + j == num:
                primeMap[0] = str(i) + '-' + str(j)
    print(''.join(primeMap[min(primeMap.keys())].replace('-', '\n', 1)))

while True:
    try:
        getPrimeFunc(int(input()))
    except:
        break

