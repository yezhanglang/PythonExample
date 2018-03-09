import re

m = re.match(r"^\d{1,3}$","1233334")
m2 = re.match(r"\d{1,3}","1233334")
if m:
    print "m match"
elif m2:
    print "m2 match"

print m2.group(0)

rule = re.compile(r"(\d{1,3})(\d{1,3})(\d{1,3})")
if rule.match("123456"):
    print rule.match("123456").groups()