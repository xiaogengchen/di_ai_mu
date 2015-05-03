#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
问:
1张大饼切100刀，总共能切多少块儿?
q(1) = 1 + 1 = 2
q(2) = 1 + 1 + 2 = 4
q(3) = 1 + 1 + 2 + 3 = 7
q(4) = 1 + 1 + 2 + 3 + 4 = 11
...
q(n) = q(n-1) + n
'''

def qie(n) :
    if n == 0 :
        return 1
    if n == 1 :
        return 2
    else :
        return qie(n-1) + n

if __name__ == "__main__" :
    n = 0
    while True :
        n = raw_input("请输入一个整数:")
        if n.isdigit() :
            break
    n = int(n)
    print qie(n)
