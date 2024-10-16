from ClassTruck import*
from ClassGarage import*

class GarageTester:
    @staticmethod
    def getExample(self):
        truck = Truck("black", False)
        garage = Garage()
        garage.setVehicle(truck)
        print(garage.toString())

tester = GarageTester()
tester.getExample()