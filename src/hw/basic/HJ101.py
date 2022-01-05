#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sortNum():
    newArry = []
    arryLen = int(input())
    tmpArry = input().split()
    for i in tmpArry:
        newArry.append(int(i))
    tmp = int(input())
    if tmp == 0:
        tmplist = [str(i) for i in sorted(newArry)]
        print(' '.join(tmplist))
    elif tmp == 1:
        tmplist = [str(i) for i in sorted(newArry, reverse=True)]
        print(' '.join(tmplist))
sortNum()