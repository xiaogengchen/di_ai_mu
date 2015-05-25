# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
(a)编写一个字符翻译程序(功能类似于 Unix 中的 tr 命令)。我们将这个函数叫做 tr(),
   它有三个字符串做参数: 源字符串、目的字符串、基本字符串,语法定义如下:
   def tr(srcstr, dststr, string)
   srcstr的内容是你打算“翻译”的字符集合,
   dsrstr 是翻译后得到的字符集合,
   而 string 是 你打算进行翻译操作的字符串。
   举例来说,如果 srcstr == 'abc', dststr == 'mno', string == 'abcdef',
   那么 tr()的输出将是'mnodef'. 注意这里 len(srcstr) == len(dststr).
   在这个练习里,你可以使用内建函数 chr() 和 ord(), 但它们并不一定是解决这个问题所必不可少的函数。
(b)在这个函数里增加一个标志符参数,来处理不区分大小写的翻译问题。
(c)修改你的程序,使它能够处理删除字符的操作。字符串 srcstr 中不能够映射到字符串 dststr 中字符的多余字符都将被过滤掉。
   换句话说,这些字符没有映射到 dststr 字符串中的任何字符,因 此就从函数返回的字符里被过滤掉了。
   举例来说:如果 srcstr == 'abcdef', dststr == 'mno', string == 'abcdefghi',
   那么 tr()将输出'mnoghi'. 注意这里 len(srcstr) >= len(dststr).
'''


def tr(srcstr, dststr, string, ignorecase=True):
    myStr = u""
    if ignorecase:
        srcstr = srcstr.lower()
        myStr = string.replace(srcstr, dststr)
    else:
        myStr = string.replace(srcstr, dststr)
    return myStr
if __name__ == "__main__":
    print tr('abc', 'mno', 'abcdef')
    print tr('ABC', 'mno', 'abcdef')
    print tr('abcdef', 'mno', 'abcdefghi')
