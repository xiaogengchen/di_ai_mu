# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
修改习题25 的代码:
使用 random 模块中的 randint()或 randrange()方法生成一个随机数集合:从 0 到 9(包括 9)中随机选择,生成 1 到 10 个随机数。
这些数字组成集合 A(A 可以是可变集合,也可以不是)。同理,按此方法生成集合 B。每次新生成集合 A 和 B 后,显示 结果 A | B 和 A & B
'''

import random


def myRandom():
    mySet = set()
    count = random.randrange(1, 11, 1)
    for i in range(count):
        mySet.add(random.randint(0, 9))
    return mySet


if __name__ == "__main__":
    A = myRandom()
    B = myRandom()
    print A
    print B
    print u"A | B:"
    print A.union(B)
    print u"A & B:"
    print A.intersection(B)
