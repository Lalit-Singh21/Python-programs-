class Property:
    def __init__(self, square_feet='', beds=0, baths=0, **kwargs):
        #super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        print("Property Information")
        print("*******************")
        print(f"Square footage :{self.square_feet}")
        print(f"Bedrooms: {self.beds}")
        print(f"Bathrooms: {self.baths}")

    @staticmethod
    def prompt_init():
        return dict(square_feet=input("Enter the Square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths:"))
    # if not putting decorator @ staticmethod use below
    #prompt_init = staticmethod(prompt_init)

    @staticmethod
    def get_valid_input(input_string, valid_options=""):
        input_string += "({})".format(','.join(valid_options))
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response

if __name__ == "__main__":
    init = Property.prompt_init()
    house = Property(**init)
    house.display()