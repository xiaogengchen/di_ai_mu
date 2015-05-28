# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
变长参数。下一个称为 printf()的函数。有一个值参数，格式字符串。剩下的就是根
据格式化字符串上的值，要显示在标准输出上的可变参数，格式化字符串中的值允许特别的字符串
格式操作指示符，如%d, %f, etc。提示：解是很琐碎的----无需实现字符串操作符功能性，但你需
要显示用字符串格式化操作（%）
'''


def printf(strFormat, *args):
    print strFormat % args


def main():
    printf("%d , %f", 5,0.5)


if __name__ == "__main__":
    main()