# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
建立字典。
有2个长度相同的list，比喻[1,2,3] 和["a","b","c"],
用这2个list的数据组成一个这样的字典{1:"a",2:"b",3:"c"}
提示：用到zip()和dict()
'''


def myFunction(list1=[], list2=[]):
    myDict = {}
    for x, y in zip(list1,list2):
        myDict[x] = y
    return myDict


if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    print myFunction(list1, list2)
