class Character:
    def __init__(self, name, health, position):
        self.__name = name
        self.__health = health
        self.__position = position
        self.__vehicle = None

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

C1 = Character("Megamind", 100, (3, 0))
C2 = Character("Batman", 100, (5, 1))
C3 = Character("Miles Morales", 200, (7,4))

# Character moves and attacks
C1.move((5, 5))
C2.move((6,2))
# #C1.attack()
# C2.move((6,0))
# C2.attack(C1)
# C2.condition("Alive and well")
# C1.move((6,0))
# C2.attack(C1)
# C1.condition("Injured")
C3.use_vehicle("Bike",(10,1))
