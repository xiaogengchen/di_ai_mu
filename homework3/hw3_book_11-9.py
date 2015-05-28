# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
用 reduce()进行函数式编程。复习 11.7.2 部分，阐述如何用 reduce()数字集合的累
加的代码。修改它，创建一个叫 average()的函数来计算每个数字集合的简单的平均值。
'''


def average(myList=[]):
    return reduce((lambda x, y: x+y), myList)*1.0/len(myList)


def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print average(myList)
    

if __name__ == "__main__":
    main()