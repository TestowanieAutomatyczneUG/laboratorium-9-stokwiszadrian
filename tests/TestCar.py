from src.Car import Car
from src.CarImpl import CarImpl
from unittest.mock import *
from unittest import TestCase, main


class test_Car(TestCase):
    def test_needsfuel_true(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.car_needsFuel(), "You need to refuel soon!")

    def test_needsfuel_false(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.car_needsFuel(), "No need to refuel now")

    def test_getenginetemperature_toocold(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 60
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.car_getEngineTemperature(), "Engine is running too cold!")

    def test_getenginetemperature_toohot(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 120
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.car_getEngineTemperature(), "Engine is running too hot!")

    def test_getenginetemperature_optimal(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 85
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.car_getEngineTemperature(), "Engine is running at an optimal temperature")

    def test_driveto(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        destination = "Szczecin"
        car.driveTo.return_value = destination
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.car_driveTo(destination), f"The car is headed to {destination}")


if __name__ == '__main__':
    main()