#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def charaterCal(str, tmpChar):
    count = str.lower().count(tmpChar.lower())
    print(count)

charaterCal(input(), input())