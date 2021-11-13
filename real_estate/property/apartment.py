from property import Property

class Apartment(Property):
    valid_laundries = ("coin", "ensuits", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs) # imp initializing property constructor with dictionary created by prompt init
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("Apartment Information")
        print("**********************")
        print(f"Laundry: {self.laundry}")
        print(f"Has Balcony: {self.balcony}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does"
                                  f"the property have?:",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?",
                                  Apartment.valid_balconies)
        parent_init.update({'laundry': laundry, 'balcony': balcony})
        return parent_init

def get_valid_input(input_string, valid_options):
    input_string += "({})".format(','.join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

if __name__ == '__main__':
    init = Apartment.prompt_init()
    apartment = Apartment(**init)
    apartment.display()