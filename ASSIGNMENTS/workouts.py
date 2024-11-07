class Character:
    def __init__(self, name, health, position):
        self._name = name
        self._health = health
        self._position = position

    def get_name(self):
        return self._name

    def move(self, new_position):
        self._position = new_position
        print(f"{self._name} moves to position {self._position}")

    def attack(self,target):
        if self._position==target._position:
            print(f"{self._name} attacks {target.get_name()}")
        else:
            print(f"{target.get_name()} is too far.")

    def condition(self,new_healthStatus):
        self.__health=new_healthStatus
        print(f"{self._name} is {self.__health}")

    #adding a method in the character class to extend its functionality
    def use_vehicle(self, vehicle, destination):
        #Character boards a vehicle and drives to destination 
        #abstraction is used to hide the complexity within the use_vehicle function
        if vehicle:
            self.__vehicle = vehicle
            print(f"{self._name} boards the {self.__vehicle}")
            self.__vehicle.drive(destination)
            self.__position = destination
            print(f"{self._name} arrives at position {self.__position} in the {self.__vehicle}.")
            self.__vehicle = None
        else:
            print(f"{self._name} is already using a vehicle.")


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

    def __str__(self):
        return self.__type

C1 = Character("Megamind", 100, (3, 0))
C2 = Character("Batman", 100, (5, 1))
C3 = Character("Miles Morales", 200, (7,4))

V1= Vehicle("Bike",100, 20)
V2= Vehicle("Bentley Mulsanne",240,90)

C3.use_vehicle( V1,(10,1))

#Special characters inheriting from the character class
class UltimateHero(Character):
    def __init__(self, name, health, position, wings=False):
        super().__init__(name, health, position)
        self._wings=wings
        
    def double_jump(self):
        print(f"{self.get_name()} performs a double jump.")

    def fast_run(self):
        print(f"{self.get_name()} runs fast. ")

    def move(self, new_position): #polymorphism using method overriding.
        if not self._wings:
            self._position = new_position
            print(f"{self._name} flies to position {self._position}")
        else:
            super().move(new_position) #this now calls the original move method.

Hero1= UltimateHero("Black widow","Good health",(1,1),False)
Hero2= UltimateHero("White Tiger","Good health",(1,5),True)
print(Hero1.get_name())
print(Hero2.get_name())

# Hero1.fast_run()
# Hero1.double_jump()
# Hero2.move((1,1))
# Hero2.attack(Hero1)
# Hero1.condition("Injured")
# Hero2.use_vehicle(V2,(10,9))

Hero1.move((2,1))
Hero2.move((6,7))
#C3.attack(Hero2)

# #A simple game scenario
# print("Our heroes are gearing to fight against a villain")
# print("Viggo Grimborn is wreaking havoc in the city of Badtown. Professor X and his apprentice are working together to defeat him.")
# Hero3=UltimateHero("Professor X","Disabled",(7,7))
# Hero4=Character("Mystique","Healthy",(5,5))
# Villain1=Character("Viggo Grimborn","Healthy",(11,2))

# V3=Vehicle("Batmobile",240,150)

# print("Professor X and Mystique locate Viggo and use the batmobile to reach him")
# Hero3.use_vehicle(V3,(11,0))
# Hero4.use_vehicle(V3,(11,0))

# Hero4.move((11,2))
# Hero3.move((11,2))
# print("Our heroes reach the villain and attack")
# Hero3.attack(Villain1)
# Hero4.attack(Villain1)

# Villain1.condition("Dead")
# print("The vilain is now dead. Our heroes are victorious")



