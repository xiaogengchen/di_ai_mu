#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
插入法对列表[3,88,76,23,999,22,888,56,39,72]进行排序
算法:N个元素用插入法排序
    1、取第一元素出来当成列表A,余下N-1个元素当成列表B
    2、取列表B中第一元素,与列表A中元素进行比较,大方后面,小放前面
    3、重复步骤2,直到将列表B中的元素取尽
'''


def charu(myList=[]):
    list_a = []
    list_a.append(myList[0])
    list_b = myList[1:]

    return list_a

if __name__ == "__main__":
    myList = [3, 88, 76, 23, 999, 22, 888, 56, 39, 72]
    print u"插入排序前:", myList
    myList = charu(myList)
    print u"插入排序后:", myList
