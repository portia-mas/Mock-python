import unittest
from io import StringIO
from unittest.mock import patch
from main import add_numbers, subtract_numbers, fruitloop, fibonacci, find_max, find_min, Person

class TestMockPython(unittest.TestCase):

    # Add Numbers
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-2, 8), 6)
        self.assertEqual(add_numbers(0, 0), 0)

    # Subtract Numbers
    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(3, 5), -2)
        self.assertEqual(subtract_numbers(0, 0), 0)

    # FruitLoop
    @patch("sys.stdout", new_callable=StringIO)
    def test_fruitloop_output(self, mock_stdout):
        fruitloop(15)
        output = mock_stdout.getvalue().strip().split("\n")
        expected = [
            "1", "2", "Fruit", "4", "Loop", "Fruit", "7", "8", "Fruit", "Loop",
            "11", "Fruit", "13", "14", "FruitLoop"
        ]
        self.assertEqual(output, expected)

    # Fibonacci
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(10), 55)

    # Find Maximum
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-10, -5, -1]), -1)
        self.assertEqual(find_max([7]), 7)
        self.assertIsNone(find_max([]))

    # Find Minimum
    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([-10, -5, -1]), -10)
        self.assertEqual(find_min([7]), 7)
        self.assertIsNone(find_min([]))

    # Person Class
    def test_person_class(self):
        p = Person("Alice", 25)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 25)
        self.assertEqual(p.greet(), "Hello, my name is Alice and I am 25 years old.")

if __name__ == "__main__":
    unittest.main()
