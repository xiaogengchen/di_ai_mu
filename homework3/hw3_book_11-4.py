# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
返回值。给你在 5-13 的解创建一个补充函数。创建一个带以分为单位的总时间以及
返回一个以小时和分为单位的等价的总时间。
'''


def myFunction(myTime):
    myTime = int(myTime[:-1])
    myTime = divmod(myTime, 60)
    return myTime


def main():
    myTime = myFunction(u'197分')
    print unicode(myTime[0]) + u'小时' + unicode(myTime[1]) + u'分'
    

if __name__ == "__main__":
    main()