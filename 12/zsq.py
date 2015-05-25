# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
演示装饰器
'''

def logger(func):
    def inner(*args,**kwargs):
        print args
        print kwargs
        #return func(*args,**kwargs)
    return inner


@logger
def foo(x,y=1):
    return x + y


def main():
    print foo(8,9)


if __name__ == "__main__":
    main()