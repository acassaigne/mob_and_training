import unittest


class Statement:

    def __init__(self, input_string):
        self.content = input_string

    def __eq__(self, other):
        return self.content == other.content

    def split_to_list_of_words(self):
        result = ListOfWords()
        if self.content == 'FALSE':
            result.append(FalseWord())
        if self.content == 'TRUE':
            result.append(TrueWord())
        return result

    def split_by_space_2(self):
        splitted_statement = SplittedStatement()
        splitted_statement.words = self.content.split(' ')
        return splitted_statement

    def split_by_space(self):
        return self.content.split(' ')

    def separate_statement_at_ith_word(self,index):
        splitted_statement = self.split_by_space_2()
        first_part_of_statement_splitted = splitted_statement.words[:index]

    def evaluate_statement(self):
        splitted = self.split_by_space()
        splitted2 = self.split_by_space_2()
        if self.content == 'TRUE':
            return True
        if self.content == 'FALSE':
            return False
        if splitted[1] == 'AND':
            first_part_statement = Statement(splitted[0])
            second_part_statement = Statement(' '.join(splitted[2:]))
            return first_part_statement.evaluate_statement() and second_part_statement.evaluate_statement()
        if len(splitted) > 2:
            if splitted[2] == 'AND':
                first_part_statement = Statement(' '.join(splitted[0:2]))
                second_part_statement = Statement(' '.join(splitted[3:]))
                return first_part_statement.evaluate_statement() and second_part_statement.evaluate_statement()
        if splitted[0] == "NOT":
            rest_of_statement = Statement(' '.join(splitted[1:]))
            return not rest_of_statement.evaluate_statement()



class ListOfWords:

    def __init__(self):
        self.words = []

    def __eq__(self, other):
        return self.words == other.words

    def __getitem__(self, item):
        return self.words[item]

    def append(self, word):
        self.words.append(word)

class SplittedStatement:

    def __init__(self):
        self.words = []

    def __getitem__(self, item):
        return self.words[item]

    def rebuild_statement(self):
        statement_content = ' '.join(self.words)
        statement = Statement(statement_content)
        return statement

    def find_first_instance_of_word(self,word):
        for index in range(self.words):
            if self.words[index] == word:
                return index
        return None


class Word:
    def __eq__(self,other):
        return type(self) == type(other)


class TrueWord(Word):
    pass


class FalseWord(Word):
    pass


class BooleanEvaluator:

    def evaluate(self, list_of_words):
        if type(list_of_words) != ListOfWords:
            raise InvalidArgument
        if list_of_words[0] == TrueWord():
            return True
        if list_of_words[0] == FalseWord():
            return False


class InvalidArgument(Exception):
    pass


class TestStringMethods(unittest.TestCase):

    def test_true_should_return_true(self):
        a_statement = Statement("TRUE")
        self.assertEqual(True, a_statement.evaluate_statement())

    def test_false_should_return_false(self):
        a_statement = Statement("FALSE")
        self.assertEqual(False, a_statement.evaluate_statement())

    def test_not_true_should_return_false(self):
        a_statement = Statement("NOT TRUE")
        self.assertEqual(False, a_statement.evaluate_statement())

    def test_not_false_should_return_true(self):
        a_statement = Statement("NOT FALSE")
        self.assertEqual(True, a_statement.evaluate_statement())

    def test_not_not_true_should_return_true(self):
        a_statement = Statement("NOT NOT TRUE")
        self.assertEqual(True, a_statement.evaluate_statement())

    def test_true_and_false_should_return_false(self):
        a_statement = Statement("TRUE AND FALSE")
        self.assertEqual(False, a_statement.evaluate_statement())

    def test_true_and_true_should_return_true(self):
        a_statement = Statement("TRUE AND TRUE")
        self.assertEqual(True, a_statement.evaluate_statement())

    def test_falsee_and_false_should_return_false(self):
        a_statement = Statement("FALSE AND FALSE")
        self.assertEqual(False, a_statement.evaluate_statement())

    def test_not_true_and_false_should_return_False(self):
        a_statement = Statement("NOT TRUE AND FALSE")
        self.assertEqual(False, a_statement.evaluate_statement())

    def test__true_and_not_true_should_return_False(self):
        a_statement = Statement("TRUE AND NOT TRUE")
        self.assertEqual(False, a_statement.evaluate_statement())

    def test_empty_statement_should_be_split_to_empty_list_of_words(self):
        a_statement = Statement('')
        a_list_of_words = ListOfWords()
        self.assertEqual(a_list_of_words, a_statement.split_to_list_of_words())

    def test_true_statement_split_to_list_should_return_good_list_of_words(self):
        a_statement = Statement('TRUE')
        expected_list_of_words = ListOfWords()
        expected_list_of_words.append(TrueWord())
        self.assertEqual(expected_list_of_words, a_statement.split_to_list_of_words())

    def test_false_statement_split_to_list_should_return_good_list_of_words(self):
        a_statement = Statement('FALSE')
        expected_list_of_words = ListOfWords()
        expected_list_of_words.append(FalseWord())
        self.assertEqual(expected_list_of_words, a_statement.split_to_list_of_words())

    def test_true_statement_should_be_evaluated_as_true(self):
        a_evaluator = BooleanEvaluator()
        list_of_words = ListOfWords()
        list_of_words.append(TrueWord())
        self.assertTrue(a_evaluator.evaluate(list_of_words))

    def test_false_statement_should_be_evaluated_as_false(self):
        a_evaluator = BooleanEvaluator()
        list_of_words = ListOfWords()
        list_of_words.append(FalseWord())
        self.assertFalse(a_evaluator.evaluate(list_of_words))

    def test_x(self):
        a_evaluator = BooleanEvaluator()
        with self.assertRaises(InvalidArgument):
            a_evaluator.evaluate([])