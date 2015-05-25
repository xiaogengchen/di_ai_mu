# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
掷两个骰子(每个骰子有六面，1～6个点)
计算两个骰子之和
1、如果和为7或者11，玩家赢，庄家输；
2、如果和为2、3或12，玩家输，庄家赢；
3、如果和为4、5、6、8、9或10，则这个值称为“点数” t，重新掷骰子
    a.如果和为“点数” t，则玩家赢，庄家输；
    b.如果和为7，则玩家输，庄家赢；
    c.否则，重新掷骰子
'''

import random


def getPoint():
    return random.randint(1, 6) + random.randint(1, 6)


def craps():
    myPoint = getPoint()
    if myPoint in (7, 11):
        return u"玩家赢,庄家输(玩家点数 " + unicode(myPoint) + u" )"
    elif myPoint in (2, 3, 12):
        return u"玩家输,庄家赢(玩家点数 " + unicode(myPoint) + u" )"
    else:
        message = u''
        count = 2
        while True:
            myPoint2 = getPoint()
            if myPoint2 == myPoint:
                message = u"玩家赢,庄家输(玩家第1次点数 " + unicode(myPoint) + \
                                     u" ,玩家第" + unicode(count) + u"次点数 " + unicode(myPoint2) + u" )"
                break
            elif myPoint2 == 7:
                message = u"玩家输,庄家赢(玩家第1次点数 " + unicode(myPoint) + \
                                     u" ,玩家第" + unicode(count) + u"次点数 " + unicode(myPoint2) + u" )"
                break
            count += 1
        return message


def main():
    print craps()


if __name__ == "__main__":
    main()
