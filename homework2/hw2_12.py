# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
在字符串模块中是不是有一个函数或方法可以鉴定一个字符串是另一个大字符串的一部分。
Strings. Are there any string methods or functions in the string module that will help me determine if a string is part of a larger string?
'''

'''
答:
string模块中的find和count方法可以鉴定一个字符串是否为另一个字符串的一部分
s1 = "hello world , I love python"
s2 = "o"
myFlag = string.find(s1,s2)
myIndex = string.index(s1,s2)
myCount = string.count(s1,s2)
myFlag不为-1,string.index(s1,s2)不抛异常,则证明s2是s1的子字符串,而myCount的值则代表在s1中有多少个s2子字符串。

'''