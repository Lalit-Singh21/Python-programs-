
#user expectations yeilds multiple related objects, and dn't know which family it is until runtime 

#one of the objects to be returned
class Dog:
    def __str__(self):
        return "dog"

    def speak(self):
        return "Woof!"

#abstract Factory
class DogFactory:
	#return dog object
	def get_pet(self):
		return Dog()

	#returning dog food string object
	def get_food(self):
		return "dog food"

class Cat:
    def __str__(self):
        return "cat"

    def speak(self):
        return "Meow!"

#abstract Factory
class CatFactory:
	#return dog object
	def get_pet(self):
		return Cat()

	#returning dog food string object
	def get_food(self):
		return "cat food"

class PetStore:
	#houses the Abstract factory
	def __init__(self, pet_factory=None):
		self._pet_factory = pet_factory

	def show_pets(self):
		#utiilty method to display the details of the object returned by the concrete factory- DogFactory
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print(f"our pet is {pet}")
		print(f"it says hello by {pet.speak()}")
		print(f"the food is {pet_food}")

#create concrete factory
factory = DogFactory()

#create pet store housing Abstract factory
shop = PetStore(factory)

#invokes the utility method to show the details of our pet
shop.show_pets()

fc = CatFactory()
shop = PetStore(fc)
shop.show_pets()