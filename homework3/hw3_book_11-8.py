# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
用 filer()进行函数式编程.使用练习 5-4 你给出的代码来决定闰年。更新你的代码一
边他成为一个函数如果你还没有那么做的话。然后写一段代码来给出一个年份的列表并返回一个只
有闰年的列表。然后将它转化为用列表解析。
'''


def leapYear(year):
    if year % 400 == 0:
        return year
    elif year % 100 != 0 and year % 4 == 0:
        return year
        

def main():
    myList = [i for i in range(1000, 3001)]
    print filter(leapYear, myList)

if __name__ == "__main__":
    main()