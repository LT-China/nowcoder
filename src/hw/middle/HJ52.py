#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Levenshtein

while True:
    try:
        print(Levenshtein.distance(input(), input()))
    except:
        break