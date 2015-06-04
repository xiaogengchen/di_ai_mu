# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
python中的类 = 属性 + 方法
'''


class Foo(object):
    u'''定义一个Foo类'''
    num = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def print_xy(self):
        print self.x, self.y

p = Foo(10, 15)
p.print_xy()
print dir(Foo)
print Foo.__dict__
print Foo.__doc__
print Foo.__name__
print Foo.__module__
