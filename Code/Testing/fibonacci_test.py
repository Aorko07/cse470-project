import unittest
import fibonacci


class FibonacciTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fibonacci.fibonacci(10), 88)


if __name__ == '__main__':
    unittest.main()
