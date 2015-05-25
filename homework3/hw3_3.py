# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
gettysburg.txt是一个文件文件,请用函数,list,dict,文件读写等知识
分析该文本文件中单词个数(输出所有单词，并输出个数),输出不重复的单词和个数,
统计每个单词出现的次数,并输出单词和出现次数的表。
'''

import os


def countWords():
    myDict = {}
    with open(u'gettysburg.txt', u'r') as myFile:
        for line in myFile:
            myList = line.split()
            for word in myList:
                if word.isalpha():
                    if word not in myDict.keys():
                        myDict[word] = 1
                    else:
                        myDict[word] += 1
                else:
                    continue
    with open(u"myCount.txt", u'w') as myFile:
        myFile.write("单词" + "\t\t" + "次数" + os.linesep)
        for k, v in myDict.iteritems():
            myFile.write(u"%-15s\t%s" % (k, unicode(v) + os.linesep))


def main():
    countWords()


if __name__ == "__main__":
    main()
