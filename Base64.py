#-*- coding:utf-8 -*-

import base64

s = base64.b64encode("dsfgfgfd的师傅的地方")
print s
print base64.b64decode(s)

s = base64.urlsafe_b64encode("dsfgfgfd的师傅的地方")
print s