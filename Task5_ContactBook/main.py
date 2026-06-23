import json
import os 
FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    print("\n------Add Contact------")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    print("✓ Contact added successfully.\n")

def view_contacts(contacts):
    print("\n------Contact list------")
    if not contacts:
        print("No contacts found.\n")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search_contact(contacts):
    keyword = input("\nEnter name or phone number: ").lower()
    found = False 

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found")
            print("-"*30)
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])
            print("-"*30)
            found = True
    
    if not found:
        print("No matching contact found.\n")

def update_contact(contacts):
    name = input("\nEnter contact name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nLeave blank to keep existing value.")
            new_phone = input(f"Phone ({contact['phone']}): ")
            new_email = input(f"Email ({contact['email']}): ")
            new_address = input(f"Address ({contact['address']}): ")

            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            save_contacts(contacts)
            print("✓ Contact updated successfully.\n")
            return

    print("Contact not found.\n")   


def delete_contact(contacts):
    name = input("\nEnter contact name to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("✓ Contarct deleted successfully.\n")
            return 
    print("Contact not found.\n")


def main():
    contacts = load_contacts()
    
    while True:
        print("=" * 40)
        print("        CONTACT BOOK")
        print("=" * 40)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")    
        print("=" * 40)

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank your for using Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()