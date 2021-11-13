def divide(dividend, divisor) ->float:
    #print(f"divisor {divisor} dividend {dividend}")
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be zero")
    return dividend / divisor

#passing the name of the function as a value in the argument
def calculate(*values, operator):
    return operator(*values)

result = calculate(24,2, operator=divide)
print(result)

from operator import itemgetter
def search(sequence, expected, finder):
    for elem in sequence:
        print(f"search : {finder}::::{elem}")
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    return friend["name"]

#first class function use
#print(search(friends, "Rolf Smith", get_friend_name))
# or use lambda function
#print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
#itemgetter to get item from sequence, itemgetter replaced by sequence name
print(search(friends, "Rolf Smith", itemgetter("name")))