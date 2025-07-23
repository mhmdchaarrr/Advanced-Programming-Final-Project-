# contactbook.py
import os
from contact import Contact
from decorators import Colors

def contact_generator(filename):
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                yield Contact.from_line(line)

class ContactBook:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            return list(contact_generator(self.filename))
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, "w") as f:
            for contact in self.contacts:
                f.write(str(contact) + "\n")

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, name):
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        if len(self.contacts) < original_count:
            self.save_contacts()
            return True
        return False

    def edit_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                self.save_contacts()
                return True
        return False

    def list_contacts(self):
        return self.contacts

    def search_contacts(self, name):
        return [c for c in self.contacts if name.lower() in c.name.lower()]

    def __add__(self, other):
        combined = ContactBook()
        combined.contacts = self.contacts + other.contacts
        return combined

class ExtendedContactBook(ContactBook):
    def __init__(self, filename="contacts.txt", user_name=""):
        super().__init__(filename)
        self.user_name = user_name or self.extract_name_from_filename(filename)

    def extract_name_from_filename(self, filename):
        return filename.split("_")[0].title()

    def list_contacts(self):
        print(f"📘 {self.user_name}'s Contact Book Listing:")
        seen = set()
        unique_contacts = []
        for c in self.contacts:
            key = str(c)
            if key not in seen:
                seen.add(key)
                unique_contacts.append(c)
        return unique_contacts

    def concat_multiple_files(self, *filenames):
        existing_set = set(str(c) for c in self.contacts)
        added = 0
        for fname in filenames:
            for contact in contact_generator(fname):
                if str(contact) not in existing_set:
                    self.contacts.append(contact)
                    existing_set.add(str(contact))
                    added += 1
        self.save_contacts()
        print(f"{Colors.GREEN}✅ Added {added} new contact(s). Skipped duplicates.{Colors.RESET}")
