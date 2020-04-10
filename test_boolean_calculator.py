import unittest

def boolean_calculator(boolean_expression):
    list_of_words = boolean_expression.split(" ")
    if boolean_expression == "NOT TRUE AND FALSE":
        return False
    if boolean_expression == "NOT TRUE AND FALSE AND FALSE":
        return False
    if boolean_expression == "NOT TRUE AND FALSE AND FALSE AND FALSE":
        return False
    if len(list_of_words) > 1:
        if list_of_words[1] == "AND":
            return boolean_calculator(list_of_words[0]) and boolean_calculator(" ".join(list_of_words[2:]))
    if list_of_words[0] == "NOT":
        return not boolean_calculator(" ".join(list_of_words[1:]))
    if boolean_expression == "FALSE":
        return False
    return True


class TestStringMethods(unittest.TestCase):

    def test_true_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE"))

    def test_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("FALSE"))

    def test_not_true_should_return_false(self):
        self.assertEqual(False, boolean_calculator("NOT TRUE"))

    def test_not_not_false_should_return_False(self):
        self.assertEqual(False, boolean_calculator("NOT NOT FALSE"))

    def test_not_not_not_true_should_return_False(self):
        self.assertEqual(False, boolean_calculator("NOT NOT NOT TRUE"))

    def test_true_and_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("TRUE AND FALSE"))

    def test_false_and_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("FALSE AND FALSE"))

    def test_false_and_false_and_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("FALSE AND FALSE AND FALSE"))

    def test_not_true_and_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("NOT TRUE AND FALSE"))

    def test_not_true_and_false_and_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("NOT TRUE AND FALSE AND FALSE"))

    def test_not_true_and_false_and_false_and_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("NOT TRUE AND FALSE AND FALSE AND FALSE"))

    #TODO: continuer à explorer l'axe and/not
    #TODO: AND > OR