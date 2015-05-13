# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
1、用raw_input()函数输入数字，将这些数字用大到小排序。
2、输入字符串，按照字符串的a-z字典顺序排序。
提示：用到while循环和list
'''


def numberSort():
    while True:
        myNum = raw_input(u"请输入一串数字:")
        if not myNum.isdigit():
            myNum = raw_input(u"请输入一串数字:")
            continue
        break
    myList = []
    num = 0
    while num < len(myNum):
        myList.append(int(myNum[num]))
        num += 1
    myList.sort(reverse=True)
    print myList


def characterSort():
    while True:
        myStr = raw_input(u"请输入一串小写字母:")
        if not myStr.isalpha():
            myStr = raw_input(u"请输入一串小写字母:")
            continue
        break
    myList = []
    num = 0
    while num < len(myStr):
        myList.append(myStr[num])
        num += 1
    myList.sort()
    print myList

if __name__ == "__main__":
    numberSort()
    characterSort()
