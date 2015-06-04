# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
类方法测试
'''


class Foo(object):
    def test(self):
        print "in test()"

    @classmethod
    def foo(cls,x):
        print "in foo() ", x
        print cls


if __name__ == "__main__":
    p = Foo()
    Foo.foo("hi")
    p.foo("hello")