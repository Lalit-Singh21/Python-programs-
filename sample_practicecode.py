'''import random
l_nums = []

def add_randomnumber(name):
    l_nums.append(name)

for i in range(20):
    add_randomnumber((random.sample(range(45), 6)))

for i in l_nums:
    print(i)'''
##########################
'''
friends = []
#x = 5
def add_friends():
    friends.append("rolf")
    #x = x+ 5 # this is an error as x is global and referenced before assignment
    # x = 5 is legal in local scope
for i in range(3):
    add_friends()
print(friends)'''

###named or keyword argument arguments and positional argument
def add_friend(name, age):
    print(f"name:{name}, age:{age}")
# add_friend("bob", age=10) #positional arguments go first
# add_friend(age=10, name="bob")

#default parameters-----------------------------
###############################
default_y=5
def addnum(x, y=default_y):# default parameters go after all required parameters
    print(x+y)
default_y =2 # changing the variable used in the
# default parameter does not change in the function answer will be 7
# addnum(2)

#lambda, without return keyword
add= lambda x,y:x+y
# can be written a (lambda x,y:x+y)(5,7) calling the same function with arguments 5,7
#print(add(5,7))
#print((lambda x,y:x+y)(4,5))

#map-----------------------------------------
'''def double(x):
    return x*2
seq = [1, 3, 5, 9]
doubled = [x*2 for x in seq]        #using list comprehension
print(doubled)
doubled = [double(x) for x in seq]     #using list comprehension is faster
print(doubled)
doubled = [(lambda x:x*2)(x) for x in seq] # using lambda
print(doubled)
doubled = map(double, seq)    #using map
print(list(doubled))
doubled = list(map(lambda x:x*2, seq)) #using lambda in map
print(doubled)'''

#dictionary comprehension
def user_auth():
    users = [
        (0, "Bob", "password"),
        (0, "Rolf", "rolf123"),
        (0, "Jose", "longpassword"),
        (0, "Username", "1234"),
    ]
    user_map = {user[1]: user for user in users}
    # print(user_map)
    # print(user_map["Bob"])
    input_username = input("enter username:")
    input_password = input("enter password")
    #unpacking
    _, usrname, passwd = user_map[input_username]
    if input_password == passwd:
        print("details correct")
    else:
        print("details incorrect")

# user_auth()


#passing arguments from list to function
def add(x, y):
    return x + y
nums = [3, 5]
#for positional argument, calling with *args unpacks the variables from a tuple/list
#print("positional arguments: ", add(*nums))
#for named arguments
nums = {"x": 15, "y": 25}
# print(add(nums["x"], nums["y"])) # ugly to read
#print(add(x = nums["x"], y = nums["y"]))# can be replaced by ** nums
# print("dictionary named arguments: ", add(**nums))

def sum_nums(args):
    print(f"args in sum: {sum()}")
    total = 0
    for arg in args:
        #print(f"sum_nums: {arg}")
        total = total+arg
    return f"sum result {total}"

# unpacking arguments: *args collects variables in a tuple
def multiply(*args):
    print(f"args in multiply: {args}")
    total = 1
    for arg in args:
        total = total*arg
    return f"multiply result {total}"

#print(multiply(1, 2, 3, 4, 5))
def apply(*args, operator):
    print(f"args in apply: {args}")
    if operator == "*":
        return multiply(*args) # unpack the values of tuple
    elif operator == "+":
        return sum_nums(args)
    else:
        return "no valid operator"

#print(apply(1,2,3,4, operator="*"))

## unpacking keyword arguments
def named(**kwargs):
    print(kwargs)
    print(f"named kwargs: {kwargs['name']} {kwargs['age']}")

#named(name="bob", age="25") #works for keyword arguments **kwargs
details = {"name": "bob", "age": 25}
named(**details)
def named1(name, age):
    print(name, age)

# named1(name="bob", age=25)
#passing only details will collect only in name
named1(**details) #unpack the dict
# *args and **kwargs can be used together
#get all the positional arguments in *args and positional arguments into **kwargs
def print_nicely(*args, **kwargs):
    named(**kwargs)
    print(args)
    print(kwargs)
    for arg,value in kwargs.items():
        print(f"print nicely:: {arg}: {value}")

print_nicely(1,2,3, name="bob", age=25)
print_nicely(1, 2, **details)


