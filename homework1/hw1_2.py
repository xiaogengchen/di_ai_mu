#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
2、有多少个三位整数能被17整除？将之输出。
'''

if __name__ == "__main__" :
    count = 0
    for num in range(100,1000) :
        if num % 17 == 0:
            count += 1
            print str(num)+" 能被17整除."
    print "有 " + str(count) + " 个三位数能被17整除."