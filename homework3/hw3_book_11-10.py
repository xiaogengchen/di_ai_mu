# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
用 filter()进行函数式编程。在 unix 文件系统中，在每个文件夹或者目录中都有两个
特别的文件：'.'表示现在的目录，'..'表示父目录。给出上面的知识，看下 os.listdir()函数的文
档并描述这段代码做了什么：
files = filter(lambda x: x and x[0] != '.', os. listdir(folder))
'''

'''
答:
files的值为一个字符串列表，列表内容为folder这个文件夹下的文件名和目录名，但不包括以“.”开头的文件名和目录名
'''
