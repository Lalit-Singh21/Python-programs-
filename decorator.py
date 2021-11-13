user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"


# unsecured
# print(get_admin_password())

# will require if statement everywhere admins password is used so not useful
# def secure_admin_password():
#     if user["access_level"] == "admin":
#         return "1234"
#
# print(secure_admin_password())

# other option
'''
def secure_function(func):
    if user["access_level"] == "admin":
        return func

# it checks access level at the definition and not at the call so its not optimal solution
get_admin_password = secure_function(get_admin_password)
print(get_admin_password())'''
import functools as fun


def make_secure(func):
    @fun.wraps(func)  # now doesn't show the wrapper function when function is printed
    def secure_function(*args, **kwargs):  # or wrapper function
        if user["access_level"] == "admin":
            # func(*args, **kwargs)
            return func(*args, **kwargs)
        else:
            print("No admin user access")

    return secure_function


get_admin_password = make_secure(get_admin_password)
user = {"username": "jose", "access_level": "admin"}
print(get_admin_password())
print("get admin password", get_admin_password.__name__)

@make_secure
def get_panel_password(*args, t=1):
    if args[0] == "admin":
        return "1234"
    if args[0] == "billing":
        return "super_secure_billing_password"

print("test with argument in wrapper")
print(get_panel_password("billing", 1, 2, 3))


# function passed as arguments example, without parenthesis it is a reference and can be used later
# with brackets it is simple call to the function
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child()


first = parent(1)
second = parent(2)
print(first())
print(second)


# understanding decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

#if @ decorator is not written
#say_whee = my_decorator(say_whee)
print("---------------------------------------")
print(say_whee)
say_whee()
#--------------------------------------

#decorators with parameters will require another top function over decorator called factory method

def make_secure(access_level):
    def decorator(func):
        @fun.wraps(func)  # now doesn't show the wrapper function when function is printed
        def secure_function(*args, **kwargs):  # or wrapper function
            if user["access_level"] == access_level:
                # func(*args, **kwargs)
                return func(*args, **kwargs)
            else:
                print("No admin user access")

        return secure_function
    return decorator

@make_secure("user")
def get_user_password():
    return "userpassword"
print("$$$$$$$$$")
user = {"username": "jose", "access_level": "user"}
print(get_user_password())

