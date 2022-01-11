#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
    try:
        maze = [[]]
        rowcount, liecount = int(input().split())
        for i in range(0, rowcount):
            for j in range(0, liecount):

                maze[i].append(j)
        print(maze)
    except:
        break