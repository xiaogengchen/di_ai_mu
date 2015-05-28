# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
日志文件抽取搜狗的不重复IP,
先用过程化语言实现一遍，再用函数做一遍，最后用生成器做一遍。
（文件为ip.txt）
'''


def myFunction(myFile=''):
    mySet = set()
    for line in myFile:
        myIndex = line.find("Sogou web spider")
        if myIndex != -1:
            mySet.add(line.split()[0])
    return mySet


def main():
    myFile = open('ip.txt', 'r')
    mySet = myFunction(myFile)
    print u"共有不重复ip " + unicode(len(mySet)) + u' 个,如下:'
    for ip in mySet:
        print ip

if __name__ == "__main__":
    main()
