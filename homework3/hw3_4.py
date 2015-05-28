# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
自己将编程思路1、2中的文本文件转换代码实现一遍
(文件为test.txt)。
'''

import os


def myFunction():
    file1 = open('test.txt', 'r')
    file2 = open('test2.txt', 'w')
    while True:
        line = file1.readline()
        s1 = line.find('*编号***')
        s2 = line.find('公司行业：')
        s3 = line.find('公司性质：')
        s4 = line.find('公司规模：')
        if s1 > 0:
            file2.write(line)
            line = file1.readline()
            line = file1.readline()
            file2.write('公司名称：' + line)
        if s2 >= 0:
            file2.write(line[:s3] + os.linesep)
            file2.write(line[s3:s4] + os.linesep)
            file2.write(line[s4:])
            myList = []
            while True:
                line = file1.readline()
                s5 = line.find('*编号***')
                if s5 < 0:
                    myList.append(line.strip())
                if s5 > 0:
                    file2.write("公司简介：" + ''.join(myList) + os.linesep)
                    file2.write(line)
                    line = file1.readline()
                    line = file1.readline()
                    file2.write('公司名称:' + line)
                    break
                if not line:
                    file2.write('公司简介：' + ''.join(myList) + os.linesep)
                    break
        if not line:
            break
    file1.close()
    file2.close()


def main():
    myFunction()


if __name__ == "__main__":
    main()
