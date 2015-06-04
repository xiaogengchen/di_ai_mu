# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
python中的类 = 属性 + 方法
'''


class Person(object):
    '''此类描述Person类'''
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def saveMoney(self):
        print u"每月定期存款工资的一半,{0}元.".format(self.salary * 1.0 / 2)

    def consume(self):
        return self.salary * 1.0 / 2

    def consume_total(self):
        consume1 = 1000
        consume2 = 1200
        if consume1 + consume2 > self.consume():
            print self.name, u"消费超标"
        else:
            print self.name, u"还可以进行其他消费"

if __name__ == "__main__":
    person = Person("Tom", 4000)
    person.consume_total()
