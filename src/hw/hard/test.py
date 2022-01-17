#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def strcountsort():
    tmp = [('a', 6), ('c', 2), ('b', 2), ('d', 1), ('e', 4)]
    a = sorted(tmp, key=lambda x: x[0])
    b = sorted(tmp, key=lambda x: -x[1])
    c = sorted(tmp, key=lambda x: x[1])
    print(a)
    print(b)
    print(c)
strcountsort()