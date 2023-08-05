from account import Account

class Customer:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact
        self.accounts =[]

    def add_account(self, account):
        self.accounts.append(account)