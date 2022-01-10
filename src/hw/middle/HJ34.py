#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def picSort(tmpvar):
    print(''.join(sorted(tmpvar)))

while True:
    try:
        picSort(input())
    except:
        break