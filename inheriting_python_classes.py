class ContactList(list):
    def search(self, name):
        matching_contact = []
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)  # name email appended to list

if __name__ == '__main__':
    f1 = Contact("Kwame", "Kwame@gmail.com")
    f2 = Contact("Yaw", "Yaw@gmail.com")
    f3 = Contact("Joe", "Joe@gmail.com")
    f4 = Contact("Kwame2", "Kwame3@gmail.com")
    f5 = Contact("Kwame3", "Kwame_45@gmail.com")

    result = [f.name for f in Contact.all_contacts.search("Kwame")]
    print(result)

    result = [f.email for f in Contact.all_contacts.search("Kwame")]
    print(result)