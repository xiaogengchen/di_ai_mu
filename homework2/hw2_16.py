# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
用列表实现，将一个整型值，返回对应的英文值，
比喻89返回“eighty-nine”.假定值是0-1000之间。
'''


def myFunction(myNum):
    oneBitList = ["zero", "one", "two", "three", "four", "five",
                  "six", "seven", "eight", "nine"]
    twoBitTeenList = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                      "fifteen", "sixteen", "seventeen", "eighteen",
                      "nineteen"]
    twoBitList = ["twenty", "thirty", "fourty", "fifty",
                  "sixty", "seventy", "eighty", "ninty"]
    myNumLen = len(myNum)
    myNum = int(myNum)
    if myNumLen == 1:
        myNum = oneBitList[myNum]
    elif myNumLen == 2:
        tenBit = myNum // 10
        oneBit = myNum % 10
        if tenBit == 1:
            myNum = twoBitTeenList[oneBit]
        elif tenBit > 1 and oneBit != 0:
            myNum = twoBitList[tenBit - 2] + "-" + oneBitList[oneBit]
        else:
            myNum = twoBitList[tenBit - 2]
    elif myNumLen == 3:
        hundredBit = myNum // 100
        tenBit = myNum // 10 % 10
        oneBit = myNum % 10
        myNumTemp = oneBitList[hundredBit] + " hundred "
        if tenBit == 0 and oneBit != 0:
            myNumTemp += "and " + oneBitList[oneBit]
        elif tenBit == 1 and oneBit == 0:
            myNumTemp += "and " + twoBitTeenList[tenBit-1]
        elif tenBit == 1 and oneBit != 0:
            myNumTemp += "and " + twoBitTeenList[oneBit]
        elif tenBit > 1 and oneBit == 0:
            myNumTemp += "and " + twoBitList[tenBit-2]
        elif tenBit > 1:
            myNumTemp += "and " + twoBitList[tenBit-2] + "-" + \
                         oneBitList[oneBit]
        myNum = myNumTemp
    else:
        myNum = "one thousand"
    return myNum

if __name__ == "__main__":
    myNum = raw_input(u"请输入一个0~1000之间的数字:")
    while True:
        if myNum.isdigit() and 0 <= int(myNum) <= 1000:
            break
        myNum = raw_input(u"请输入一个0~1000之间的数字:")
    if len(myNum) != 1:
        myNum = myNum.lstrip("0")
    print myFunction(myNum)
