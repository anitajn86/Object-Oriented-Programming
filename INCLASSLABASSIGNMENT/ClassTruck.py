from ClassVehicle import*

class Truck(Vehicle):
    def __init__(self, color, hasTrailer=False):
        super().__init__(color)
        self.hasTrailer = hasTrailer

    def toString(self):
        return super().toString() + f"\nHas trailer: {self.hasTrailer}"
    
t1=Truck(True)
print(t1.toString())