# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
在这个练习中，我们将实现 max()和 min()内建函数。
(a) 写分别带两个元素返回一个较大和较小元素，简单的 max2()核 min2()函数。他们应该可以
用任意的 python 对象运作。举例来说，max2(4,8)和 min2(4,8)会各自每次返回 8 和 4。
(b) 创建使用了在 a 部分中的解来重构 max()和 min()的新函数 my_max()和 my_min().这些函
数分别返回非空队列中一个最大和最小值。它们也能带一个参数集合作为输入。用数字和字符串来
测试你的解。
'''


def getReadyList(*mySeq):
    mySeq = [i for i in mySeq if isinstance(i, int) or
             isinstance(i, float) or
             i.isdigit()]
    myList = []
    for i in mySeq:
        if isinstance(i, str):
            if i.find('.') != -1:
                myList.append(float(i))
            else:
                myList.append(int(i))
        else:
            myList.append(i)
    return myList


def my_max(*mySeq):
    myList = getReadyList(*mySeq)
    maxValue = 0
    if len(myList) != 0:
        maxValue = myList[0]
        for i in myList:
            if i > maxValue:
                maxValue = i
    else:
        maxValue = u'元素不合法!'
    return maxValue


def my_min(*mySeq):
    myList = getReadyList(*mySeq)
    minValue = 0
    if len(myList) != 0:
        minValue = myList[0]
        for i in myList:
            if i < minValue:
                minValue = i
    else:
        minValue = u'元素不合法!'
    return minValue


def max2(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def min2(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


def main():
    print max2(4, 8)
    print min2(4, 8)
    print my_max('a', 3, '2.5t', '7', '5&', 0.5)
    print my_min('a', 3, '2.5t', '7', '5&', 0.5)

if __name__ == "__main__":
    main()
