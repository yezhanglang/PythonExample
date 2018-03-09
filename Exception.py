try:
    k = 10/0
    print k
except Exception, e:
    print e
    print Exception
    raise ZeroDivisionError()