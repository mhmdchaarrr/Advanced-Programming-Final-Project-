# main.py
import os
from contact import Contact
from contactbook import ExtendedContactBook
from decorators import Colors

CONFIG_FILE = "user_config.txt"
name = ""

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        name = f.read().strip().lower()
else:
    while True:
        input_name = input("Enter your name: ").strip().lower()
        if input_name:
            name = input_name
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                f.write(name)
            break

def main():
    contact_file = f"{name}_contacts.txt"
    if not os.path.exists(contact_file):
        print(f"{Colors.YELLOW}📝 Creating new contact file: {contact_file}{Colors.RESET}")

    display_name = name.title()
    book = ExtendedContactBook(filename=contact_file, user_name=display_name)

    print(f"{Colors.BOLD}📘 {display_name}'s Contact Book Menu{Colors.RESET}")

    while True:
        print("\n1. List Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        print("7. Merge Contacts from File(s)")

        choice = input("Enter choice (1–7): ").strip()

        if choice == "1":
            contacts = set(book.list_contacts())
            if not contacts:
                print("No contacts found.")
            else:
                print("\n--- Contact List ---")
                for i, contact in enumerate(contacts, 1):
                    print(f"{i}. {contact.colored_str()}")

        elif choice == "2":
            name = input("Enter name: ")
            while True:
                phone = input("Enter phone: ").strip()
                if Contact.is_valid_phone(phone):
                    break
                else:
                    print(f"{Colors.RED}❌ Invalid phone number. Must be at least 10 digits.{Colors.RESET}")

            while True:
                email = input("Enter email: ").strip()
                try:
                    contact = Contact(name, phone, email)
                    break
                except ValueError as e:
                    print(f"{Colors.RED}❌ {e}. Please enter a valid email.{Colors.RESET}")

            book.add_contact(contact)
            print(f"{Colors.GREEN}✅ Contact added.{Colors.RESET}")

        elif choice == "3":
            name = input("Enter name of contact to edit: ")
            while True:
                phone = input("Enter new phone (leave blank to keep current): ").strip()
                if not phone or Contact.is_valid_phone(phone):
                    break
                else:
                    print(f"{Colors.RED}❌ Invalid phone number. Must be at least 10 digits.{Colors.RESET}")

            while True:
                email = input("Enter new email (leave blank to keep current): ").strip()
                if not email:
                    break
                try:
                    _ = Contact(name, phone or "1234567890", email)
                    break
                except ValueError as e:
                    print(f"{Colors.RED}❌ {e}. Please enter a valid email.{Colors.RESET}")

            success = book.edit_contact(name, phone or None, email or None)
            print(f"{Colors.GREEN}✅ Contact updated.{Colors.RESET}" if success else f"{Colors.RED}❌ Contact not found.{Colors.RESET}")

        elif choice == "4":
            name = input("Enter name of contact to delete: ")
            success = book.delete_contact(name)
            print(f"{Colors.GREEN}🗑️ Contact deleted.{Colors.RESET}" if success else f"{Colors.RED}❌ Contact not found.{Colors.RESET}")

        elif choice == "5":
            name = input("Enter name to search: ")
            matches = book.search_contacts(name)
            if matches:
                print("\n🔎 Search Results:")
                for c in matches:
                    print(c.colored_str())
            else:
                print(f"{Colors.RED}❌ No contacts found with that name.{Colors.RESET}")

        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break

        elif choice == "7":
            files_input = input("Enter file names to merge (space-separated): ").strip()
            filenames = [f.strip() for f in files_input.split() if f.strip()]
            if not filenames:
                print(f"{Colors.RED}❌ No files entered.{Colors.RESET}")
                continue

            try:
                book.concat_multiple_files(*filenames)
                print(f"{Colors.GREEN}✅ Successfully merged contacts from: {', '.join(filenames)}{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}❌ Failed to merge: {e}{Colors.RESET}")

        else:
            print(f"{Colors.RED}❗ Invalid option. Please enter a number from 1 to 7.{Colors.RESET}")

if __name__ == "__main__":
    main()
