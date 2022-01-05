#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def wordReverse():
    tmpStr = input()
    # tmpList = [i for i in tmpStr.split()]
    wordList = re.findall(r"[a-zA-Z]*[a-zA-Z]", tmpStr)
    wordList.reverse()
    print(' '.join(wordList))

wordReverse()