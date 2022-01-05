#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#TODO
def sumRabbit():
    adultRabbit = 1
    growingRabbit = 0
    babyRabbit = 0
    tmpMonth = int(input())
    for tmpvar in range(1, tmpMonth):
        babyRabbit = babyRabbit + growingRabbit
        growingRabbit = adultRabbit
        adultRabbit = babyRabbit
        totalNums = adultRabbit + growingRabbit + babyRabbit
    print(totalNums)

sumRabbit()