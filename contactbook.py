contacts = {}
def add_contact():
    Name = input("Enter name:")
    Phone = input("Enter phone number:")
    Email = input("Enter email:")
    Address = input("Enter address:")
    if Name in contacts:
        print("This contact already exists")
    else:
        contacts[Name] = Phone 
        print("Contact added successfully")


def view_contact():
    if contacts == {}:
        print("There are no contacts")
    else:
        print("Contacts list:") 
        for Name, Phone in contacts.items():
            print(Name, Phone)


def search_contact():
    Name = input("Enter name:")
    for contact in contacts:
        if contact.lower() == Name.lower():
            print("Contact found")
            print(contact,contacts[contact])
            break
        else:
            print("Contact not found")


def update_contact():
    Name = input("Enter name:")
    for contact in contacts:
        if contact==Name:
           Phone = input("Enter new phone number:")
           contacts[Name] = Phone
           print("Contact updated successfully")
           break
        else:
           print("This contact does not exist")


def delete_contact():
    Name = input("Enter name:")
    if Name in contacts:
        del contacts[Name]
        print("Contact deleted successfully")
    else:
        print("This contact does not exist")
        

while True:
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6):"))

    if choice == 1:
        add_contact()
    
    elif choice == 2:
        view_contact()

    elif choice == 3:
        search_contact()
    
    elif choice == 4:
        update_contact()
    
    elif choice == 5:
        delete_contact()
    
    elif choice == 6:
        print("Exiting Contact Book")
    
    else:
        print("Invalid choice. Please enter a valid choice.")