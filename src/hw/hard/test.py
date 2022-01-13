#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def strQualified(pwd):
    for i in pwd:
        pwd = pwd[1:]
        print(pwd)

strQualified(input())