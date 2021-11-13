# x = "awesome"

import random


def myfunc():
    num = random.randint(0, 9)
    print(num)
    while True:
        user_input = input("would you like to play? Y/n: ").lower()
        if user_input == "n":
            print("no problem lets play next time!")
            break
        elif user_input == "y":
            user_num = int(input("guess my number"))
            if abs(user_num - num) == 1:
                print("close by one")
            elif user_num == num:
                print("you guessed correct!")
            else:
                print("you guessed wrong!")
        else:
            print("input correct option!")


# myfunc()

def myfuncloop():
    friends = ["alpha", "beta", "gamma", "delta"]
    # creates another construct(range) to iterate
    # for i in range(len(friends)):
    #     print(f"{friends[i]} is my friend")
    for friend in friends:
        print(f"{friend} is my friend")


# myfuncloop()

def practicelist():
    friends = ["bob", "john", "sam", "david", "saurabh", "sara"]
    friendliness_s = [friend for friend in friends if friend.startswith("s")]
    print(friendliness_s)
    print([x*2 for x in friends])

#practicelist()


def practicedict():
    friend_ages = {"rolf": 24, "adam": 30, "anne": 27}
    '''print(f" original dict : {friend_ages}")
    #get a value by key
    print(f"accessing adams age: {friend_ages['adam']}")
    #adding element
    friend_ages["bob"] = 20
    print(f" adding bob to dict: {friend_ages}")
    #change value
    friend_ages["rolf"] = 20
    print(f"changing age of rolf: {friend_ages}")'''

    #list of dict
    friends = [
        {"name": "rolf", "age": 24},
        {"name": "adam", "age": 30},
        {"name": "anne", "age": 27},
    ]
    #print(friends[0]["name"])

    student_attendence = {"rolf": 96, "adam": 80, "anne": 100}
    #access key value
    # for student in student_attendence:
    #     print(f"{student} : {student_attendence[student]}")
    #better way to access keys and values
    for student, attendence in student_attendence.items():
        print(f"{student} : {attendence}")

    #in keyword
    if "adam" in student_attendence:
        print(f" adam attendence: {student_attendence['adam']}")
    else:
        print("adam not a student")

    attendence_values = student_attendence.values()
    attendence_avg = sum(attendence_values)/len(attendence_values)
    print(f"average attendence is : {attendence_avg}")


# practicedict()

def destructuringVar():
    t = 5, "abc" # or x, y = 1,2
    a, b = t
    print(t)
    print(a, b)

    student_attendence = {"rolf": 96, "adam": 80, "anne": 100}
    print(list(student_attendence.items()))

    for t in student_attendence.items():
        print(t)
    people = [("bob", 42, "mechanic"), ("james", 24, "artist"), ("harry", 32, "lecturer")]
    #destructuting helps code look readable
    # for person in people:
    #     print(f"age:{person[0]}, age: {person[1]}, profession: {person[2]}")
    for name, age, profession in people:
        print(f"name: {name} , age: {age}, profession: {profession}")

    #if you want to ignore age
    person1 = ("bob", 42, "mechanic")
    #unpack with _ variable for age (its so bad that no one uses it)
    name, _, profession = person1
    print(name, _, profession)

    # make 2 lists using * and **
    head, *tail = [1,2,3,4,5]
    print(head, tail)
    #print(head, *tail)

#destructuringVar()



