#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
测试函数文档字符串
'''

import def_doc_test

__author__='XiaoGengchen'
__version__='1.0'

class Foo(object):
    u'''演示类文档字符串'''
    pass

def mysum(x,y):
    '''加法的函数
return x+y
    '''
    return x+y ;

if __name__=='__main__':
    print Foo.__doc__
    print mysum.__doc__
    print def_doc_test.__doc__
    print ur'd:\nba'
