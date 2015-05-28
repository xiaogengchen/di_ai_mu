# !/usr/bin/env python
# -*-coding:utf-8-*-

'''
用 map() 进 行 函 数 式 编 程 。 给 定 一 对 同 一 大 小 的 列 表 ， 如 [1 ， 2 ， 3] 和
['abc','def','ghi',....]，将两个标归并为一个由每个列表元素组成的元组的单一的表，以使我
们的结果看起来像这样：{[(1, 'abc'), (2, 'def'), (3, 'ghi'), ...}.（虽然这问题在本质上和
第六章的一个问题相似，那时两个解没有直接的联系）然后创建用 zip 内建函数创建另一个解。
'''


def main():
    list1 = [1, 2, 3]
    list2 = ['abc', 'def', 'ghi']
    print map((lambda x, y: (x, y)), list1, list2)
    print zip(list1, list2)

if __name__ == "__main__":
    main()
