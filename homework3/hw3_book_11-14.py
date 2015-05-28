# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
递归。我们也来看下在第八章中的 Fibonacci 数字。重写你先前计算 Fibonacci 数字
的解(练习 8-9）以便你可以使用递归。
'''


def fibonacci(N):
    if N == 1 or N == 2:
        return 1
    else :
        return fibonacci(N - 1) + fibonacci(N - 2)


def main():
    print fibonacci(6)


if __name__ == "__main__":
    main()