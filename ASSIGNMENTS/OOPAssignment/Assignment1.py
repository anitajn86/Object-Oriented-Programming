class Car:
    def __init__(self,brand,model,year,mileage):
        self.brand=brand
        self.model=model
        self.year=year
        self.mileage=mileage

    def display_info(self):
        print(f"Car information: \nBrand:{self.brand} \nModel:{self.model} \nYear:{self.year} \nMileage:{self.mileage}")
        print("-"*30)

    def drive(self,distance):
        self.mileage=self.mileage+distance
        print(f"After driving {distance}km")
    
car1=Car("Roll Royce","Rolls Royce Phantom",2022,5000)
car2=Car("Porsche","Porsche 911",2021,15000)
car3=Car("Ferrari","Ferrari 488 GTB",2018,6000)
    
car1.display_info()
car2.display_info()
car3.display_info()

car1.drive(100)
car1.display_info()

car2.drive(250)
car2.display_info()

car3.drive(300)
car3.display_info()

class ElectricCar(Car):
    def __init__(self,brand,model,year,mileage,battery_capacity,charge_level):
        super().__init__(brand,model,year,mileage)
        self.battery_capacity=battery_capacity
        self.charge_level=charge_level

    def charge(self,amount):
        print(f'Charge {amount} to the car')
            
        if self.battery_capacity>100:
            self.battery_capacity=100
        print(f"Charging....Current battery capacity is {self.charge_level} kW")
    
    def display_info(self):
        super().display_info()
        print(f"Battery capacity:{self.battery_capacity}kW \n Charge level:{self.charge_level}")
        print("-" * 30)

electricCar1=ElectricCar("Tesla","Tesla Model S",2022,10000,70,20)
electricCar1.charge(20)
electricCar1.display_info()


# 3c.
# The electric car class demonstrates modularity byy extending functionality of the car class without altering
# the base class itself. 
# It demonstrates reusabilty by allowing shared functionality like the display_info function to be reused without
# redundant code.
# The electric car class enhances maintainability by isolating electric-specific changes to the ElectricCar class,
# allowing updates or modifications related to electric cars to be made without affecting the Car class or other 
# parts of the code.            
            
