from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, ID,passportNumber):
        self._name = name
        self._ID = ID
        self._passportNumber = passportNumber

@property
def passportNumber(self):
    return self._passportNumber

@abstractmethod
def validate_passportNumber(self):
    pass
@abstractmethod
def bookFlight(self):
    pass

class Passenger(Person):
    def __init__(self,name,ID,passportNumber,ticketNumber):
        super().__init__(name,ID,passportNumber)
        self._ticketNumber=ticketNumber

    def validate_passportNumber(self):
        max_length=9
        if len(self._passportNumber) != max_length:
            raise ValueError(f"Passport number must have {max_length} characters")
        else:
            print("Proceed to book flight")

    def bookFlight(self):
        if validate_passportNumber():
            print(f"{self._name} has received ticket {self._ticketNumber}")



