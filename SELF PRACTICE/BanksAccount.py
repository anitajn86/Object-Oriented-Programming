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

    def transfer(self,amount,account):
        try:
            print("\n***********\n\nBeginning transfer..🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!✅\n\n***********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance=self.balance+(amount*1.05)
        print("\nDeposit complete")
        self.getBalance()       
    #no initializer because there are no new properties
    #override the deposit method because any amount added to this account
    #gets an additional 5%

class SavingsAcct(InterestRewardsAcct):
    #we are going to add a new property to class so we shall use init method and then super() to
    #bring in everything from the parent class.
    def __init__(self,initialAmount,acctName):
        super().__init__(initialAmount,acctName)
        self.fee=5
    #any deposit will get a 5% deposit but since it is a savings account, any withdraw will have a fee of 5$ deducted
    #so we shall override the withdrawal method
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\nWithdraw completed")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
    
