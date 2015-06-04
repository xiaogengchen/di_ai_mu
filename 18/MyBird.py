# !/usr/bin/env python
# -*- coding:utf-8 -*-

u'''
鸟类
'''

class Bird(object):
    def __init__(self):
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print "Aaaah..."
            self.hungry = False
        else:
            print "No. thanks!"

class SongBird(Bird):
    def __init__(self):
#        Bird.__init__(self)
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'
    
    def sing(self):
        print self.sound

if __name__ == "__main__":
    b = Bird()
    b.eat()
    b.eat()
    sb = SongBird()
    sb.eat()
    sb.eat()
    sb.sing()