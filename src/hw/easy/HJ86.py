#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def maxBitNum(num):
    numBin = bin(num).replace('0b', '').split('0')
    newNumBin = list(filter(None, numBin))

    print(len(max(newNumBin)))
while True:
    try:
        maxBitNum(int(input()))
    except:
        break