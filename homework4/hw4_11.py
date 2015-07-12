# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
电子商务。你需要为一家 B2C(商业到消费者)零售商编写一个基础的电子商务引擎。 
                  你需要写一个针对顾客的类 User, 一个对应存货清单的类 Item, 
                  还有一个对应购物车的类叫 Cart. 货物放到购物车里， 顾客可以有多个购物车。
                  同时购物车里可以有多个货物，包括多个同样的货物。            
'''

    
class Item(object):
    def __init__(self):
        self.item = list()
    
    def __str__(self):
        return self.item
            
class Cart(object):
    def __init__(self):
        self.items = list()
        
    def __str__(self):
        return self.items

class User(object):
    def __init__(self):
        self.carts = list()
    
    def __str__(self):
        myStr = u''
        for cart in self.carts:
            for item in cart.items:
                    myStr += item.item[0] + u"-->" + item.item[1] + u"\r\n"
        return myStr.encode('gbk')
        
        
            
if __name__=="__main__":
    item1 = Item()
    item1.item.append(u"货号1")
    item1.item.append(u"货名a")
    item2 = Item()
    item2.item.append(u"货号2")
    item2.item.append(u"货名b")
    item3 = Item()
    item3.item.append(u"货号3")
    item3.item.append(u"货名c")
    cart1 = Cart()
    cart1.items.append(item1)
    cart1.items.append(item2)
    cart2 = Cart()
    cart2.items.append(item3)
    user = User()
    user.carts.append(cart1)
    user.carts.append(cart2)
    print user