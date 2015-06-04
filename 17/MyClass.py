# !/usr/bin/env python
# -*- coding:utf-8 -*-

u'''
此类为抽取日志文件中的ip地址
'''

import os


class FindIp(object):

    def __init__(self, path):
        self.txtFile = path

    def chou_sogou_ip(self):
        file1 = open(self.txtFile, 'r')
        ipList = []
        for line in file1:
            if line.find("Sogou") != -1:
                ipList.append(line.split()[0])
        file1.close()
        return set(ipList)

    def write_sogou_ip(self):
        myIpList = list(self.chou_sogou_ip())
        with open('myIp.txt', 'w') as myIptxt:
            myIptxt.writelines([line+'\n' for line in myIpList])

if __name__ == "__main__":
    findIp = FindIp("ip.txt")
#   myIpList = list(findIp.chou_sogou_ip())
#   print len(myIpList)
#   for ip in myIpList:
#      print ip
    findIp.write_sogou_ip()
