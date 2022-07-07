from winreg import ConnectRegistry


class Contact():
    list_contact = []

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        Contact.list_contact.append(self)
a = Contact()
print(a.self.list_contact)