from collections.abc import Container

class OddSetBag:
    # we need to define __contains__ for Oddsetbag to be subclass of Container class
    #instance of Odsetbag will be instance of container
    #instance to create odd numbers
    def __contains__(self, item):
        if not isinstance(item, int) or not item%2:
            return False
        return True
mybag = OddSetBag()
print(isinstance(mybag, Container)) #false if method name changed to __contains
print(issubclass(OddSetBag, Container))

#check contains odd numbers
print(1 in mybag)
print(2 in mybag)
print(3 in mybag)