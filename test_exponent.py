import power_of_a_number
import unittest

class Powbase(unittest.TestCase):
    def test_is_natural_number_correctly_power(self):
        self.assertEqual(power_of_a_number.returning_power_base_of_a_number(2, 2), 4)

    def test_for_a_big_number(self):
        self.assertEqual(power_of_a_number.returning_power_base_of_a_number(4566, 12),
                        82116586110675706515281619246434838196064256)

    def test_if_power_is_a_string(self):
        with self.assertRaises(TypeError):
            power_of_a_number.returning_power_base_of_a_number('power', 2)

    def if_base_is_a_characater(self):
        with self.assertRaises(TypeError):
            power_of_a_number.returning_power_base_of_a_number(6,'Foo')

    def test_is_power_of_float(self):
        with self.assertRaises(TypeError):
            power_of_a_number.returning_power_base_of_a_number(8, 0.354)

    def test_zero_is_power_and_zero_is_base(self):
        self.assertEqual(power_of_a_number.returning_power_base_of_a_number(0, 0), 1)

    def test_is_the_power_equal_zero(self):
        self.assertEqual(power_of_a_number.returning_power_base_of_a_number(56, 0), 1)

    def test_0_to_negative_raises_exception(self):
        with self.assertRaises(ZeroDivisionError):
            power_of_a_number.returning_power_base_of_a_number(0, -2)

    def test_if_power_is_less_than_zero(self):
        self.assertEqual(power_of_a_number.returning_power_base_of_a_number(4,-2),0.0625)

if __name__ == "__main__":
    unittest.main()
