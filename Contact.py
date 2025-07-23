from decorators import Colors
class Contact:
    def __init__(self, name, phone, email):
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email  # Uses property setter

    def __str__(self):
        return f"{self.name},{self.phone},{self.email}"

    @classmethod
    def from_line(cls, line):
        parts = line.strip().split(",")
        if len(parts) != 3:
            raise ValueError("Invalid contact format.")
        return cls(*parts)

    @staticmethod
    def is_valid_phone(phone):
        return phone.isdigit() and len(phone) >= 10

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format.")
        self._email = value.strip()

    def colored_str(self):
        return (f"{Colors.BLUE}{self.name}{Colors.RESET}, "
                f"{Colors.RED}{self.phone}{Colors.RESET}, "
                f"{Colors.YELLOW}{self.email}{Colors.RESET}")
