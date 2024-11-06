# Character class with encapsulation
class Character:
    def __init__(self, name, health, position):
        self.__name = name
        self.__health = health
        self.__position = position

    def move(self, new_position):
        self.__position = new_position
        print(f"{self.__name} moves to position {self.__position}")

    def attack(self,target):
        if self.__position==target.__position:
            print(f"{self.__name} attacks {target}")
        else:
            print(f"{target} is too far.")

    def condition(self,new_healthStatus):
        self.__health=new_healthStatus
        print(f"{self.__name} is {self.__health}")

    #adding a method in the character class to extend its functionality
    def use_vehicle(self, vehicle, destination):
        """Boards a vehicle, drives it to a destination, and exits upon arrival."""
        if vehicle:
            self.__vehicle = vehicle
            print(f"{self.__name} boards the {self.__vehicle}")
            self.__vehicle.drive(destination)
            self.__position = destination
            print(f"{self.__name} arrives at position {self.__position} in the {self.__vehicle}.")
            self.__vehicle = None
        else:
            print(f"{self.__name} is already using a vehicle.")

# C1 = Character("Megamind", 100, (3, 0))
# C2 = Character("Batman", 100, (5, 1))
# # Character moves and attacks
# C1.move((5, 5))
# #C1.attack()
# C2.move((6,0))
# C2.attack(C1)
# C2.condition("Alive and well")
# C1.move((6,0))
# C2.attack(C1)
# C1.condition("Injured")
C3 = Character("Miles Morales", 200, (7,4))

# Vehicle class with encapsulation
class Vehicle:
    def __init__(self, type, speed, fuel_level):
        self.__type = type
        self.__speed = speed
        self.__fuel_level = fuel_level

    def drive(self,destination):
        if self.__fuel_level > 0:
            print(f"The {self.__type} drives at speed {self.__speed} to {destination}.")
            self.__fuel_level -= 10
        else:
            print(f"The {self.__type} is out of fuel!")

    def refuel(self):
        self.__fuel_level = 100
        print(f"The {self.__type} is refueled to {self.__fuel_level}.")

    def stop(self):
        print(f"The {self.__type} stops.")

V1= Vehicle("Car", 60, 50)
V2= Vehicle("Bike", 120, 70)
V1.drive((2,1))
V1.refuel()
V1.stop()
V2.drive((6,9))
V2.refuel()
V2.stop()

C3.use_vehicle("Bike",(10,1))

#Special characters inheriting from the character class
class UltimateHero(Character):
    def double_jump(self):
        print(f"{self.__name} performs a double jump!")

    def fast_run(self):
        print(f"{self.__name} runs fast!")


# Simple game scenario
# def game_scenario():
#     # Create character and vehicle objects
#     character = Character("Player1", 100, (0, 0))
#     hero = HeroCharacter("Hero", 150, (10, 10))
#     vehicle = Vehicle("Car", 60, 50)
    
#     # Character moves and interacts
#     character.move((5, 5))
#     character.attack()
#     character.interact()

#     # Character interacts with vehicle
#     player_with_vehicle = CharacterWithVehicle("Player2", 100, (0, 0))
#     player_with_vehicle.get_in(vehicle)
#     vehicle.drive()
#     player_with_vehicle.get_out()

#     # Hero character uses specialized abilities
#     hero.double_jump()
#     hero.fast_run()

#     # Handling different object types with polymorphism
#     handle_object(character)
#     handle_object(vehicle)

# # Run the game scenario
# game_scenario()
