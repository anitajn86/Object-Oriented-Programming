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