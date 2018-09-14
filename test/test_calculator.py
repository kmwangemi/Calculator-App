import unittest
from app.calculator import calculator

class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.calc = calculator()

    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.asserRaises(ValueError, self.calc.add, 'two', 'three') 

    def test_calculator_returns_error_message_if_first_arg_not_number(self):
        self.asserRaises(ValueError, self.calc.add, 'two', 2)

    def test_calculator_returns_error_message_if_second_arg_not_number(self):
        self.asserRaises(ValueError, self.calc.add, 2, 'three') 



if __name__ == '__main__':
    unittest.main()