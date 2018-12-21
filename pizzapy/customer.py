from .address import Address

class Customer:
    """The Customer who orders a pizza."""

    def __init__(self, fname='', lname='', email='', phone=''):
        self.first_name = fname.strip()
        self.last_name = lname.strip()
        self.email = email.strip()
        self.phone = str(phone).strip()

    def __repr__(self):
        return "Name: {} {}\nEmail: {}\nPhone: {}\nAddress: {}".format(
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
            self.address,
        )

    def add_Address(self, address):
        self.address = address
