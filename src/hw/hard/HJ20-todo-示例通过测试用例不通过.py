#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import Counter

def substrCal(pwd):
    substrlists = []
    count = 0
    # 重复子字符串统计
    substr = []
    # substring generate
    for i in pwd:
        for j in range(1, len(pwd)):
            # print(newPwd[:j])
            j += 1
            substrlists.append(pwd[:j])
        count += 1
        pwd = pwd[1:]

    # 统计substrlists 重复的元素 次数
    for k, v in Counter(substrlists).items():
        strLen = len(k)
        if v > 1 and strLen > 2:
            substr.append(k)
    return substr

def strQualified(pwd, substr):
    # 匹配非字母数字的字符
    charaterLists = re.findall('\W', pwd)
    # print(pwd, substr)
    # print(charaterLists, len(charaterLists))

    if len(pwd) > 8 and len(substr) == 0:
        # print('1------------')
        if pwd.isalnum() and pwd.islower():
            print('NG')
        elif pwd.isalnum() and pwd.isupper():
            print('NG')
        elif pwd.isalnum() or pwd.islower() or pwd.isupper():
            print('1--------')
            print('OK')
        elif len(charaterLists) != 0 and pwd.isalnum() or pwd.islower() or pwd.isupper():
            print('2--------')
            print('OK')
        elif len(charaterLists) != 0 and pwd.islower() and pwd.isupper():
            print('3--------')
            print('OK')
    else:
        # print(len(substr))
        print('NG')


# pwd = input()
# # 去除空格换行
# newpwd = re.sub(r'\s+', '', pwd)
# substr = substrCal(newpwd)
# strQualified(newpwd, substr)

while True:
    try:
        pwd = input()
        # 去除空格换行
        newpwd = re.sub(r'\s+', '', pwd)
        substr = substrCal(newpwd)
        strQualified(newpwd, substr)
    except:
        break

