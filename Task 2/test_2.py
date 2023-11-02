import unittest
from task_2 import text_stat

class TestTextStat(unittest.TestCase):
    def test_valid_file(self):
        result = text_stat('zadanie.txt')
        self.assertIsInstance(result, dict)

    def test_invalid_file(self):
        result = text_stat('invalid_file.txt')
        self.assertEqual(result['error'], 'Файл не найден')

if __name__ == '__main__':
    unittest.main()