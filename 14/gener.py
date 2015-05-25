# !/usr/bin/env python
# -*- coding:utf-8 -*-


def gener():
    yield "hello"
    yield "world"
    yield "welcome"
    

g = gener()
print g.next()
print g.next()
print g.next()