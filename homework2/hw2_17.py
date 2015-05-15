# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
写一个函数，返回跟一个输入的字符串相似的字符串，要求字符串的大小写反转。
比如输入“Mr.ED”，返回“mR.ed”
'''

import string


def translateCharacter(myStr=u""):
    myList = []
    for character in myStr:
        if character in string.uppercase:
            myList.append(chr(ord(character)+32))
        elif character in string.lowercase:
            myList.append(chr(ord(character)-32))
        else:
            myList.append(character)
    return "".join(myList)

if __name__ == "__main__":
    myStr = raw_input(u"请输入一个带英文字母的字符串:")
    while True:
        flag = False
        for character in myStr:
            if character in string.letters:
                flag = True
                break
        if flag:
            break
        myStr = raw_input(u"请输入一个带英文字母的字符串:")
    print translateCharacter(myStr)
