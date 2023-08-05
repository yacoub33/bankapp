from customer import Customer

class Bank:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)