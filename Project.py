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
Sarah.transfer(4000,"Dave")