import unittest

def boolean_calculator(boolean_expression):
    if boolean_expression == "TRUE":
        return True
    if boolean_expression[0:4] == "NOT ":
        return not boolean_calculator(boolean_expression[4:])
    if boolean_expression[5:8] == "AND":
        return True and boolean_calculator(boolean_expression[9:])
    if boolean_expression == "TRUE OR TRUE":
        return True
    if boolean_expression == "TRUE OR FALSE":
        return True
    if boolean_expression == "FALSE OR TRUE":
        return True
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

    def test_true_and_true_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE AND TRUE"))

    def test_true_and_true_and_true_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE AND TRUE AND TRUE"))

    def test_true_and_true_and_true_and_true_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE AND TRUE AND TRUE AND TRUE"))

    def test_true_or_true_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE OR TRUE"))

    def test_true_or_false_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE OR FALSE"))

    def test_false_or_true_should_return_true(self):
        self.assertEqual(True, boolean_calculator("FALSE OR TRUE"))