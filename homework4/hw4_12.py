# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
映射类型子类化。假设在 13.11.3 节中字典的子类，若将 keys()方法重写为：
                            def keys(self):
                                return sorted(self.keys())
                            (a) 当方法 keys()被调用，结果如何？
                                 答：抛出RuntimeError: maximum recursion depth exceeded异常
                            (b) 为什么会有这样的结果？如何使我们的原解决方案顺利工作？
                                  答：因为调用d.keys()返回的还是sorted(d.keys())。始终是同一个对象在调用keys()方法。
'''

class SortedKeyDict(dict):
    
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())
    
if __name__ == "__main__":
    d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))
    print 'By iterator:'.ljust(12), [key for key in d]
    print 'By keys():'.ljust(12), d.keys()