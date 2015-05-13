# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
以下语句
a = 10
b = 10
c = 100
d = 100
e = 10.0
f = 10.0
请问下面的表达式输出的值是：
a is b
c is d
e is f
id(a)
id(b)
id(c)
id(e)
id(f)
'''

'''
答:
a is b --> True
c is d --> True
e is f --> False
之所以会出现这样的结果是因为10和100在python的简单整数缓存范围
而-10不在这个范围。
python2.7.8版本的简单整数缓存范围为-5到256(包含-5和256)。
id(a) --> 30703024L
id(b) --> 30703024L
id(c) --> 30704848L
id(d) --> 30704848L
id(e) --> 38050576L
id(f) --> 38050552L
'''