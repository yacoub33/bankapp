# account.py
from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now()
        self.status = "Pending"

    def complete_transaction(self):
        self.status = "Completed"

class Account:
    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        
        transaction = Transaction("Withdrawal", amount)
        self.add_transaction(transaction)
        transaction.complete_transaction()

        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        transaction = Transaction("Deposit", amount)
        self.add_transaction(transaction)
        transaction.complete_transaction()

        self.balance += amount
