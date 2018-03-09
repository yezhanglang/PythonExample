#-*- coding:utf-8 -*-
import json

data = {
    'name': 'abc'
    ,'age': 100
}
print type(data), data

#将python对象转为字符串
str = json.dumps(data)
print type(str), str

#将字符串转为python对象
data2 = json.loads(str)
print data2['name']

#写json数据到文件
with open("data.json", "w") as f:
    json.dump(data, f)

#从文件读json数据
with open("data.json", 'r') as f:
    data3 = json.load(f)
    print data3

