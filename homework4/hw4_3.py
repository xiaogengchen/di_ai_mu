# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
对类进行定制。写一个类，用来将浮点型值转换为金额。在本练习里，我们使用美国货币，但读者也可以自选任意货币。
基本任务: 编写一个 dollarize()函数，它以一个浮点数值作为输入，返回一个字符串形式的金额数。比如说：
               dollarize(1234567.8901) ==> ‘$1,234,567.89.
               dollarize()返回的金额数里应该允许有逗号(比如 1,000,000)，和美元的货币符号。如果有负号，
               它必须出现在美元符号的左边。完成这项工作后，你就可以把它转换成一个有用的类，名为MoneyFmt。
               MoneyFmt 类里只有一个数据值(即，金额)， 和五个方法(你可以随意编写其他方法)。
               __init__()构造器对数据进行初始化，update()方法把数据值替换成一个新值，
               __nonzero__()是布尔型的，当数据值非零时返回 True，
               __repr__()方法以浮点数的形式返回金额；而__str__()方法采用和dollarize()一样的字符格式显示该值。
              (a) 编写 update()方法，以实现数据值的修改功能。
              (b) 以你已经编写的 dollarize()的代码为基础，编写__str__()方法的代码
              (c) 纠正__nonzero__()方法中的错误,这个错误认为所有小于1的数值,
                   例如,50美分($0.50),返回假值(False)。
              (d) 附加题: 允许用户通过一个可选参数指定是把负数数值显示在一对尖括号里还是显示一个负号。默认参数是使用标准的负号。
'''


class MoneyFmt(object):
    def __init__(self, money):
        self.flag = 0
        self.update(money)

    def update(self, money):
        self.money = money

    def __nonzero__(self):
        if self.money != 0:
            return True

    def __repr__(self):
        return self.money

    def __str__(self):
        return dollarize(self.money, self.flag)


def dollarize(myFloat=0.0, flag=0):
    myFloatStringList = unicode(abs(myFloat)).split(u'.')
    try:
        myFloatStringList[1] = \
            unicode(round(float(u'0.'+myFloatStringList[1]), ndigits=2))[1:]
    except IndexError, e:
        print u'传入的参数非浮点数'
        return
    myCount = len(myFloatStringList[0])/3
    tempList = []
    tempString = u''.join(myFloatStringList[0][::-1])
    j = 0
    for i in range(myCount+1):
        tempList.append(tempString[j:j+3][::-1] + u',')
        j = j + 3
    if tempList[-1].endswith(u','):
        tempList[-1] = tempList[-1][:-1]
    tempList.append(u'$')
    if myFloat < 0:
        tempList.append(u'-')
    myFloatStringList[0] = u''.join(tempList[::-1])[:-1]
    if myFloatStringList[0] == u'$':
        myFloatStringList[0] = u'$0'
    result = myFloatStringList[0] + myFloatStringList[1]
    if flag == 0:
        return result
    else:
        if result.startswith(u'-'):
            return u'<' + result[1:] + u'>'
        else:
            return result

if __name__ == "__main__":
    moneyFmt = MoneyFmt(-123456789.8901)
    moneyFmt.flag = -1
    print moneyFmt.__repr__()
    print moneyFmt.__str__()
    print moneyFmt.__nonzero__()
    moneyFmt.update(0.5)
    print moneyFmt.__repr__()
    print moneyFmt.__str__()
    print moneyFmt.__nonzero__()
