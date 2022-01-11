#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def characterCal(temstr):
    alphabetLists = []
    spaceLists = []
    numLists = []
    othercharLists = []
    for i in temstr:
        if i.isalpha():
            alphabetLists.append(i)
        elif i.isspace():
            spaceLists.append(i)
        elif i.isdigit():
            numLists.append(i)
        else:
            othercharLists.append(i)
    print(len(alphabetLists))
    print(len(spaceLists))
    print(len(numLists))
    print(len(othercharLists))

while True:
    try:
        characterCal(input())
    except:
        break