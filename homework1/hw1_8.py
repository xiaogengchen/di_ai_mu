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
'''

if __name__ == "__main__" :
    row = 1
    while row < 10 :
        if row < 6 :
            i = 1
            j = row
            while j < 5 :
                print " ",
                j += 1
            while i <= 2*row-1 :
                print "*",
                i += 1
        else :
             i = 1
             j = 5
             while j < row :
                 print " ",
                 j += 1
             while i <= 19-2*row :
                 print "*",
                 i += 1
        row += 1    
        print
