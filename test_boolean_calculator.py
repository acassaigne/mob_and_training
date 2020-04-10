import unittest

def boolean_calculator(boolean_expression):
    list_of_terms = boolean_expression.split(" ")
    len_first_word = len(list_of_terms[0])
    if boolean_expression == "TRUE":
        return True
    if boolean_expression[0:len("NOT")] == "NOT":
        return not boolean_calculator(boolean_expression[len("NOT" + " "):])
    if boolean_expression[len("TRUE" + " "):len("TRUE" + " " + "AND")] == "AND":
        return True and boolean_calculator(boolean_expression[len("TRUE" + " " + "AND" + " "):])
    if boolean_expression[len("TRUE" + " "):len("TRUE" + " " + "OR")] == "OR":
        return True or boolean_calculator(boolean_expression[len("TRUE" + " " + "OR" + " "):])
    if boolean_expression[len("FALSE" + " "):len("FALSE" + " " + "OR")] == "OR":
        return False or boolean_calculator(boolean_expression[len("FALSE" + " " + "OR" + " "):])
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