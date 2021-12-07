import Car

class CarImpl:
    def __init__(self, car: Car):
        self.car = car

    def car_needsFuel(self):
        if self.car.needsFuel():
            return "You need to refuel soon!"
        else:
            return "No need to refuel now"

    def car_getEngineTemperature(self):
        if self.car.getEngineTemperature() < 75:
            return "Engine is running too cold!"
        elif self.car.getEngineTemperature() > 100:
            return "Engine is running too hot!"
        else:
            return "Engine is running at an optimal temperature"

    def car_driveTo(self, destination):
        return f"The car is headed to {self.car.driveTo(destination)}"
