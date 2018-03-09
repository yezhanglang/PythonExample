#-*-coding:utf-8 -*-

import os
import shutil

try:
    with open("E:\jackson.txt", 'r') as f:
        for line in f:
        #for line in f.readlines(): 一次读取所有数据到内存
            print line
except Exception, e:
    print e

try:
    with open("E:\\tmp.txt", "a") as f:
        f.write("hahaha")
        f.flush()
except Exception, e:
    print e

print os.name
print os.environ #系统环境变量
print os.getenv('TMP')
print os.path.abspath(".") #当前目录

#单层目录
if os.path.exists("dir"):
    os.removedirs("dir")
else:
    os.mkdir("dir")

#多层目录
if os.path.exists("dir2\\dir"):
    os.removedirs("dir2\\dir")
else:
    os.makedirs("dir2\\dir")

#复制、删除
shutil.copy("E:\\tmp.txt","E:\\tmp2.txt")
os.remove("E:\\tmp.txt")

#当前目录下文件
print [x for x in os.listdir(".") if os.path.isfile(x)]

#命令行输入
while True:
    word = raw_input("输入单词：")
    print word