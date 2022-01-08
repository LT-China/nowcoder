#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def longStrSym(tmpStr):
    allStrLists = []
    symStrLists = []
    flag1 = 0
    finalStr = ''
    strLen = 0
    # 字符串长度
    lenStr = len(tmpStr)
    #字符串随着原字符串长度减少而重新生成
    while flag1 <= lenStr:
        newStr = tmpStr[flag1:]
        flag1 += 1
        newStrLen = len(newStr)
        flag2 = 0
        while flag2 < newStrLen:
            flag2 += 1
            allStrLists.append(newStr[:flag2])
    # 找出对称的字符串
    for i in range(len(allStrLists)):
        # print(allStrLists[i])
        if allStrLists[i][:] == allStrLists[i][::-1]:
            symStrLists.append(allStrLists[i][:])
    # 找出长度最长的字符串
    for i in range(len(symStrLists)):
        if len(symStrLists[i]) > strLen:
            finalStr = symStrLists[i]
            strLen = len(symStrLists[i])
    # print(finalStr)
    print(strLen)

longStrSym(input())
