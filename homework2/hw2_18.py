# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
写2个字典，将2个字典合并起来。
'''


def unionDicts(dict1={}, dict2={}):
    mydict = dict()
    for k, v in dict1.items():
        mydict[k] = v
    for k, v in dict2.items():
        mydict[k] = v
    return mydict

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'d': 4, 'e': 5, 'f': 6}
    print unionDicts(dict1, dict2)
