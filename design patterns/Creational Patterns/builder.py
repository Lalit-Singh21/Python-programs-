class Director():
    def __init__(self, builder):
        self._builder = builder

    def construct_Car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_engine()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car

class Builder():
    #abstract builder
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class ToyotaBuilder(Builder):
    #concrete builder
    def add_model(self):
        self.car.model = "Toyota"

    def add_tyre(self):
        self.car.tyre = "Regular tyre"

    def add_engine(self):
        self.car.tyre = "Turbo Engine"

class Car():
    #product
    def __init__(self):
        self.model = None
        self.tyre = None
        self.engine = None

    def __str__(self):
        return "{}|{}|{}".format(self.model, self.tyre, self.engine)

builder = ToyotaBuilder()
director = Director(builder)

director.construct_Car()
car = director.get_car()
print(car)

