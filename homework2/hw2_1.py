# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
Given the following assignment:
items = ( ( 3 , 2 ) , ( 5 , 7 ) , ( 1 , 9 ) , 0 , ( 1 ) )
without writing a Python program or using the Python interpreter, answer the following:
1. What value is returned by len ( items )?
2. What is the value of items[1]?
3. print items[2][0] prints 1 but print items[3][0] causes a TypeError. Why is this given that items has more than 3 elements?
4. For items[x][y], what values of x and y cause the expression to evaluating to 9?
5. It might at first appear that the type of items[0] and the type of items[4] are the same.
(a) What are the types of these two expressions? 
(b) Why is the type of items[4] not tuple?
(c) If it was intended that items[4] be a tuple, how should the assignment be altered, without adding any new values?
'''

'''
Answer :

1、It returns 5
2、The value of items[1] is a tuple that is (5,7)
3、It's a value of items[3] , so print items[3][0] causes a TypeError . items[3] and items[4] are not tuple , but they are still elements in items . 
4、When x is 2 and y is 0 , the value is 9 .
5、(a)items[0] is a tuple and items[4] is a int value
   (b)Because it's a int value
   (c)If writed like (1,) , it is a tuple
'''