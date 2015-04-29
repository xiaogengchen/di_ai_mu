#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
7、只能⽤用while和print语句输出下⾯面的图样
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

if __name__ == "__main__" :
    print "图形一:"
    row = 1 ;
    while row < 6 :
        print "*"*(2*row-1)
        row += 1

    print "图形二:"
    space = 5
    row = 1
    while row < 6 :
        print " "*space + "*"*(2*row-1)
        space -= 1
        row += 1
