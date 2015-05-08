#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
字符串与列表之间的相互转换
'''

def strToList(mystr=''):
    '''字符串转为列表'''
    return mystr.split()

def listTostr(mylist=[]):
    '''列表转为字符串'''
    return "".join(mylist)

if __name__=="__main__":
    print strToList('hello,world')
    print listTostr(['hello','100'])