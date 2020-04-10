import unittest

def boolean_calculator(boolean_expression):
    list_of_terms = boolean_expression.split(" ")
    len_first_word = len(list_of_terms[0])
    first_word = list_of_terms[0]
    if boolean_expression == "TRUE":
        return True
    if len(list_of_terms) > 1:
        second_word = list_of_terms[1]
        if first_word == "NOT":
            return not boolean_calculator(" ".join(list_of_terms[1:]))
        rest_boolean_expression = " ".join(list_of_terms[2:])
        if first_word == "TRUE" and second_word == "AND":
            return True and boolean_calculator(rest_boolean_expression)
        if first_word == "TRUE" and second_word == "OR":
            return True or boolean_calculator(rest_boolean_expression)
        if first_word == "FALSE" and second_word == "OR":
            return False or boolean_calculator(rest_boolean_expression)
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

    def test_true_or_true_or_true_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE OR TRUE OR TRUE"))

    def test_x(self):
        self.assertEqual(True, boolean_calculator("FALSE OR TRUE"))


    #TODO: continuer à explorer l'axe and/not
    #TODO: AND > OR