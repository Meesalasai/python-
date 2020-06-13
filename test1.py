import unittest
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
if __name__ == '__main__':
    unittest.main()
import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([30, 30, 40]), 50.0)
        self.assertEqual(round(average([1, 2, 7]), 1), 5.0)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(30, 30, 40)
unittest.main()  # Calling from the command line invokes all tests