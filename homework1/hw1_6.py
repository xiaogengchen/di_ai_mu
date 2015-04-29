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
        NUM = raw_input("请输入一个数字：")
        if not NUM.isdigit() :
            continue
        NUM = int(NUM)
        break
    for num in range(1,NUM+1):
        temp_NUM = num
        while temp_NUM > 1 :
            print temp_NUM,
            temp_NUM -= 1
        for i in range(1,num+1):
            print i,
        print
