from ClassVehicle import*

class Car(Vehicle):
    def __init__(self, color, winterTyres=False):
        super().__init__(color)
        self.winterTyres = winterTyres

    def toString(self):
        return super().toString() + f"\nHas winter tyres: {self.winterTyres}"
    
c1=Car(1)
print(c1.toString())