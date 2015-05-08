#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
选择法对列表[7,9,3,11,45,23,12,87,234,11,5,93]进行排序
算法:N个元素,排序N-1次,第一次排序假设第一元素为最小,将其与余下的元素进行
    比较,如果发现有比其更小的元素则将其与之交换位置,交换后该位置的元素继续
    与其后的元素进行比较,如果发现有比其小的则继续与之交换,第一次结束后第一个
    位置上为最小的元素,第二次排序的时候,假设第二个元素为最小,与其后的元素进行
    比较，第二次结束后,第二个位置上的元素为本组数中第二小的元素,依次类推直到
    第N-1次。
'''

def xuanze(myList=[]):
    for times in range(len(myList)):
        print '-'*times,myList
        for index in range(times+1,len(myList)):
            print '>'*(index+times),myList
            if myList[times] > myList[index]:
                myList[times],myList[index] = myList[index],myList[times]
    return myList

if __name__ == "__main__":
    myList = [7,9,3,11,45,23,12,87,234,11,5,93]
    print u"选择排序前:",myList
    myList = xuanze(myList)
    print u"选择排序后:",myList