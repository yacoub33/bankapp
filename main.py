from bank import Bank
from customer import Customer
from account import Account, Transaction

# Create a Bank
bank = Bank("The Bank", "London")

# Create Customers
customer1 = Customer("Tim", "123 St", "tim@example.com")
customer2 = Customer("Jane", "456 St", "jane@example.com")

# Add Customers to the Bank
bank.add_customer(customer1)
bank.add_customer(customer2)

# Create Accounts for Customers
account1 = Account("123456789", "Savings", 1000)
account2 = Account("987654321", "Checking", 5000)

# Add Accounts to Customers
customer1.add_account(account1)
customer2.add_account(account2)

# Perform Withdrawal and Deposit
try:
    withdraw_amount = float(input("Enter withdrawal amount for John Doe's Savings Account: "))
    account1.withdraw(withdraw_amount)

    deposit_amount = float(input("Enter deposit amount for Jane Smith's Checking Account: "))
    account2.deposit(deposit_amount)
except ValueError as e:
    print(f"Transaction failed: {e}")

# Display Updated Account Balances
print(f"{customer1.name}'s {account1.account_type} balance: {account1.balance}")
print(f"{customer2.name}'s {account2.account_type} balance: {account2.balance}")
