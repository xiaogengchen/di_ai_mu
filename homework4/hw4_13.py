# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
类的定制。改进脚本 time60.py，见 13.13.2 节，示例 13.3.
                  (a) 允许“空”实例化: 如果小时和分钟的值没有给出，默认为零小时、零分钟。
                  (b) 用零占位组成两位数的表示形式,因为当前的时间格式不符合要求。如下面的示例，wed
                       应该输出为“12:05.”
                       >>> wed = Time60(12, 5)
                       >>> wed
                       12:5
                  (c)除了用 hours (hr) 和 minutes (min)进行初始化外，还支持以下时间输入格式：
                      一个由小时和分钟组成的元组(10, 30)
                      一个由小时和分钟组成的字典({'hr': 10, 'min': 30})
                      一个代表小时和分钟的字符串("10:30")
                  附加题: 允许不恰当的时间字符串表示形式，如 “12:5”.
                  (d) 我们是否需要实现__radd__()方法? 为什么? 如果不必实现此方法，那我们什么时候可
                       以或应该覆盖它?
                  (e) __repr__()函数的实现是有缺陷而且被误导的。我们只是重载了此函数，这样我们可以省
                      去使用 print 语句的麻烦，使它在解释器中很好的显示出来。但是，这个违背了一个原则:对于可估
                      值的 Python 表达式，repr()总是应该给出一个(有效的)字符串表示形式。12:05 本身不是一个合法
                      的 Python 表达式，但 Time60('12:05')是合法的。请实现它。
                  (f) 添加六十进制(基数是 60)的运算功能。下面示例中的输出应该是 19:15，而不是 18:75:
                       >>> thu = Time60(10, 30)
                       >>> fri = Time60(8, 45)
                       >>> thu + fri
                      18:75
'''

class Time60(object):
    def __init__(self, hr=0, min=0):
        self.hr = hr
        self.min = min
    '''
    def __init__(self, *args, **kwargs):
        if issubclass(args[0].__class__, tuple):
            self.hr = args[0][0]
            self.min = args[0][1]
        if issubclass(args[0].__class__, dict):
            self.hr = args[0].get("hr")
            self.min = args[0].get("min")
        if issubclass(args[0].__class__, str):
            self.hr = int(args[0].split(":")[0])
            self.min = int(args[0].split(":")[1])
    '''
    def __str__(self):
        return '%02d:%02d' % (self.hr, self.min)
    
    def __add__(self, other):
        tempTime = self.__class__(self.hr + other.hr, self.min + other.min)
        tempTuple = divmod(tempTime.min,60)
        tempTime.hr += tempTuple[0]
        tempTime.min = tempTuple[1]
        return tempTime
    
if __name__ == "__main__":
    time61 = Time60(10,30)
    time62 = Time60(8,45)
    '''
    time62 = Time60({'hr': 8, 'min': 45})
    time63 = Time60("8:45")  
    print time61,vars(time61)
    print time62,vars(time62)
    print time63,vars(time63)
    '''
    print time61 + time62