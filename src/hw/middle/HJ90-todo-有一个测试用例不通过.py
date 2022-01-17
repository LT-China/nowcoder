#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def iplegal(str):
    iplist = str.split('.')
    count = 0
    for i in iplist:
        if int(i) >= 0 and int(i) <= 255:
            count += 1
        else:
            count += 0
    if count == 4:
        print('YES')
    else:
        print('NO')
while True:
    try:
        iplegal(input())
    except:
        break