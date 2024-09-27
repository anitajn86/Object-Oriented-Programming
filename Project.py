from BanksAccount import *
Dave=BankAccount(1000,"Dave")
Alexa=BankAccount(12000,"Alexa")
Sarah=BankAccount(1000,"Sarah")

Dave.getBalance()
Alexa.getBalance()
Sarah.getBalance()

Sarah.deposit(4000)
Dave.withdraw(2000)
Alexa.withdraw(10000)

Dave.transfer(5000,"Alexa")
Alexa.transfer(5000,"Dave")
Sarah.transfer(4000,Dave)

#an error i encountered when i used a string "Dave"
#The error you're encountering occurs because the variable account, which is passed as a string 
# (likely "Dave" in this case), is treated like a bank account object that has a deposit() method.
#  Since strings don't have a deposit() method, Python raises an AttributeError.

#Issue:
#You're trying to call account.deposit(amount) on a string instead of an instance of a class
#  that has a deposit() method, which causes the error.

#Suggested Fix:
#You need to pass an actual account object (e.g., Dave, an instance of the BankAccount class or similar)
#  instead of the string "Dave"