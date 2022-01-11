#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def subStrFunc(str, k):
    print(str[:k])

while True:
    try:
        str = input()
        k = int(input())
        subStrFunc(str, k)
    except:
        break