#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
普通字符串与unicode字符串之间的转换
'''
# import 
__author__='XiaoGengchen'
__version__='1.0'

def strToUnicode(plainString=''):
    '''普通字符串向unicode字符串的转换用decode'''
    temp_str = plainString.decode("utf-8")
    print temp_str,type(temp_str)

def unicodeToStr(unicodeString=u'') :
    '''unicode字符串向普通字符串之间的转换encode'''
    utf8String = unicodeString.encode("gbk")
    print utf8String,type(utf8String)

if __name__=="__main__":
    unicodeToStr(u"你好world")
    strToUnicode("你好world")
