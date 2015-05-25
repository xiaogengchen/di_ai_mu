# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
闭包:
    内部函数引用外部函数中的变量，内部函数就认为是闭包
'''


def outer(x):
    z = 2
    def inner(y):
        return x + y + 2
    return inner

p = outer(5)
print p(6)