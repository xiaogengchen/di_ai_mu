# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
设计一个代码，可以检测字符串是长度，也可以判断字符串长度为一，还可以判断该字符串是不是python关键词
对后一个要求需要用到 
import keyword
keyword.kwlist
'''

import keyword


def checkString(myStr=""):
    strCount = len(myStr)
    isKeyword = myStr in keyword.kwlist
    if isKeyword:
        isKeyword = "is"
    else:
        isKeyword = "is not"
    print "%s's length is %s and it %s python keyword" % \
          (myStr, strCount, isKeyword)

if __name__ == "__main__":
    myStr = "myfor"
    checkString(myStr)
