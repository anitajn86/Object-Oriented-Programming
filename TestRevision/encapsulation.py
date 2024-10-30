#encapsulation
class Payment:
    def __init__(self,price):
        self.__final_price=price+price*0.05
    #the private method is only for the class
    def get_final_price(self):
        return self.__final_price
    
    def set_final_price(self,discount):
        self.discount=discount
        return self.__final_price*(discount/100)
    

book=Payment(10)
#book.__final_price=0
book.set_final_price(15)
print(book.get_final_price())



