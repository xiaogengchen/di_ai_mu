# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
队列类。一个队列(queue)是一种具有先进先出(first-in-first-out，FIFO)特性的数
              据结构。一个队列就像是一行队伍，数据从前端被移除，从后端被加入。这个类必须支持下面几种
              方法:
                     enqueue()  在列表的尾部加入一个新的元素
                     dequeue()  在列表的头部取出一个元素，返回它并且把它从列表中删除。        
'''

class MyQueue(object):
    def __init__(self):
        self.myList = list()
    
    def enqueue(self, value):
        self.myList.append(value)
    
    def dequeue(self):
        value = self.myList[0]
        self.myList = self.myList[1:]
        return value
    
    
if __name__ == "__main__":
    ms = MyQueue()
    ms.enqueue(1)
    ms.enqueue(2)
    ms.enqueue(3)
    ms.enqueue(4)
    print ms.myList
    ms.dequeue()
    print ms.myList