from property import Property
from house import House
from apartment import Apartment

class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("**************")
        print(f"Selling Price: {self.price}")
        print(f"Estimated taxes: {self.taxes}")

    @staticmethod
    def prompt_init():
        return dict(
            price=input("what is the selling price? :"),
            taxes=input("what are the taxes? :"))

class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print("Rental Information")
        print("**************")
        print(f"Rent : {self.rent}")
        print(f"Estimated utilities : {self.utilities}")
        print(f"Furnished : {self.furnished}")

    @staticmethod
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? :"),
            utilities=input("what are the estimated utilities?: "),
            furnished=Property.get_valid_input("is the property furnished", ("yes", "no")),
        )

class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Apartment.prompt_init())
        return init

if __name__ == "__main__":
    # init = HousePurchase.prompt_init()
    # house_purchase =HousePurchase(**init)
    # house_purchase.display()

    init = HouseRental.prompt_init()
    house_rental =HouseRental(**init)
    house_rental.display()

