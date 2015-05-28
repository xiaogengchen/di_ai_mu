# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
(a) 描述偏函数应用和 currying 之间的区别。
(b) 偏函数应用和闭包之间有什么区别？
(c) 最后，迭代器和生成器是怎么区别开的？
'''

'''
答:
(a)
偏函数应用：找一个函数，固定其中的几个参数值，从而得到一个新的函数。（通过functional模块中partial()函数来创建）
currying:函数加里化是一种使用匿名单参数函数来实现多参数函数的方法。
(b)
偏函数应用：找一个函数，固定其中的几个参数值，从而得到一个新的函数。（通过functional模块中partial()函数来创建）
闭包：在一个内部系统里，对在外部作用域（但不是全局作用域）的变量进行引用，那么内部函数就被认为是闭包。
(c)
迭代器：有next()方法和__iter__()方法的容器对象就是迭代器（实现了迭代协议）。
生成器：有yield关键字的函数就是生成器。
'''