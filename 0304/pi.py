#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
问:
pi = 4 - 4/3 + 4/5 - 4/7 + ...
直到最后一项的绝对值小于10的-6为止
'''
import math
flag= 4.0
sumpi = 0
n = 1

if __name__ == "__main__" :
    while math.fabs(flag/(2*n-1)) >= 1e-6 :
        sumpi += flag/(2*n-1)
        n += 1
        flag = -flag
    print sumpi
