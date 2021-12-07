from src.SomeEnv import SomeEnv
from src.Checker import Checker
from unittest.mock import *
from unittest import TestCase, main
from datetime import datetime

class test_Checker(TestCase):
    def test_reminder_true(self):
        env = SomeEnv()
        env.getTime = Mock(name="getTime")
        env.getTime.return_value = datetime(2021, 12, 20, 18, 20, 31)
        checker = Checker(env)
        checker.reminder("DefinitelyAFile")
        self.assertTrue(checker.wasPlayed)

    def test_reminder_false(self):
        env = SomeEnv()
        env.getTime = Mock(name="getTime")
        env.getTime.return_value = datetime(2021, 12, 20, 13, 20, 31)
        checker = Checker(env)
        checker.reminder("DefinitelyAFile")
        self.assertFalse(checker.wasPlayed)


if __name__ == '__main__':
    main()