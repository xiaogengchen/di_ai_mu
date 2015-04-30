#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
6、用键盘输入15以内的整数，输出这样的格式。
        1
        2 1 2
        3 2 1 2 3
        4 3 2 1 2 3 4
        5 4 3 2 1 2 3 4 5
        6 5 4 3 2 1 2 3 4 5 6
        7 6 5 4 3 2 1 2 3 4 5 6 7
'''

if __name__ == "__main__" :
    while True :
        rows = raw_input("请输入一个数字：")
        if not rows.isdigit() :
            continue
        rows = int(rows)
        break
    row = 1
    while row <= rows :
        col = row
        while col >= 1 :
            print col,
            col -= 1
        col += 2
        while col <= row :
            print col,
            col += 1
        row += 1
        print
            
