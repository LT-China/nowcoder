#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def pick7Cal(num):
    count = 0
    for i in range(1, num +1):
        # sevenlists.append(str(i))
        if re.search('7', str(i)):
            count += 1
        elif i > 7 and i % 7 == 0:
            count += 1
    print(count)

while True:
    try:
        pick7Cal(int(input()))
    except:
        break