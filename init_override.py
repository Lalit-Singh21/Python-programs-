class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def __init__(self, name, email, phone=""):
        super().__init__(name, email)
        self.phone = phone

if __name__ == "__main__":
    person1 = Contact("Joe", "Joe@123.com")
    person2 = Supplier("Ken", "kenzhu@idu.com")
    person3 = Supplier("Ras", "ras@gmail.com")

    print(person2.all_contacts[0].email)