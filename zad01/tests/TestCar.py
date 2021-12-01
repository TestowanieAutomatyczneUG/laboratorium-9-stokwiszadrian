from src.Car import *
from unittest.mock import *
from unittest import TestCase, main


class test_Car(TestCase):
    @patch.object(Car, 'needsFuel')
    def test_needsfuel(self, mock_method):
        mock_method.return_value = False

        self.assertFalse(mock_method())

    @patch.object(Car, 'getEngineTemperature')
    def test_getenginetemperature(self, mock_method):
        mock_method.return_value = 95

        self.assertEqual(95, mock_method())

    @patch.object(Car, 'driveTo')
    def test_driveto(self, mock_method):
        pass


if __name__ == '__main__':
    main()