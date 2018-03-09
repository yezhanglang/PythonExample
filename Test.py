# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
import urllib


params = {
    'pos' : 0
    ,'idfa': 'dsdf'
    ,'ip' : '127.0.0.1'
    ,'from' : 'UCLLQ'
    ,'callback' : 'http://www.baidu.com'}
params = urllib.urlencode(params)
ret = urllib.urlopen("http://iphone.v0.mgtv.com/ggt.php", params)
status_code = ret.getcode()
print status_code
print ret.read()
'''

sent = []
sent.extend("sd,gd".split(","))
sent.extend("sd2,gd2".split(","))
print sent
