#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
题:
警察抓了a,b,c,d4名犯罪嫌疑人，其中有一名是小偷，审讯中：
    a说我不是小偷
    b说c是小偷
    c说小偷肯定是d
    d说c胡说
其中有三人说的是实话，一人说的是假话
问:谁是小偷?

'''

if __name__ == "__main__" :
    for xiaotou in ['a','b','c','d'] :
        result = (xiaotou != 'a') + (xiaotou == 'c') + (xiaotou == 'd') + (xiaotou != 'd')
        if result == 3 :
            print "小偷是:%s " % xiaotou
