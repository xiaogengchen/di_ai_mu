# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
默认参数。更新你在练习 5-7 中创建的销售税脚本以便让销售税率不再是函数输入的必要之物。
创建使用你地方税率的默认参数如果在调用的时候没有值传入。
'''


def myTax(price, taxRate=0.03):
    return price * taxRate


def main():
    print myTax(100)
    print myTax(200, 0.05)


if __name__ == "__main__":
    main()