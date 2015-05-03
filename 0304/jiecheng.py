#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
求解:
1! + 2! + 3! + 4! + ... + n!
'''

def jiecheng(n) :
    if n == 1 :
        return 1
    else :
        return n*jiecheng(n-1)

if __name__ == "__main__" :
    while True :
        n = raw_input("请输入一个整数：")
        if n.isdigit() :
            break
    n = int(n)
    mysum = 0
    while n > 0 :
        mysum += jiecheng(n)
        n -= 1
    print mysum
    

            
