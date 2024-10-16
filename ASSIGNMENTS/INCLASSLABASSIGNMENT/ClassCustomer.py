class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def toString(self):
        return f"Customer Name: {self.name}\nCustomer Address: {self.address}"
    
cu1 = Customer("Anita", "Mukono")
print(cu1.toString())

