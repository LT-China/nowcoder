#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def intfunc(t):
    intT = int(t)
    t1 = t - intT
    if (t1 < 0.5):
        print(intT)
    elif (t1 >= 0.5) & (t1 < 1):
        print(intT + 1)

intfunc(float(input()))