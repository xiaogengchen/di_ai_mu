# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
插入法对列表[3,88,76,23,999,22,888,56,39,72]进行排序

'''


def charu(myList=[]):
    for i in range(len(myList)):
        key = myList[i]
        j = i - 1
        while j > -1 and myList[j] > key:
            myList[j+1] = myList[j]
            j -= 1
        myList[j+1] = key
    return myList

if __name__ == "__main__":
    myList = [3, 88, 76, 23, 999, 22, 888, 56, 39, 72]
    print u"插入排序前:", myList
    myList = charu(myList)
    print u"插入排序后:", myList
