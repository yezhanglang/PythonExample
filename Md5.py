import hashlib

md5 = hashlib.md5()
md5.update("dsfdgfd")
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update("dsfdgfd")
print sha1.hexdigest()