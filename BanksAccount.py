class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance=initialAmount
        self.name=acctName
        print(f"\nAccount {self.name} created.\nBalance=${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount {self.name} balance=${self.balance:.2f}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        #print(f"\nDeposit complete.\nAccount {self.name} balance=${self.balance:.2f}")  
        #the above line can also work instead of the two below
        print("\nDeposit complete.")
        self.getBalance()
    
    def viableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\nSorry,account {self.name} only has a balance of ${self.balance:.2f}")
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted.\n{error}")