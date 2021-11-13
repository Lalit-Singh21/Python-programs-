def divide(dividend, divisor) ->float:
    #print(f"divisor {divisor} dividend {dividend}")
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be zero")
    return dividend / divisor

#grades = []

students = [
    {"name": "Bob", "grades": [75,90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100,90]}
]

print("welcome to average grades program.")

try:
    #average = divide(sum(grades), len(grades))
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"name: {name}, averaged: {average}")
except ZeroDivisionError as e:
    print(f"Errror! {name} has no grades!  <{e}>")

else: # it will be called when try is executed
    print(f"__All students average calculated__")
finally:
    print("__End of students average calculation thank you!__")
