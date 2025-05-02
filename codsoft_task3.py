contacts = {}

def add_contact():
    name = input("\nEnter the contact name: ").strip()
    phone = input("\nEnter phone number: ").strip()
    email = input("\nEnter the email address: ").strip()
    address = input("Enter address: ").strip()

    contacts[name.lower()] = {
        'Name' : name,
        'Phone' : phone,
        'Email' : email,
        'Address' : address
    }
    print(f"\nContact '{name}' added successfully!")

def view_contacts():
    if contacts:
        print("\n ---Contact List--- ")
        for contact in contacts.values():
            print(f"{contact['Name']} - {contact['Phone']}")
    else:
        print("\nNo contact found")

def search_contacts():
    keyword = input("\nEnter the name or phone number to search: ").strip()
    found = False
    for contact in contacts.values():
        if keyword in contact['Name'].lower() or keyword in str(contact['Phone']):
            print("\n--- Contact found ---")
            print_contact_details(contact)
            found = True
            break
    if not found:
        print("\nNo matching contact found.")


def update_contact():
    name = input("\nEnter the name of contact to update: ").strip().lower()
    if name in contacts:
        print("\nEnter new details (leave blank to keep current):")
        phone = input(f" New phone [{contacts[name]['Phone']}]: ").strip()
        email = input(f"New email [{contacts [name]['Email']}]: ").strip()
        address = input(f"New address [{contacts[name]['Address']}]: ").strip()

        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address

        print("\nContact updated successfully")

    else:
        print("\nContact not found.")

def delete_contact():
    name = input("\nEnter the name of the contact to delete: ").strip().lower()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"\nContact not found")

def print_contact_details(contact):
    print(f"Name  : {contact['Name']}")
    print(f"Phone : {contact['Phone']}")
    print(f"Email : {contact['Email']}")
    print(f"Address : {contact['Address']}")


def main_menu():
    while True:
        print("\n======= Contact Book Menu ====")
        print("1.Add contact")
        print("2.view the contact list")
        print("3.search contact")
        print("4.update the contact")
        print("5. Delete the contact")
        print("6.Exit")

        choice = input("\nEnter your choice (1-6):").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nExisting contact book .Goodbye!")
            break
        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    print("welcome to your personal conatct book!")
    main_menu()




    


