# !/usr/bin/env python
# -*- coding:utf-8 -*-
u'''
汉诺塔
n个盘子和A、B、C三个柱子
要求:n个盘子从上到下由小到大在A柱子上排列，要由A柱子上移动到C柱子上，可借助于B柱子，小盘子
     不可以放在大盘子下，一次只能移动一个盘子
算法:
    0、若1个盘子直接从A柱子上移动到C柱子上
    1、若n>1个盘子,先将A柱子上的n-1个盘子借助C柱子移动到B柱子上，再将A柱子上的第n个盘子移动到C柱子上
    2、将B柱子上n-2个盘子借助C柱子移动到A柱子上，再将B柱子上的第n-1个盘子移动到C柱子上
    3、将A柱子上的n-2个盘子根据前三步的方法循环移动到C柱子上
'''

def hannuo(n,A,B,C):
    if n == 1:
        print u'第 %d 个盘子由 %s 移到 %s' % (n, A, C)
    if n > 1 :
        hannuo(n-1, A, C, B)
        print u'第 %d 个盘子由 %s 移到 %s' % (n, A, C)
        hannuo(n-1, B, A, C)

if __name__ == "__main__":
    hannuo(2, u"A", u"B", u"C")