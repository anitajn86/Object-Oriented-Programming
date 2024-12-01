class Customer:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

class Account:
    def __init__(self,account_number,balance,account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited UGX {amount} to checking account {self.account_number}. New balance: UGX {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew UGX {amount} from checking account {self.account_number}. New balance: UGX {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance")







