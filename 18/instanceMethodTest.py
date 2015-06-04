# !/usr/bin/env python
# -*- coding:utf-8 -*-

u'''
类中实例对象调用方法
'''


class Foo(object):
    def test(self):
        print "in test()"

if __name__ == "__main__":
    p = Foo()
    p.test()
    Foo.test(p) #同p.test()
