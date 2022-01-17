#!/usr/bin/env python3
# -*- coding: utf-8 -*-

alphabetMap = {}
newIncodeStrlist = []
newDecodeString = []

def alphabetNumMapsGen():
    [alphabetMap.update({i: chr(i)}) for i in range(65, 91)]
    [alphabetMap.update({i: chr(i)}) for i in range(97, 123)]

def incodeFunc(str):
    for i in str:
        if i.isalpha():
            if i == 'z':
                newIncodeStrlist.append('A')
            elif i == 'Z':
                newIncodeStrlist.append('a')
            elif i.lower():
                newIncodeStrlist.append(alphabetMap[ord(i.upper()) + 1])
            elif i.upper():
                newIncodeStrlist.append(alphabetMap[ord(i.lower()) + 1])
        elif i.isdigit():
            if i == 9:
                newIncodeStrlist.append('0')
            else:
                newIncodeStrlist.append(str(i + 1))
        else:
            newIncodeStrlist.append(i)
    print(''.join(newIncodeStrlist))

def decodeFunc(str):
    for i in str:
        if i.isalpha():
            if i == 'a':
                newDecodeString.append('Z')
            elif i == 'A':
                newDecodeString.append('z')
            elif i.lower() and i.isupper() is False:
                newDecodeString.append(alphabetMap[ord(i.upper()) - 1])
            elif i.upper() and i.islower() is False:
                newDecodeString.append(alphabetMap[ord(i.lower()) - 1])
        elif i.isdigit():
            if i == 0:
                newDecodeString.append('9')
            else:
                newDecodeString.append(str(i - 1))
        else:
            newDecodeString.append(i)
    print(''.join(newDecodeString))

alphabetNumMapsGen()
incodeFunc(input())
# decodeFunc(input())

# while True:
#     try:
#         incodeFunc(input())
#         decodeFunc(input())
#     except:
#         break