#
import unittest

from src.homework.j_classes.class_a import die

class Test_Config(unittest.TestCase):
    def test_get_rolled_value(self):
        d = die()
        for _ in range(3):  # Test at least 3 rolls
            d.roll()
            value = d.get_rolled_value()
            self.assertIn(value, range(1, 7))
            self.assertIn(value, range(1, 7))
            self.assertIn(value, range(1, 7))

            