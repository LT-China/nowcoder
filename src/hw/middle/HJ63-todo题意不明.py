#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def getGCRatioStr(str):
    gcLists = []
    newgcLists = []
    dnasublists = []
    dnaLists = []
    gcMap = {}
    for i in range(0, len(str) + 1):
        newgcstr= str[i:]
        for j in range(1, len(newgcstr) + 1):
            # gcLists.append(newgcstr[:j])
            gcLists.append(newgcstr[:j])
    # func = lambda x, y: x if y in x else x + [y]
    newgcLists = reduce(lambda x, y: x if y in x else x + [y], [[], ] + gcLists)


getGCRatioStr(input())

# while True:
#     try:
#         getGCRatioStr(input())
#     except:
#         break
