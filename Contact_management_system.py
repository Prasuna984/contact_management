def load_contacts():
    contacts = {}
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, number = line.strip().split(":")
                contacts[name] = number
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for name, number in contacts.items():
            file.write(f"{name}:{number}\n")

def add_contact(contacts):
    name = input("Enter contact name: ").capitalize()
    number = input("Enter phone number: ")
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = number
        save_contacts(contacts)
        print(f"Contact '{name}' added successfully!")

def search_contact(contacts):
    name = input("Enter contact name to search: ").capitalize()
    if name in contacts:
        print(f"Found: {name} -> {contacts[name]}")
    else:
        print("Contact not found!")

def update_contact(contacts):
    name = input("Enter contact name to update: ").capitalize()
    if name in contacts:
        new_number = input("Enter new phone number: ")
        contacts[name] = new_number
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").capitalize()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available!")
    else:
        print("\n Contact List:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def main():
    contacts = load_contacts()
    while True:
        print("\n📞 Contact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            view_contacts(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
