#having many forms
#inheritance. an object can be treated of  the same type as parent class
#duck typing. object must have necessary attributes or methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius**2
    

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return self.base*self.height*0.5
    
#if you do not out inheritance from the parent class,you will have an error
#class Pizza():

class Pizza(Circle):
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping=topping
#the pizza is considered a pizza, a circle and a shape. hence polymorphism
shapes=[Circle(4),Square(3),Triangle(5,4),Pizza("Chicken",18)]


for shape in shapes:
    print(shape.area())