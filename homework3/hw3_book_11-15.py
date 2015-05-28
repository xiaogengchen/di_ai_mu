# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
递归。从写练习 6-5 的解，用递归向后打印一个字符串。用递归向前以及向后打印一个
字符串。
'''


def myFunction1(myStr, start=0):
    if start != len(myStr):
        myFunction1(myStr, start+1)
        print myStr[start],


def myFunction2(myStr, start=0):
    if start != 0:
        myFunction2(myStr, start-1)
        print myStr[start-1],


def main():
    myFunction1("hello")
    print
    myFunction2("hello", len("hello"))


if __name__ == "__main__":
    main()
