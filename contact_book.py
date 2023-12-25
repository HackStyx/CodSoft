class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        print("\nContacts:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name}: {contact.phone}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        print("\nSearch results:")
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result.name}: {result.phone}")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_phone = input("Enter the new phone number: ")
                contact.phone = new_phone
                print(f"Contact updated: {contact.name}'s new phone number is {contact.phone}")
                return
        print(f"Contact not found with the name {name}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact deleted: {contact.name}")
                return
        print(f"Contact not found with the name {name}")


if __name__ == "__main__":
    contact_manager = ContactManager()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully!")

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            contact_manager.search_contact(keyword)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            contact_manager.update_contact(name)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
