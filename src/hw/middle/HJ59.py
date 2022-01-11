#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def characterCal(tmpstr):
    characterLists = []
    for i in tmpstr:
        if tmpstr.count(i) == 1:
            characterLists.append(i)
    if len(characterLists) == 0:
        print('-1')
    else:
        print(characterLists[0])
while True:
    try:
        characterCal(input())
    except:
        break
