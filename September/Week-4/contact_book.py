def display_contacts(contacts):
    print("\n--- Contacts ---")

    if not contacts:
        print("No contacts found.")
        return

    for name, phone in contacts.items():
        print(f"{name}: {phone}")


contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. View contacts")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        if name == "" or phone == "":
            print("Name and phone number cannot be empty.")
        else:
            contacts[name] = phone
            print("Contact added.")

    elif choice == "2":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "3":
        display_contacts(contacts)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")