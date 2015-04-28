#!/usr/bin/python
#-*-coding:utf-8-*-

'''
猜数,随机生成一个数字，猜该数字的值是多少，猜错提示并继续猜
'''

import random
import string

num = random.randint(0,100)

while True:
    myNum = raw_input("请输入一个数字:")
    if not myNum.isdigit() :
        continue
    myNum = int(myNum)
    if myNum == num :
        print "猜对了!"
        break
    elif myNum > num :
        print "您的数字偏大,请继续猜..."
    else :
        print "您的数字偏小,请继续猜..."
    
