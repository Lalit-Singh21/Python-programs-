a = []
b = a
# points to same memory location
print(id(a))
print(id(b))

a.append(35)

print(a)
print(b)
print(id(a))
print(id(b))

b.append(10)
print(a)
print(b)
print(id(a))
print(id(b))

b=[]
print(a)
print(b)
print(id(a))
print(id(b))

a=[]
b=[]
print(a)
print(b)
print(id(a))
print(id(b))

#python dosent create new location for 2 same integer variables
#but it create new location for two empty lists. int, str, float, boolean, tuples are immutable and can be
# used as default argument in function parameters
#when the value is changed a new memory location is assigned in integers

a=10
b=10
print(id(a), id(b))
a=4
print(id(a), id(b))

a="hello"
print(id(a))
a=a+" world"
print(a)
print(id(a))

