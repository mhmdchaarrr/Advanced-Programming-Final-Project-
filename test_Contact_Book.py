import os
import pytest
from contact import Contact
from contactbook import ExtendedContactBook

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "contacts.txt"

def test_add_and_list_contact(temp_file):
    book = ExtendedContactBook(filename=str(temp_file), user_name="TestUser")
    contact = Contact("John", "1234567890", "john@example.com")
    book.add_contact(contact)

    contacts = book.list_contacts()
    assert len(contacts) == 1
    assert contacts[0].name == "John"

def test_edit_contact(temp_file):
    book = ExtendedContactBook(filename=str(temp_file), user_name="TestUser")
    book.add_contact(Contact("Jane", "1112223333", "jane@x.com"))

    book.edit_contact("Jane", new_phone="9999999999")
    edited = book.search_contacts("Jane")[0]
    assert edited.phone == "9999999999"

def test_delete_contact(temp_file):
    book = ExtendedContactBook(filename=str(temp_file), user_name="TestUser")
    book.add_contact(Contact("Jake", "2223334444", "jake@x.com"))

    deleted = book.delete_contact("Jake")
    assert deleted
    assert len(book.search_contacts("Jake")) == 0
