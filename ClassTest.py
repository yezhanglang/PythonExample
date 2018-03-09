#coding=utf-8

from types import MethodType

class A():
    def __init__(self):
        pass

    def setName(self, name):
        self.__name = name
        print(name)

    def getName(self):
        self.__private()

    def __private(self):
        print(self.__name)

#绑定方法
def addAge(self, age):
    self.age += age

a = A()
a.setName("hahah")
a.getName()
#a.__private()
a.age = 3
print(type(a.age))
print(isinstance(a.age, int))
print(hasattr(a,'age1'))

A.addAge = MethodType(addAge, None, A)

a.addAge(5)
print a.age

