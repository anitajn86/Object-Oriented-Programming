from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, ID, passportNumber):
        self._name = name
        self._ID = ID
        self._passportNumber = passportNumber

    @property
    def passportNumber(self):
        return self._passportNumber

    @abstractmethod
    def validate_passportNumber(self,passportNumber):
        pass
    @abstractmethod
    def bookFlight(self,ticketNumber):
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
        if self.validate_passportNumber():
            print(f"{self._name} has received {self._ticketNumber} ticket")
        else:
            print("Please enter a proper passport number")     


class Crew(Person):
    def __init__(self,name,ID,passportNumber,staffPosition):
        super().__init__(name,ID,passportNumber)
        self._staffPosition = staffPosition

    def update_staff_position(self,newPosition):
        self._staffPosition = newPosition
        print(f"{self._name} has updated their staff position to {self._staffPosition}")

    def get_staffPosition(self):
        return self._staffPosition

class Flight:
    def __init__(self,flight_id,aircraft,no_passengers=0):
        self._flight_id=flight_id
        self._aircraft=aircraft
        self._no_passengers=no_passengers

    def update_no_passengers(self,passenger):
        if not isinstance(passenger,Passenger):
            raise ValueError("Passenger must be an instance of the passenger class")
        else:
            self._no_passengers+=1
            print(f"{self._flight_id} has {self._no_passengers}")


     
    
    
          







