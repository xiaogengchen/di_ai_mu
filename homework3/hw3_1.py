# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
写一个函数实现以下功能
找出一个列表的中位数，列表的元素都是浮点数。
列表中的元素个数为奇数：比喻L =[15.0, 5.3, 18.2], returns 15.0. 返回中位数
列表中的元素个数为偶数：比喻L =[1.0, 2.0, 3.0, 4.0], returns 2.5. 返回中间2位数之和/2
'''


def findMedian(L):
    L.sort()
    myMedian = 0
    if len(L) % 2 == 1:
        myMedian = L[len(L) / 2]
    else:
        myMedian = (L[(len(L) / 2) - 1] + L[len(L) / 2]) / 2
    return myMedian


def main():
    L1 = [15.0, 5.3, 18.2]
    L2 = [1.0, 2.0, 3.0, 4.0]
    print findMedian(L1)
    print findMedian(L2)

if __name__ == "__main__":
    main()
