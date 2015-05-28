# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
用 map()进行函数式编程。写一个使用文件名以及通过除去每行中所有排头和最尾的空
白来“清洁“文件。在原始文件中读取然后写入一个新的文件，创建一个新的或者覆盖掉已存在的。
给你的用户一个选择来决定执行哪一个。将你的解转换成使用列表解析。
'''


def myFunction():
    srcFile = open('test.txt', 'r')
    targetFile = None
    while True:
        num = raw_input(u"创建一个新的或覆盖掉已存在的文件(1.创建  2.覆盖):")
        if num == '1':
            newFileName = raw_input(u"输入新的文件名:")
            targetFile = open(newFileName, 'w')
            break
        if num == '2':
            targetFile = open('testClean.txt', 'w')
            break
    lines = map((lambda x: x + '\n'), [line.strip() for line in srcFile])
#   列表解析
#   lines = [line.strip()+'\n' for line in srcFile]
    targetFile.writelines(lines)
    print u'转换完毕！'


def main():
    myFunction()


if __name__ == "__main__":
    main()
