import unittest

def boolean_calculator(boolean_expression):
    if boolean_expression == "TRUE":
        return True
    if boolean_expression[0:4] == "NOT ":
        return not boolean_calculator(boolean_expression[4:])

    return False

class TestStringMethods(unittest.TestCase):

    def test_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE"))

    def test_should_return_false(self):
        self.assertEqual(False, boolean_calculator("FALSE"))

    def test_not_true_should_return_false(self):
        self.assertEqual(False, boolean_calculator("NOT TRUE"))

    def test_not_false_should_return_true(self):
        self.assertEqual(True, boolean_calculator("NOT FALSE"))

    def test_not_not_true_should_return_true(self):
        self.assertEqual(True, boolean_calculator("NOT NOT TRUE"))

    def test_not_not_not_false_should_return_true(self):
        self.assertEqual(True, boolean_calculator("NOT NOT NOT FALSE"))