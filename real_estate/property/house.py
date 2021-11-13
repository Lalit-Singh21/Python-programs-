from property import Property

class House(Property):
    valid_fenced = ("yes", "no")
    valid_garage = ("attached", "detached", "none")

    #positional default arguments are resolved and rest of the arguments
    #are contained in **kwargs
    #passed **kwargs = {'square_feet': '1243', 'beds': '2', 'baths': '1', 'fenced': 'yes', 'garage': 'none', 'num_stories': '2'}
    #printed kwargs in function: {'square_feet': '1243', 'beds': '2', 'baths': '1'}
    def __init__(self, num_stories="", garage='', fenced='', **kwargs):
        #print(f"kwargs == {kwargs}")
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("House Information")
        print("**********************")
        print(f"num of stories: {self.num_stories}")
        print(f"Fenced: {self.fenced}")
        print(f"Has garage: {self.garage}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        num_stories = input("How many stories?:")
        garage = Property.get_valid_input("What garage does the property have?: ", House.valid_garage)
        fenced = Property.get_valid_input("Does the property have a fence?: ", House.valid_fenced)
        parent_init.update({'fenced': fenced, 'garage': garage, 'num_stories': num_stories})
        return parent_init


if __name__ == '__main__':
    init = House.prompt_init()
    house = House(**init)
    house.display()
