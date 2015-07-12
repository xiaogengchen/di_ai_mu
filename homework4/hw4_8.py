# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
堆栈类。一个堆栈(Stack)是一种具有后进先出(last-in-first-out，LIFO)特性的数
              据结构。我们可以把它想象成一个餐盘架。最先放上去的盘子将是最后一个取下来的，而最后一个
              放上去的盘子是最先被取下来的。你的类中应该有 push()方法(向堆栈中压入一个数据项)和 pop()
              方法(从堆栈中移出一个数据项)。还有一个叫 isempty()的布尔方法，如果堆栈是空的，返回布尔值
              1,否则返回 0；一个名叫 peek()的方法，取出堆栈顶部的数据项，但并不移除它。
              注意，如果你使用一个列表来实现堆栈，那么 pop()方法从 Python1.5.2 版本起已经存在了。那
              就在你编写的新类里，加上一段代码检查 pop()方法是否已经存在。如果经检查 pop()方法存在，就
              调用这个内建的方法；否则就执行你自己编写的 pop()方法。你很可能要用到列表对象；如果用到它
              时，不需要担心实现列表的功能(例如，切片)。只要确保你写的堆栈类能够正确实现上面的两项功
              能就可以了。你可以用列表对象的子类或自己写个类似列表的对象，请参考示例 6.2.              
'''

class MyStack(object):
    def __init__(self):
        self.myList = list()
    
    def push(self, value):
        self.myList.append(value)
    
    def pop(self):
        if self.myList.pop != None:
            return self.myList.pop()
        else:
            value = self.myList[-1]
            self.myList = self.myList[:-1]
            return value
    
    def isempty(self):
        if len(self.myList) == 0:
            return 1
        else:
            return 0
    
    def peek(self):
        return self.myList[-1]
    
if __name__ == "__main__":
    ms = MyStack()
    ms.push(1)
    ms.push(2)
    ms.push(3)
    ms.push(4)
    print ms.myList
    print ms.isempty()
    print ms.peek()
    print ms.myList
    ms.pop()
    print ms.myList