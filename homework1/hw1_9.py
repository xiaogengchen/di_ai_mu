#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
9、编写⼀一个程序，⽣生成下⾯面的算术⽰示例。
1 * 8 + 1 = 9
12 * 8 + 2 = 98
123 * 8 + 3 = 987
1234 * 8 + 4 = 9876
12345 * 8 + 5 = 98765
123456 * 8 + 6 = 987654
1234567 * 8 + 7 = 9876543
12345678 * 8 + 8 = 98765432
123456789 * 8 + 9 = 987654321
'''

if __name__ == "__main__" :
    num = 1
    while num < 10 :
        mynum = ""
        i = 1
        while i <= num :
            mynum += str(i)
            i += 1
        print mynum + " * 8 + " + str(num) + " = " + str(int(mynum)*8+num)
        num += 1
        print
        
