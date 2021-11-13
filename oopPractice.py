class Student:
    def __init__(self, name, grades):
        #set or change properties
        # self.name = "Rolf"
        self.name = name
        # self.grades = (90, 90, 93, 78, 90)
        self.grades = grades
    #student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}
    # function inside class is called method
    def average_grade(self):
        return sum(self.grades)/len(self.grades)
    #
    # print(average(student["grades"]))

# student = Student("Bob", (100, 90, 93, 78, 90)) # creating object, this will call init
# student2 = Student("Rolf", (90, 90, 93, 78, 90))
# uncomment to test
# print(student.average_grade()) # is equal to print(Student.average(student)) python internally passing this

#------------------------------------
# str and repr methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # magic method return object nice easy to read string
    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

    #unambiguous representation of and object so that you can recreate that object,
    # used for python debugger, prints only when str method is commented
    def __repr__(self):
        return f"<Person({self.name} {self.age})>"

bob = Person("Bob", 35)
#uncomment to test
# print(bob)  # same as print(bob.__repr__())

#----------------------
# @staticmethod and @classmethod

class ClassTest:
    def instance_method(self):
        print(f"called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"called class method of {cls}")

    @staticmethod
    def static_method():
        print(f"called static method")
# calling instance method
test = ClassTest() #instance of classTest
# uncomment to run
#test.instance_method()
# ClassTest.instance_method(test) # same as above

# calling class method, used as factories
# uncomment to run
# ClassTest.class_method()

#calling static method, its really not a method its a function placed
# inside of class
# uncomment to run
#ClassTest.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<repr> Book {self.name}, {self.book_type}, {self.weight}"

    @classmethod # factory method to ensure book type is of TYPE , hardcover por paperback
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight+100)

    @classmethod # factory method to ensure book type is of TYPE , hardcover por paperback
    def paperback(cls, name, page_weight):
        return cls(name, Book.TYPES[1], page_weight+100)

#print(Book.TYPES)
# uncomment to run
# book = Book("Harry Potter", "hardcover", 1500)
# print(book.name)
# print(book)

# calling factory method using class method
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
print(book)
print(light)

