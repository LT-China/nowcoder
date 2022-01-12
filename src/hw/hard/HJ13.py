#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sentenceReverse(str):
    if ' ' in str:
        tmplist = str.split()
        tmplist.reverse()
        print(' '.join(tmplist))
    else:
        print(str)

sentenceReverse(input())