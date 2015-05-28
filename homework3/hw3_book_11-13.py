# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
使用 reduce()进行函数式编程以及递归。在第 8 张中，我们看到 N 的阶乘或者 N!作为
从 1 到 N 所有数字的乘积。
(a) 用一分钟写一个带 x,y 并返回他们乘积的名为 mult(x,y)的简单小巧的函数。
(b)用你在 a 中创建 mult()函数以及 reduce 来计算阶乘。
(c)彻底抛弃掉 mult()的使用，用 lamda 表达式替代。
(d)在这章中， 我们描绘了一个递归解决方案来找到 N!用你在上面问题中完成的 timeit()函数，
并给三个版本阶乘函数计时(迭代的，reduce()以及递归）
'''

import time


def timeit(func, *args):
    start = time.clock()
    myList = func(*args)
    end = time.clock()
    return myList, end - start


def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return (N * factorial(N - 1))


def mult(x, y):
    return x * y


def myFunction1(N):
    return reduce(mult, range(1, N + 1))


def myFunction2(N):
    return reduce((lambda x, y: x * y), range(1, N + 1))


def myFunction3(N):
    return factorial(N)


def myFunction4(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result


def main():
    N = 5
    print u'reduce阶乘普通函数版'
    print timeit(myFunction1, N)
    print u'reduce阶乘lambda版'
    print timeit(myFunction2, N)
    print u'递归阶乘'
    print timeit(myFunction3, N)
    print u'迭代阶乘'
    print timeit(myFunction4, N)


if __name__ == "__main__":
    main()
