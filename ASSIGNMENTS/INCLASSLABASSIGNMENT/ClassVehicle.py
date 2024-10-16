class Vehicle:
    def __init__(self,color):
        self.color=color

    def getColor(self):
        return self.color
    
    def toString(self):
        return f"This vehicle is {self.color}"
    
car=Vehicle("Blue")
print(car.getColor())
print(car.toString())