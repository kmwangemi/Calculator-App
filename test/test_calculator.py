import unittest
from app.calculator import calculator

class TddInPythonExample(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        calc = calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_subtract_method_returns_correct_result(self):
        calc = calculator()
        result = calc.subtract(4,2)
        self.assertEqual(2, result)



if __name__ == '__main__':
    unittest.main()