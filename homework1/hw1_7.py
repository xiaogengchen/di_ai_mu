#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
7、只能⽤用while和print语句输出下⾯面的图样
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

if __name__ == "__main__" :
    row = 1
    while row < 6 :
        i = 1
        j = row
        while j < 5 :
            print " ",
            j += 1
        while i <= 2*row-1 :
            print "*",
            i += 1
        print
        row += 1
        
