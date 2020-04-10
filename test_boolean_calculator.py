import unittest

SEPARATOR = " "

def find_inner_parenthese(boolean_string):
    i = len(boolean_string)-1
    while i >= 0:
        if boolean_string[i] == "(":
            j = i+1
            last_open_parenthese = i
            while j < len(boolean_string):
                if boolean_string[j] == ")":
                    first_closing_parenthese = j
                    break
                j += 1
            return (last_open_parenthese, first_closing_parenthese)
        i -= 1
    return (None, None)

def word_position(word_list, word):
    for i in range(len(word_list)):
        if word_list[i] == word:
            return i
    return None

def get_left_part_boolean_expression_of_word_position(list_of_words, word_position):
    return SEPARATOR.join(list_of_words[0:word_position])


def get_right_part_boolean_expression_of_word_position(list_of_words, word_position):
    return SEPARATOR.join(list_of_words[word_position+1:])

def boolean_to_string(boolean_value):
    if boolean_value:
        return "TRUE"
    return "FALSE"

def get_inner_expression(boolean_expression):
    last_open_parenthese, first_closing_parenthese = find_inner_parenthese(boolean_expression)
    if first_closing_parenthese is not None:
        inner_string = boolean_expression[last_open_parenthese+1:first_closing_parenthese]
        return inner_string
    return "undefined"

def get_left_part_of_expression(boolean_string):
    last_open_parenthese, first_closing_parenthese = find_inner_parenthese(boolean_string)
    if first_closing_parenthese is not None:
        return boolean_string[:last_open_parenthese]
    return "undefined"

def get_right_part_of_expression(boolean_string):
    last_open_parenthese, first_closing_parenthese = find_inner_parenthese(boolean_string)
    if first_closing_parenthese is not None:
        return boolean_string[first_closing_parenthese+1:]
    return "undefined"

def boolean_calculator(boolean_expression):
    # last_open_parenthese, first_closing_parenthese = find_inner_parenthese(boolean_expression)
    # if first_closing_parenthese is not None:
    #     inner_string = boolean_expression[last_open_parenthese+1:first_closing_parenthese]
    #     boolean_value_inner_expression = boolean_calculator(inner_string)
    #     string_result_inner_expression = boolean_to_string(boolean_value_inner_expression)
    #     left_of_expression = get_left_part_of_expression(boolean_expression)
    #     right_of_expression = boolean_expression[first_closing_parenthese+1:]
    #     return boolean_calculator(left_of_expression + string_result_inner_expression + right_of_expression)

    inner_string = get_inner_expression(boolean_expression)
    if inner_string != "undefined":
        boolean_value_inner_expression = boolean_calculator(inner_string)
        string_result_inner_expression = boolean_to_string(boolean_value_inner_expression)
        left_of_expression = get_left_part_of_expression(boolean_expression)
        right_of_expression = get_right_part_of_expression(boolean_expression)
        return boolean_calculator(left_of_expression + string_result_inner_expression + right_of_expression)

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

    def test_simple_parenthesis_expression_should_return_true(self):
        self.assertEqual(True, boolean_calculator("(TRUE)"))

    def test_first_parenthese_position_should_be_0(self):
        first, last = find_inner_parenthese("(TRUE)")
        self.assertEqual(0, first)

    def test_first_parenthese_position_should_be_None(self):
        first, last = find_inner_parenthese("TRUE")
        self.assertTrue(last is None)

    def test_inner_expression_should_be_true(self):
        self.assertEqual("TRUE", get_inner_expression("(TRUE)"))

    def test_inner_expression_should_be_undefined(self):
        self.assertEqual("undefined", get_inner_expression("TRUE"))

    def test_left_part_should_be_empty_for_simple_expression(self):
        self.assertEqual("", get_left_part_of_expression("(TRUE)"))

    def test_right_part_should_be_empty_for_simple_expression(self):
        self.assertEqual("", get_right_part_of_expression("(TRUE)"))

    def test_more_complex_parenthesis_expression_should_return_true(self):
        self.assertEqual(True, boolean_calculator("(TRUE OR FALSE)"))

    #TODO: continuer à explorer l'axe and/not
    #TODO: AND > OR