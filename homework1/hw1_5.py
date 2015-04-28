#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
5、限定用while 循环和print语句输出以下样式
    样式一：
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
    样式二：
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    样式三：
        1
        2 1
        3 2 1
        4 3 2 1
        5 4 3 2 1
        6 5 4 3 2 1
'''

if __name__ == "__main__" :
    print "样式一:"
    num = 1 
    while num < 7 :
        i = 1
        while i <= num :
            print i,
            i += 1
        num += 1
        print

    print "样式二:"
    num = 6
    while num > 0 :
        i = 1
        while i <= num :
            print i,
            i += 1
        num -= 1
        print 

    print "样式三:"
    num = 1
    while num < 7 :
        i = num
        while i >= 1 :
            print i,
            i -= 1
        num += 1
        print

