#regular expression
import re

teststring1="a * b"
teststring2="123,456"
teststring3="123,456-222%345"

#substitution

print re.sub(r"\*",r"::",teststring1)
print re.sub(r"\d","digit",teststring2,3)

#splitting
print re.split(r",",teststring2)
print re.split(r"[+\-*/%2]+",teststring3)

#find all
string="the cat sat at the mat at ten"
print string
print re.findall(r'at',string)
print re.findall(r'\sat',string)
print re.findall(r'\Sat',string)


#extraction
teststring1="Albert Einstein, phone: 123-456, e-mail: albert@bug2bug.com"
#expression1=r"(\w+)\s+(\w+)\s*,\s*phone:\s*\d+[\-]?\d+s\*,\s*email
