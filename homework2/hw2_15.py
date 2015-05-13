# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
创建一个string.strip()的替代函数，自己写代码，去掉字符串前后的空格。
提示：要注意有多个空格的可能。
'''
import string


def myStrip(myStr=u""):
    pass

if __name__ == "__main__":
    myStr = u"hello world"
    print u"空格处理前:", myStr
    myStrip(myStr)
    #print u"空格处理后:", myStrip(myStr)