# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
更新 easyMath.py。这个脚本，如例子 11.1 描绘的那样，以入门程序来帮助年轻人强
化他们的数学技能。通过加入乘法作为可支持的操作来更进一步提升这个程序。额外的加分：也加
入除法；这比较难做些因为你要找到有效的整数除数。幸运的是，已经有代码来确定分子比分母大，
所以不需要支持分数。
'''


from operator import add, sub, mul, div
from random import randint, choice

ops = {'+': add, '-': sub, '*': mul, '/': div}
MAXTRIES = 2

def doprob():
    op = choice('+-*/')
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d'%(pr, ans)
            else:
                print 'incorrect... try again'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'invalid input... try again'
def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()