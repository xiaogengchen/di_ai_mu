# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
几何. 创建一个由有序数值对(x, y) 组成的 Point 类，它代表某个点的 X 坐标和 Y 坐标。
         X 坐标和 Y 坐标在实例化时被传递给构造器，如果没有给出它们的值，则默认为坐标的原点。
'''


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return u'X:{x} Y:{y}'.format(x=self.x, y=self.y)

    __str__ = __repr__


if __name__ == "__main__":
    point1 = Point()
    point2 = Point(3, 5)
    print point1
    print point2
