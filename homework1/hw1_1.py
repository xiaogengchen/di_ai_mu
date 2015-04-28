#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
1、请写出一下逻辑表达式的值
    False and None
    0 and None or () and []
    True and None or () and []
    0 or None and () or []
    True or None and () or []
    1 or None and 'a' or 'b'

答：and所连接的N个操作数有一个值为False，表达式结果就为False
       or所连接N个操作数有一个值为True，表达式结果就为True
       and优先级高于or

       因此，结果如下：
       False and None                       -->    False
       0 and None or () and []            -->    False
       True and None or () and []       -->    False
       0 or None and () or []              -->    False
       True or None and () or []         -->    True
       1 or None and 'a' or 'b'            -->    True
'''

if __name__=="__main__" :
    print False and None
    print 0 and None or () and []
    print True and None or () and []
    print 0 or None and () or []
    print True or None and () or []
    print 1 or None and 'a' or 'b'