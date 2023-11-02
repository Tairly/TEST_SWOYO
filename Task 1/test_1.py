import unittest
from task_1 import prime_numbers

class TestPrimeNumbers(unittest.TestCase):
    def test_valid_range(self):
        self.assertEqual(prime_numbers(1, 10), [2, 3, 5, 7])
        self.assertEqual(prime_numbers(10, 20), [11, 13, 17, 19])

    def test_empty_range(self):
        self.assertEqual(prime_numbers(-2, 1), [])
        self.assertEqual(prime_numbers(20, 10), [])

    def test_small_range(self):
        self.assertEqual(prime_numbers(1, 1), [])
        self.assertEqual(prime_numbers(1, 2), [2])

    def test_large_range(self):
        self.assertEqual(prime_numbers(200000000, 200000100),[200000033, 200000039, 200000051, 200000069, 200000081, 200000083, 200000089, 200000093])


if __name__ == '__main__':
    unittest.main()
