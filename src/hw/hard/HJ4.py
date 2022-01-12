#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def strsplit(str):
    count = 0
    if len(str) < 8:
        print(''.join((str, '0' * (8 - len(str)))))
    elif len(str) % 8 == 0:
        while count < len(str):
            print(str[count: count + 8])
            count += 8
    else:
        while count < len(str):
            if len(str) - count > 8:
                print(str[count: count + 8])
                count += 8
            else:
                print(''.join((str[count:], '0' * (8 - (len(str) - count)))))
                break
while True:
    try:
        strsplit(input())
    except:
        break