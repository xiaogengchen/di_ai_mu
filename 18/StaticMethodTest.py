# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
静态方法测试
'''


class Foo(object):
    def test(self):
        print "in test()"

    @staticmethod
    def foo(x):
        print "in foo() ", x


if __name__ == "__main__":
    p = Foo()
    Foo.foo("hello")
    p.foo("world")
    p.test()
