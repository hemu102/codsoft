class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)

    def view_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts to display.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact}")

    def search_contacts(self, keyword):
        if len(self.contacts) == 0:
            print("No contacts to search.")
        else:
            matched_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword.lower() in contact.phone]
            if len(matched_contacts) == 0:
                print("No matches found.")
            else:
                print("Matched Contacts:")
                for i, contact in enumerate(matched_contacts, 1):
                    print(f"{i}. {contact}")

    def update_contact(self, old_name, new_name, new_phone, new_email, new_address):
        old_contact = next((contact for contact in self.contacts if contact.name.lower() == old_name.lower()), None)
        if old_contact:
            old_contact.name = new_name
            old_contact.phone = new_phone
            old_contact.email = new_email
            old_contact.address = new_address
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]

address_book = AddressBook()

while True:
    command = input("Enter command (add/view/search/update/delete/exit): ").lower().split()

    if command[0] == "add":
        name = input(" Name: ")
        phone = input(" Phone: ")
        email = input(" Email: ")
        address = input(" Address: ")
        address_book.add_contact(name, phone, email, address)

    elif command[0] == "view":
        address_book.view_contacts()

    elif command[0] == "search":
        keyword = input(" Keyword: ")
        address_book.search_contacts(keyword)

    elif command[0] == "update":
        old_name = input(" Name: ")
        new_name = input(" New Name: ")
        new_phone = input(" New Phone: ")
        new_email = input(" New Email: ")
        new_address = input(" New Address: ")
        address_book.update_contact(old_name, new_name, new_phone, new_email, new_address)

    elif command[0] == "delete":
        name = input(" Name: ")
        address_book.delete_contact(name)

    elif command[0] == "exit":
        break

    else:
        print("Invalid command.")

print("Goodbye!")
