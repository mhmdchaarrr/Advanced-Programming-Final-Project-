# 📇 Advanced Programming Project

This repository contains our **Advanced Programming Project** — a **terminal-based contact management system in Python** that uses a simple text file (`contacts.txt`) to persist data. The application supports adding, editing, deleting, searching, and listing contacts with a user-friendly, colorful interface using ANSI color codes.

---

## ✨ Features

- 📂 **File-based storage** using `contacts.txt`
- ➕ Add new contacts
- ✏️ Edit existing contacts
- ❌ Delete contacts
- 🔍 Search contacts by name
- 📋 List all contacts with color formatting
- 🎨 Colored output using decorators and ANSI escape codes
- 🔗 Merge contacts from multiple files through an external contact book

---

📦 Project Root
- Contact_book_file_based.py # Main script
- Contacts.txt # Auto-created upon first run

---

# ⚙️ Functionality

- Contacts are saved in the format: `Name, Phone number, Email`
- Basic input validation:
  - ✅ Phone number must contain at least **10 digits**
  - ✅ Email must include the `@` symbol

---

## 📋 Output Menu

Upon running the program, users are presented with the following menu options:

1. **List Contacts** – Display all saved contacts
2. **Add Contact** – Add a new contact (name, phone, email)
3. **Edit Contact** – Modify the phone or email of an existing contact
4. **Delete Contact** – Remove a contact by name
5. **Search Contact** – Search and display contacts by name
6. **Exit** – Close the application

---

## 📝 Notes

- The application runs in the terminal/console.
- All changes are saved in `contacts.txt`.
---
