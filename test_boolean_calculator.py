import unittest

SEPARATOR = " "


def word_position(word_list, word):
    for i in range(len(word_list)):
        if word_list[i] == word:
            return i
    return None


def get_left_part_boolean_expression_of_word_position(list_of_words, word_position):
    return SEPARATOR.join(list_of_words[0:word_position])


def get_right_part_boolean_expression_of_word_position(list_of_words, word_position):
    return SEPARATOR.join(list_of_words[word_position+1:])


def boolean_calculator(boolean_expression):
    if
    if boolean_expression[0] == '(':
        bo

    list_of_words = boolean_expression.split(SEPARATOR)
    position_or = word_position(list_of_words, "OR")
    position_and = word_position(list_of_words, "AND")
    if position_or:
        return boolean_calculator(get_left_part_boolean_expression_of_word_position(list_of_words, position_or)) \
               or boolean_calculator(get_right_part_boolean_expression_of_word_position(list_of_words, position_or))
    if position_and:
        return boolean_calculator(get_left_part_boolean_expression_of_word_position(list_of_words, position_and)) \
               and boolean_calculator(get_right_part_boolean_expression_of_word_position(list_of_words, position_and))
    if list_of_words[0] == "NOT":
        return not boolean_calculator(SEPARATOR.join(list_of_words[1:]))
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

    def test_false_or_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("FALSE OR FALSE"))

    def test_false_or_false_or_false_should_return_false(self):
        self.assertEqual(False, boolean_calculator("FALSE OR FALSE OR FALSE"))

    def test_x(self):
        self.assertEqual(False, boolean_calculator("(TRUE OR FALSE)"))


    #TODO: continuer à explorer l'axe and/not
    #TODO: AND > OR