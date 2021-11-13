class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)  # name email appended to list


class Supplier(Contact):
    def order(self, order):
        print(f"Send {order} order to {self.name}")


if __name__ == '__main__':
    friend_contact = Contact("Kwame", "Kwame@gmail.com")
    water_guy_contact = Supplier("Joseph", "purest@gmail.com")

    print(f"All Contacts: {friend_contact.all_contacts[0].name}")
    print(f"All Contacts: {friend_contact.all_contacts[1].name}")
    water_guy_contact.order("distilled water order")