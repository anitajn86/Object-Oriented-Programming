# Part a: Character and Vehicle Classes

class Character:
    def __init__(self, name, health, position):
        self.__name = name           # Encapsulated attribute
        self.__health = health       # Encapsulated attribute
        self.__position = position   # Encapsulated attribute
    
    def move(self, new_position):
        self.__position = new_position
        print(f"{self.__name} moved to position {self.__position}.")
    
    def attack(self, target):
        print(f"{self.__name} attacks {target.__name}.")
    
    def interact(self):
        print(f"{self.__name} is interacting with the environment.")

class Vehicle:
    def __init__(self, type, speed, fuel_level):
        self.__type = type           # Encapsulated attribute
        self.__speed = speed         # Encapsulated attribute
        self.__fuel_level = fuel_level   # Encapsulated attribute
    
    def drive(self):
        if self.__fuel_level > 0:
            print(f"{self.__type} is driving at speed {self.__speed}.")
            self.__fuel_level -= 1
        else:
            print(f"{self.__type} has no fuel left to drive.")
    
    def refuel(self, amount):
        self.__fuel_level += amount
        print(f"{self.__type} refueled by {amount}. Current fuel level: {self.__fuel_level}.")
    
    def stop(self):
        print(f"{self.__type} has stopped.")

# Demonstrate the Character and Vehicle classes
char1 = Character("Player1", 100, (0, 0))
vehicle1 = Vehicle("Car", 60, 5)

char1.move((5, 10))
char1.attack(char1)  # Example attack on itself for demonstration
char1.interact()

vehicle1.drive()
vehicle1.refuel(3)
vehicle1.stop()

# Part b: Interaction Between Objects

class CharacterWithVehicle(Character):
    def get_in(self, vehicle):
        print(f"{self.__name} gets into the {vehicle.__type}.")
    
    def get_out(self, vehicle):
        print(f"{self.__name} gets out of the {vehicle.__type}.")

# Demonstrate interaction between objects
char_with_vehicle = CharacterWithVehicle("Player2", 90, (1, 1))
char_with_vehicle.get_in(vehicle1)
vehicle1.drive()
char_with_vehicle.get_out(vehicle1)
