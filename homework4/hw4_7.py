# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
数据类。提供一个 time 模块的接口，允许用户按照自己给定时间的格式，比如:
              “MM/DD/YY,” “MM/DD/YYYY,” “DD/MM/YY,” “DD/MM/ YYYY,” “Mon DD, YYYY,” 或是标准
              的 Unix 日期格式： “Day Mon DD, HH:MM:SS YYYY” 来查看日期。你的类应该维护一个日期值，
              并用给定的时间创建一个实例。如果没有给出时间值，程序执行时会默认采用当前的系统时间。
              还包括另外一些方法：
              update() 按给定时间或是默认的当前系统时间修改数据值
              display() 以代表时间格式的字符串做参数，并按照给定时间的格式显示:
              'MDY' ==> MM/DD/YY
              'MDYY' ==> MM/DD/YYYY
              'DMY' ==> DD/MM/YY
              'DMYY' ==> DD/MM/YYYY
              'MODYY' ==> Mon DD, YYYY
              如果没有提供任何时间格式，默认使用系统时间或 ctime()的格式。附加题: 把这个类和练习
              6-15 结合起来。
'''

import time
import datetime

class myTime(object):
    def __init__(self, value=time.time(), fmt="MDY"):
        self.value = value
        self.fmt = fmt
    def update(self,value):
        self.value = value
    def display(self,fmt="MDY"):
        if fmt=="MDY":
            result = time.strftime("%m/%d/%y", time.localtime(self.value))
        if fmt=="MDYY":
            result = time.strftime("%m/%d/%Y", time.localtime(self.value))
        if fmt=="DMY":
            result = time.strftime("%d/%m/%y", time.localtime(self.value))
        if fmt=="DMYY":
            result = time.strftime("%d/%m/%Y", time.localtime(self.value))
        if fmt=="MODYY":
            result = time.strftime("%m %d,%Y", time.localtime(self.value))
        print result

if __name__=="__main__":
    mt = myTime()
    timeArray = time.strptime('05/19/2015', "%m/%d/%Y")
    mt.update(time.mktime(timeArray))
    mt.display("MODYY")