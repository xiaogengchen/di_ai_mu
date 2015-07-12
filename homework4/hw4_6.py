# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
几何. 创建一个直线/直线段类。 除主要的数据属性： 一对坐标值(参见上一个练习)外，
         它还具有长度和斜线属性。你需要覆盖__repr__()方法(如果需要的话，还有__str__()方法)，使得
         代表那条直线(或直线段)的字符串表示形式是由一对元组构成的元组，即，((x1, y1), (x2, y2)).
         总结：
                 __repr__ 将直线的两个端点(始点和止点)显示成一对元组
                 length 返回直线段的长度 - 不要使用"len", 因为这样使人误解它是整数。
                 slope  返回此直线段的斜率(或在适当的时候返回 None)
'''

import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return u'({x} ,{y})'.format(x=self.x, y=self.y)

    __str__ = __repr__


class Line(object):
    def __init__(self, point1=Point(), point2=Point()):
        self.point1 = point1
        self.point2 = point2
        self.length = round(math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2), 2)
        self.slop = round((point2.y-point1.y)*1.0/(point2.x-point1.x), 2)

    def __repr__(self):
        return u'({point1},{point2})'.format(point1=self.point1, point2=self.point2)


if __name__ == "__main__":
    line1 = Line(point1=Point(2, 3), point2=Point(5, 8))
    print line1
    print line1.length
    print line1.slop
