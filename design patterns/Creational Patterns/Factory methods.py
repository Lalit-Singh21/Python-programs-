# Design patterns Factory method  when user don't know what type of objects you will be needing
# or what class to be used at run time
# factory incapsulates object creation, specializing in creating other objects
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"
     
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

# factory method:
def get_pet(pet = "dog"):
	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
	return pets[pet]

d = get_pet("dog")
print(d.speak())
c = get_pet("cat")
print(c.speak())

