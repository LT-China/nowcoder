#!/usr/bin/env python3
# -*- coding: utf-8 -*-

alphabetMap = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,'m': 13, 'n': 14,
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
    'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

def beautifulLerverCal(name):
    for namevar in name:
        scoreName = 0
        for i in namevar:
            scoreName += alphabetMap[i]
        print(scoreName)

while True:
    try:
        nameLists = []
        count = int(input())
        for i in range(1, count + 1):
            nameLists.append(input().lower())
        beautifulLerverCal(nameLists)
    except:
        break