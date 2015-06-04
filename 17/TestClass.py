# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
python中的类 = 属性 + 方法
'''


class TestClass(object):
    u'''测试类属性和实例属性'''
    jishu = 100
    my_list = []

    def testJishu(self, number):
        '''定义实例属性'''
        self.jishu = number

    def print_jishu(self):
        print u'jishu, 我是实例变量:', self.jishu

if __name__ == "__main__":
    mytest = TestClass()
    mytest.testJishu(20)
    mytest.print_jishu()
    mytest.jishu += 1
    mytest.print_jishu()
    print TestClass.jishu
    TestClass.jishu += 1
    print TestClass.jishu
    mytest.my_list.append(1)
    print mytest.my_list
    TestClass.my_list.append(2)
    print TestClass.my_list
    print mytest.my_list
    pass
