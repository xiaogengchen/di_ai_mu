#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
8、只能⽤用while和print语句输出下⾯面的图样
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *
* * * * * * *
* * * * *
* * *
*

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

if __name__ == "__main__" :
    print "图形一:"
    row = 1
    n = 2
    while row < 10 :
        if row < 6 :
            print "*"*(2*row-1)
        elif row > 6 :
            print "*"*(row-n)
            n += 3
        else :
            print "*"*(row+1)
        row += 1

    print "图形二:"
    row = 1
    n = 2
    space = 4
    while row < 10 :
        if row < 6 :
            print " "*space+"*"*(2*row-1)
            space -= 1
        elif row > 6 :
            print " "*space+"*"*(row-n)
            space += 1
            n += 3
        else :
            space = 1
            print " "*space+"*"*(row+1)
            space += 1
        row += 1
