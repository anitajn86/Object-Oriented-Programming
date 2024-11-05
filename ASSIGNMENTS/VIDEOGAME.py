# Character class with encapsulation
class Character:
    def __init__(self, name, health, position):
        self._name = name
        self._health = health
        self._position = position

    def move(self, new_position):
        self._position = new_position
        print(f"{self._name} moves to position {self._position}")

    def attack(self):
        print(f"{self._name} attacks!")

    def interact(self):
        print(f"{self._name} interacts with the environment.")

# Vehicle class with encapsulation
class Vehicle:
    def __init__(self, type, speed, fuel_level):
        self._type = type
        self._speed = speed
        self._fuel_level = fuel_level

    def drive(self):
        if self._fuel_level > 0:
            print(f"The {self._type} drives at speed {self._speed}.")
            self._fuel_level -= 10
        else:
            print(f"The {self._type} is out of fuel!")

    def refuel(self):
        self._fuel_level = 100
        print(f"The {self._type} is refueled to {self._fuel_level}.")

    def stop(self):
        print(f"The {self._type} stops.")

# Extending Character class to interact with Vehicle
class CharacterWithVehicle(Character):
    def get_in(self, vehicle):
        self._vehicle = vehicle
        print(f"{self._name} gets into the {self._vehicle._type}.")

    def get_out(self):
        print(f"{self._name} gets out of the {self._vehicle._type}.")
        self._vehicle = None

# Specialized Character class using inheritance
class HeroCharacter(Character):
    def double_jump(self):
        print(f"{self._name} performs a double jump!")

    def fast_run(self):
        print(f"{self._name} runs fast!")

# Polymorphic behavior
def handle_object(obj):
    if isinstance(obj, Character):
        obj.interact()
    elif isinstance(obj, Vehicle):
        obj.drive()

# Simple game scenario
def game_scenario():
    # Create character and vehicle objects
    character = Character("Player1", 100, (0, 0))
    hero = HeroCharacter("Hero", 150, (10, 10))
    vehicle = Vehicle("Car", 60, 50)
    
    # Character moves and interacts
    character.move((5, 5))
    character.attack()
    character.interact()

    # Character interacts with vehicle
    player_with_vehicle = CharacterWithVehicle("Player2", 100, (0, 0))
    player_with_vehicle.get_in(vehicle)
    vehicle.drive()
    player_with_vehicle.get_out()

    # Hero character uses specialized abilities
    hero.double_jump()
    hero.fast_run()

    # Handling different object types with polymorphism
    handle_object(character)
    handle_object(vehicle)

# Run the game scenario
game_scenario()
