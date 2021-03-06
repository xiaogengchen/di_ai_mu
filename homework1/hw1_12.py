#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
12、解释"is "和"=="之间的差异,示例说明,对is 返回为假，== 返回为真。

答：is和==都是比较运算符。is比较的是两个变量所引用对象的id值是否一致，==比较的是两个变量所引用对象的值是否一致。
以此看来==的条件更宽泛一些而is的条件更苛刻一些。

举例如下：
>>> a = (1,2,3)
>>> b = (1,2,3)
>>> a is b    ---> False
>>> a == b    ---> True

'''
