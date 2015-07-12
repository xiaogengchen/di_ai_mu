# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
堆栈和队列。编写一个类，定义一个能够同时具有堆栈(FIFO)和队列(LIFO)操作行为的数据结构。
                     这个类和 Perl 语言中数组相像。需要实现四个方法：
                     shift() 返回并删除列表中的第一个元素，类似于前面的 dequeue()函数。
                     unshift()  在列表的头部"压入"一个新元素
                     push() 在列表的尾部加上一个新元素，类似于前面的 enqueue()和 push()方法。
                     pop() 返回并删除列表中的最后一个元素，与前面的 pop()方法完全一样。            
'''

class MySQ(object):
    def __init__(self):
        self.myList = list()
    
    def shift(self):
        value = self.myList[0]
        self.myList = self.myList[1:]
        return value
    
    def unshift(self, value):
        self.myList.insert(0, value)
    
    def push(self, value):
        self.myList.append(value)
    
    def pop(self):
        if self.myList.pop != None:
            return self.myList.pop()
        else:
            value = self.myList[-1]
            self.myList = self.myList[:-1]
            return value
    
if __name__ == "__main__":
    ms = MySQ()
    ms.push(1)
    ms.push(2)
    ms.push(3)
    ms.push(4)
    ms.unshift(5)
    print ms.myList
    ms.shift()
    print ms.myList
