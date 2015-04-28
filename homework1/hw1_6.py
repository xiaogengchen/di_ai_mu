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
    for num in range(1,8):
        for i in range(1,num):
            pass