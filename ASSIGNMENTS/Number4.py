def Car(brand, model, year, mileage):
    return {
        'brand': brand,
        'model': model,
        'year': year,
        'mileage': mileage
    }

def display_info(Car):
    """Display car information."""
    print(f"Car information: \nBrand: {Car['brand']} \nModel: {Car['model']} \nYear: {Car['year']} \nMileage: {Car['mileage']} km")
    print("-" * 30)

car1 = Car("Rolls Royce", "Rolls Royce Phantom", 2022, 5000)
car2 = Car("Porsche", "Porsche 911", 2021, 15000)
car3 = Car("Ferrari", "Ferrari 488 GTB", 2018, 6000)

display_info(car1)
display_info(car2)
display_info(car3)

#DIFFERENCES BETWEEN OOP AND PROCEDURAL PROGRAMMING
# Object-oriented programming (OOP) organizes code around objects that combine both data (attributes) and behavior
# (methods), while procedural programming focuses on functions that operate on separate data structures. 

# In OOP, encapsulation keeps data hidden within objects, ensuring controlled access through methods, whereas
# in procedural programming, data is accessible and modifiable by any function. 

# OOP supports inheritance, allowing new classes to inherit properties and behavior from existing ones,
# promoting code reuse and extension, which is absent in procedural programming.
#  
# Modularity in OOP is achieved through objects and classes, making it easier to maintain and scale,
# while procedural programming achieves modularity through functions but often requires more effort to extend.

# OOP also allows for higher abstraction, modeling complex systems with real-world entities, whereas procedural
# programming tends to follow a more direct, step-by-step approach. 

# OOP is more suitable for large,complex systems, while procedural programming is simpler and more 
# suited to small or medium-sized programs.

#HOW OOP PROVIDES BENEFITS LIKE MODULARITY, REUSABILITY AND MAINTAINABILITY
# OOP enhances modularity by organizing code into self-contained objects, making components easier to manage and 
# modify. 

# It promotes reusability through inheritance and polymorphism, allowing code to be reused and extended 
# without duplication. 

# Maintainability is improved by encapsulating data and behavior within objects, reducing 
# side effects and making updates more straightforward.
 
# Procedural programming lacks these structured approaches, leading to more tightly coupled code and harder
# maintenance.