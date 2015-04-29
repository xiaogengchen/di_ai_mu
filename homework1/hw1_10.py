#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
10、下⾯面的代码x=4时会发⽣生什么情况？
while True :
    for x in range(6):
        y = 2*x + 1
        print y
        if y>9 :
            break

答：外层是一个死循环，x等于4的时候会输出9，内层for循环不会结束，当x=5的时候内层for循环会结束，
程序继续在外层死循环中执行，内层的for循环会不停输出1、3、5、7、9、11。
'''

if __name__ == "__main__" :
    while True :
        for x in range(6):
            y = 2*x + 1
            print y
            if y>9 :
                break
