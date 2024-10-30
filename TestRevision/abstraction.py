from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
#1=Vehicle()
#abstract classes cannot be instantiated 

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")
c1=Car()
#the child class should be able to implement all the abstract methods from the parent class.
c1.go()
c1.stop()

class MotorCycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

m1=MotorCycle()
m1.go()
m1.stop()

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")
b=Boat()
b.go()
b.stop()
#the object b1 cannot be instantiated without implementing all methods in the parent abstract class.
#we shall have to now add the stop method to the Boat class
#In conclusion
#Abstract classes can't be instantiated on their own.
#They contain abstract methods that are declared but no implementation.
#Prevents instantiation of the class itself.
#Requires children to use inherited abstract methods.
#Abstract methods are declared in abstract class but defined in the children class.
