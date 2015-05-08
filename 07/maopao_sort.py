#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
冒泡法对列表[13,9,3,111,145,23]进行排序
算法:N个元素排序N-1次,每一次排序都是相邻元素进行比较，
    大的右移，第n次排序相邻元素比较N-n次,排序结果由小到大
'''

def maopao(myList=[]):
    u'''对myList列表进行冒泡排序,设置标记flag,如果在某轮排序
    结束后,flag标记没有变化,则证明列表已经排序好,余下轮的循环
    不必进行。
    '''
    for times in range(len(myList)-1):
        flag = true
        print "-"*times,myList
        for index in range(len(myList)-times):
            print '>'*(times+index),myList
            if index!=len(myList)-1 and myList[index] > myList[index+1] :
                myList[index],myList[index+1] = myList[index+1],myList[index]
                flag = flag
        if flag :
            break
        
    return myList


if __name__=="__main__":
    myList = [13,9,3,111,145,23]
    print u"冒泡排序前:",myList
    myList = maopao(myList)
    print u"冒泡排序后:",myList