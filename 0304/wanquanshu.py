#!/usr/bin/python
#-*-coding:utf-8-*-

'''
1000以内完全数测试
如果数字n等于所有n能整除1到n-1的数字的和，则n为完全数
例如：6 = 1 + 2 + 3
'''

for num in range(1,1001):
    i = 1 ;
    sum = 0 ;
    while i < num :
        if num % i == 0 :
            sum += i
        i += 1
    if sum == num :
        print str(num)+"是完全数!"
