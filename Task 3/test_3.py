import unittest
from task_3 import roman_numerals_to_int

class TestPrimeNumbers(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(roman_numerals_to_int('XXI'),21)
        self.assertEqual(roman_numerals_to_int("MCMXCIV"),1994)
        self.assertEqual(roman_numerals_to_int("MMMMCMLXXXIX"),4989)

    def test_invalid_symbols(self):
        self.assertEqual(roman_numerals_to_int('SWOYO'), None)

    def test_invalid_combinations(self):
        self.assertEqual(roman_numerals_to_int('XXXXI'),None)
        self.assertEqual(roman_numerals_to_int('VV'), None)

    def test_wrong_sequence(self):
        self.assertEqual(roman_numerals_to_int('IIIV'), None)
        self.assertEqual(roman_numerals_to_int('IVIVI'), None)
        self.assertEqual(roman_numerals_to_int('IVX'), None)

if __name__ == '__main__':
    unittest.main()