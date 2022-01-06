#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def perfectNum(num):
    sumCal = 0
    sumList = []
    for i in range(1, num):
        if num % i == 0:
            sumList.append(i)
    sumCal = sum(sumList)
    if sumCal == num:
        return True
    else:
        return False


def perfectNumCal():
    totalPerfectNum = []
    tmpNum = int(input())
    for i in range(1, tmpNum):
        if perfectNum(i):
            totalPerfectNum.append(i)
    print(len(totalPerfectNum))


while True:
    try:
        perfectNumCal()
    except:
        break