# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
11–1.参数。比较下面 3 个函数：
def countToFour1():
    for eachNum in range(5):
        print eachNum,
def countToFour2(n):
    for eachNum in range(n, 5):
        print eachNum,
def countToFour3(n=1):
    for eachNum in range(n, 5):
        print eachNum,
给定如下的输入直到程序输出，你认为什么会发生？向下表 11.2 填入输出。
如果你认为给定的输入会发生错误的话填入“ERROR"或者如果没有输出的话填入“NONE"
'''

'''
答:
Input        countToFour1        countToFour2        countToFour3
2               ERROR               2 3 4              2 3 4
4               ERROR                 4                  4
5               ERROR                NONE               NONE
(nothing)      1 2 3 4              ERROR             1 2 3 4
'''
