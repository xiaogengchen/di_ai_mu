# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
字典和列表的方法：
1、创建一个字典，并把这个字典的键按照字母的顺序显示出来。
2、按照上面的字母排好顺序的键，显示出这个字典中的键和值
3、将字典中的值排好序，再按照排好的序输出键和值。
'''


def myFunction1(myDict={}):
    return sorted(myDict.keys())


def myFunction2(myDict={}):
    myList = myFunction1(myDict)
    for key in myList:
        print key, "-->", myDict[key]


def myFunction3(myDict={}):
    myList = myDict.items()
    tempList = []
    for (x, y) in myList:
        tempList.append((y, x))
    tempList = sorted(tempList)
    myList = []
    for (x, y) in tempList:
        myList.append((y, x))
    for (x, y) in myList:
        print x, "-->", y
    
       

if __name__ == "__main__":
    myDict = {'h': 3, 'c': 1, 'a': 3, 'e': 2, 'b': 4, 'd': 5}
    myList = myFunction1(myDict)
    print myList
    print "-"*25
    myFunction2(myDict)
    print "-"*25
    myFunction3(myDict)
