#coding=utf-8

from collections import deque
from collections import defaultdict
from collections import OrderedDict

#list， tuple
a = []
a.append((0,'as'))
for i,j in a:
    print(i)
    print(j)


#set
c = set([1,2,3])
c.add(3)
c.remove(1)
print(c)

#list
l = [1,2,3,4,5]
print(l[1:])
print(l[-1:])

for idx,val in enumerate(l):
    print idx,val

#dict
b = dict()
b["1"] = 1
print(b.get("-1",100))

d = {"a":1, "b":2}
for key in d:
    print key,d[key]
for val in d.itervalues():
    print val
for key,val in d.iteritems():
    print key,val

#列表生成式
print range(10), range(1,10), range(1,10,2)
x1 = range(10)
x2 = [x for x in range(10)]
x3 = [x*x for x in range(10)]
x4 = [x for x in range(10) if x%2 == 0]
print x1,x2,x3,x4
y = ['A','B','C']
y1 = [x.lower() for x in y]
y2 = [i+j for i in y for j in y]
print y1, y2

#生成器：不事先生成，减少内存占用
y3 = (i+j for i in y for j in y)
print y3

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print fib(5)
for i in fib(5):
    print i

#*
def param(*val):
    a = 0
    for i in val:
        a += i
    print a

param(1,2,3,4)
param(*[1,2,3,4])

def param(**val):
    a = 0
    for key,v in val.iteritems():
        a += v
    print a

param(a=1,b=2)

#双向队列
dq = deque()
dq.append("b")
dq.appendleft("a")
print dq
dq.popleft()
print dq

#defaultdict
dict = defaultdict(lambda: None)
print dict.get("a")

#有序dict
dict = OrderedDict()
dict["a"] = 1
dict["c"] = 2
dict["b"] = 3
print dict