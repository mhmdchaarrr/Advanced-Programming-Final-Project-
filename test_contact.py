# test_contact.py
import pytest
from Contact import Contact

def test_create_valid_contact():
    c = Contact("Alice", "1234567890", "alice@example.com")
    assert c.name == "Alice"
    assert c.phone == "1234567890"
    assert c.email == "alice@example.com"

def test_invalid_email_raises_error():
    with pytest.raises(ValueError):
        Contact("Bob", "1234567890", "bobexample.com")

def test_phone_validation():
    assert Contact.is_valid_phone("0123456789")
    assert not Contact.is_valid_phone("12345")

def test_str_output():
    c = Contact("Eve", "1112223333", "eve@example.com")
    assert str(c) == "Eve,1112223333,eve@example.com"
