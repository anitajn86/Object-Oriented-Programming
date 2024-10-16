class Garage:
    def __init__(self):
        self.vehicle = None

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def toString(self):
        if self.vehicle:
            return f"Description of the parked vehicle ...\n{self.vehicle.toString()}"
        else:
            return "No vehicle parked in the garage."