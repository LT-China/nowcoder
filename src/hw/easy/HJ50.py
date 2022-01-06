#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def arithmetifunc():
    print(int(eval(input().replace('{', '(').replace('[', '(').replace('}', ')').replace(']', ')'))))

arithmetifunc()