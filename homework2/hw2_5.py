# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
Examine the following code:
a = 10
b = 20
print "Before swapping a=%d, b=%d" % ( a , b ) #Swap values
a=b
b=a
print "After swapping a=%d, b=%d" % ( a , b )
1. Try running this small program. What are the values of a and b after the swap?
2. Why is the result not a having the value 20 and b having the value 10 as appears to be the intention from the use of the word swap in the code?
3. Modify the code so that the final result is a having the value 20 and b having the value 10 using simultaneous assignment to swap the values.
4. Many languages, such as C, C++, Java, do not have simulta- neous assignment. Modify the program so that it successfully swaps the two values without using simultaneous assignment.
1. Both a and b have the value 20.
2. Becausethelinea=bsetsato20,leavingbasitwas. 
3. a,b=b,a
4. a = 10 b = 20
print "Before swapping a=%d, b=%d" % (a, b) # Swap values
temp = a
a=b
b = temp
print "After swapping a=%d, b=%d" % (a, b)
'''

'''
Answer :

1、a and b have the same value 20
2、If wanted a have 20 and b have 10 , we can operate a and b like this :
   1)
     temp = a
     a = b
     b = temp
   2)
     a, b = b, a
3、a, b = b, a
4、
  a = 10
  b = 20
  print "Before swapping a=%d, b=%d" % ( a , b ) #Swap values
  temp = a 
  a = b
  b = temp
  print "After swapping a=%d, b=%d" % ( a , b )
'''