# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
随机数。
熟读随机数模块然后解下面的题:
生成一个有 N 个元素的由随机数 n 组成的列表, 其中 N 和 n 的取值范围分别为: (1 <
N <= 100), (0 <= n <= 2**31 -1)。然后再随机从这个列表中取 N (1 <= N <= 100)个随机数 出来, 对它们排序,然后显示这个子集。
'''

import random


def myRandom():
    myList, mySet = [], set()
    N = random.randint(2, 100)
    for num in range(N):
        myList.append(random.uniform(0, 2**31-1))
    N2 = random.randint(1, N)
    for i in range(N2):
        mySet.add(random.choice(myList))
    return sorted(mySet)

if __name__ == "__main__":
    mySet = myRandom()
    for i in mySet:
        print i



