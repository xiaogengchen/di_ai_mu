# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
传递函数。给在这章中描述的 testit()函数写一个姊妹函数。timeit()会带一个函数
对象（和参数一起）以及计算出用了多少时间来执行这个函数，而不是测试执行时的错误。返回下
面的状态：函数返回值，消耗的时间。你可以用 time.clock()或者 time.time()，无论哪一个给你
提供了较高的精度。 （一般的共识是在 POSIX 上用 time.time()， 在 win32 系统上用 time.clock()）
注意：timeit()函数与 timeit 模块不相关(在 python2.3 中引入）
'''

import time


def myFunction(*args):
    return [i for i in args]


def timeit(func, *args):
    start = time.clock()
    myList = func(*args)
    end = time.clock()
    return myList, end - start



def main():
    args = tuple([i for i in range(100)])
    for i in timeit(myFunction, *args):
        print i


if __name__ == "__main__":
    main()
