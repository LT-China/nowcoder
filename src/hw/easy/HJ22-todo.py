#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bottlecal(emptybottlenum):
    # 空瓶数
    # emptybottlenum = 0
    # 汽水瓶
    #sodabottlenumsum = 0
    # 置换的空瓶
    switchemptybottle = emptybottlenum
    if switchemptybottle >= 2:
        # 第一次置换
        sodabottlenum = emptybottlenum // 3
        switchemptybottle = sodabottlenum + emptybottlenum % 3
        sodabottlenumsum = sodabottlenum
        # 第一次置换后
        while switchemptybottle > 2:
            sodabottlenum = switchemptybottle // 3
            switchemptybottle = sodabottlenum + switchemptybottle % 3 + 1
            sodabottlenumsum = sodabottlenumsum + sodabottlenum
        print(sodabottlenumsum)
    else:
        print(0)

bottlecal(int(input()))
# while True:
#     try:
#         bottlecal(int(input()))
#     except:
#         break