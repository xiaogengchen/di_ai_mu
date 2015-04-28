#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
3、用循环嵌套的方式计算连续整数之和，要求输出结果如下。如果输入数5，输出连续5个数字之和：
      1 = 1
      1+2 = 3
      1+2+3 = 6
      1+2+3+4 = 10
      1+2+3+4+5 = 15
'''

if __name__ == "__main__" :
    while True:
        num = raw_input("请输入数字:")
        if not num.isdigit() :
            continue
        num = int(num)
        mysum = 0 
        mystr = ''
        for i in range(1,num+1) :
            mysum += i
            if i != num :
              mystr += str(i) + '+'
            else :
              mystr +=str(i) +' = '
        print mystr+str(mysum)
        break
