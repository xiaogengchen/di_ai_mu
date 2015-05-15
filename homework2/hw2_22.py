# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
颠倒字典中的键和值，将一个字典的键最为另一个字典的值，值作为另一个字典的键。
'''


def myFunction(myDict={}):
    myDict2 = {}
    for k,v in myDict.items():
        myDict2[v] = k
    return myDict2

if __name__ == "__main__":
    myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print myFunction(myDict)