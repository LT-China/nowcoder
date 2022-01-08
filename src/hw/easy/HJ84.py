#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def capitalLetterCal(tmpStr):
    print(len(re.findall('[A-Z]', tmpStr)))

while True:
    try:
        capitalLetterCal(input())
    except:
        break