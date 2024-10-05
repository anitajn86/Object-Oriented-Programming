class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Car information: \nBrand: {self.brand} \nModel: {self.model} \nYear: {self.year} \nMileage: {self.mileage} km")
        print("-" * 30)

    def drive(self, distance):
        self.mileage += distance
        print(f"After driving {distance} km, the mileage is now {self.mileage} km")
        

car1 = Car("Rolls Royce", "Rolls Royce Phantom", 2022, 5000)
car2 = Car("Porsche", "Porsche 911", 2021, 15000)
car3 = Car("Ferrari", "Ferrari 488 GTB", 2018, 6000)

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
    def __init__(self, brand, model, year, mileage, battery_capacity, charge_level):
        super().__init__(brand, model, year, mileage)
        self.battery_capacity = battery_capacity
        self.charge_level = charge_level

    def charge(self, amount):
        print(f"Charging {amount} kW to the battery...")
        
        while self.battery_capacity < 100:
            self.battery_capacity += self.charge_level
            
            if self.battery_capacity > 100:
                self.battery_capacity = 100
            print(f"Charging... Current battery capacity is {self.battery_capacity} kW")
            
        print("Battery fully charged!")

    def display_info(self):
        super().display_info()  # Display the base car info
        print(f"Battery capacity: {self.battery_capacity} kW \nCharge level: {self.charge_level} kW")
        print("-" * 30)


electricCar1 = ElectricCar("Tesla", "Tesla Model S", 2022, 10000, 20, 20)
electricCar1.display_info()

electricCar1.charge(30)
electricCar1.display_info()


