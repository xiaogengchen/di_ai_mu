# -*- coding:utf-8 -*-
'''
百钱买百鸡，公鸡1只5钱，母鸡1只3钱，小鸡3只1钱
'''

if __name__ == "__main__":
    for x in range(21):
        for y in range(34):
            z = 100 - x - y
            if z%3==0 and x+y+z==100 and 5*x+3*y+z/3==100 :
                print "公鸡%d只,母鸡%d只,小鸡%d只。" % (x,y,z)
