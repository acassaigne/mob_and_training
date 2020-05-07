import unittest


class Statement:

    def __init__(self, input_string):
        self.content = input_string

    def __eq__(self, other):
        return self.content == other.content

    def _convert(self, word_string):
        words_dict = {'FALSE': FalseWord(), 'TRUE': TrueWord(), 'NOT': NotWord(), 'AND': AndWord(), 'OR': OrWord()}
        if word_string in words_dict:
            return words_dict[word_string]
        if word_string != '' and word_string not in words_dict:
            raise InvalidStatement

    def _extract_word_from_indexes(self, start, end):
        return self.content[start:end]

    def split_to_list_of_words(self):
        result = ListOfWords()
        self.recursive_split(self.content, result)
        return result

    def recursive_split(self, input_string, result_list):
        current_index = 0
        while current_index < len(input_string) and input_string[current_index] != ' ':
            current_index += 1
        word = input_string[0:current_index]
        converted_word = self._convert(word)
        result_list.append(converted_word)
        if current_index < len(input_string):
            self.recursive_split(input_string[current_index + 1:], result_list)

    def split_by_space_2(self):
        splitted_statement = SplittedStatement()
        splitted_statement.words = self.content.split(' ')
        return splitted_statement

    def split_by_space(self):
        return self.content.split(' ')

    def separate_statement_at_ith_word(self, index):
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

    def __len__(self):
        return len(self.words)

    def __str__(self):
        result = ""
        count = 0
        for word in self.words:
            if count >= 1:
                result += ' | '
            result += str(word)
            count += 1
        return result

    def is_single_word(self):
        return len(self.words) == 1

    def append(self, word):
        if word is None:
            return
        if not issubclass(type(word), Word):
            raise InvalidWord
        self.words.append(word)

    def find_first_instance_of_word(self, word):
        count = 0
        for word_in_list in self.words:
            if word_in_list == word:
                return count
            count += 1
        return None

    def create_sublist(self, start_index, end_index):
        sublist = ListOfWords()
        sublist.words = self.words[start_index:end_index]
        return sublist


class SplittedStatement:

    def __init__(self):
        self.words = []

    def __getitem__(self, item):
        return self.words[item]

    def rebuild_statement(self):
        statement_content = ' '.join(self.words)
        statement = Statement(statement_content)
        return statement

    def find_first_instance_of_word(self, word):
        for index in range(self.words):
            if self.words[index] == word:
                return index
        return None



class BooleanEvaluator:

    def evaluate_single_word(self, word):
        if word == TrueWord():
            return True
        if word == FalseWord():
            return False
        raise InvalidStatement

    def evaluate_or(self, list_of_words):
        or_index = list_of_words.find_first_instance_of_word(OrWord())
        if or_index:
            return self.evaluate(list_of_words.create_sublist(0, or_index)) or \
                   self.evaluate(list_of_words.create_sublist(or_index + 1, len(list_of_words)))

    def evaluate_and(self, list_of_words):
        and_index = list_of_words.find_first_instance_of_word(AndWord())
        if and_index:
            return self.evaluate(list_of_words.create_sublist(0, and_index)) and \
                   self.evaluate(list_of_words.create_sublist(and_index + 1, len(list_of_words)))

    def evaluate(self, list_of_words):
        self._checkIfInvalideArgument(list_of_words)
        if list_of_words.is_single_word():
            word = list_of_words[0]
            return self.evaluate_single_word(word)
        if len(list_of_words) == 2 and list_of_words[0] == NotWord():
            return not self.evaluate(list_of_words.create_sublist(1, len(list_of_words)))
        # operator = list_of_words.first_operator()
        # if operator == OrWord():
        #     return self.evaluate_or(list_of_words)
        # if operator == AndWord():
        #     return self.evaluate_and(list_of_words)
        #
        result_or = self.evaluate_or(list_of_words)
        if result_or is not None:
            return result_or
        result_and = self.evaluate_and(list_of_words)
        if result_and is not None:
            return result_and
        raise InvalidStatement
    
    
    def _checkIfInvalideArgument(self, list_of_words):
        if type(list_of_words) != ListOfWords or list_of_words == ListOfWords():
            raise InvalidArgument


class InvalidArgument(Exception):
    pass


class InvalidWord(Exception):
    pass


class Word:
    def __eq__(self, other):
        return type(self) == type(other)


class TrueWord(Word):
    def __str__(self):
        return "true"


class FalseWord(Word):
    def __str__(self):
        return "false"


class NotWord(Word):
    def __str__(self):
        return "not"


class AndWord(Word):
    def __str__(self):
        return "and"


class OrWord(Word):
    def __str__(self):
        return "or"


class InvalidStatement(Exception):
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
        self.assertEqual(str(a_list_of_words), str(a_statement.split_to_list_of_words()))

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
        self.assertEqual(False, a_evaluator.evaluate(list_of_words))

    def test_invalid_type_of_list_of_words_should_raise_error(self):
        a_evaluator = BooleanEvaluator()
        with self.assertRaises(InvalidArgument):
            a_evaluator.evaluate([])

    def test_an_evaluation_of_an_empty_list_of_words_should_raise_error(self):
        a_evaluator = BooleanEvaluator()
        with self.assertRaises(InvalidArgument):
            a_evaluator.evaluate(ListOfWords())

    def test_split_to_list_of_words_of_true_false_should_return_true_false(self):
        a_statement = Statement('TRUE FALSE')
        expected_list_of_words = ListOfWords()
        expected_list_of_words.append(TrueWord())
        expected_list_of_words.append(FalseWord())
        self.assertEqual(str(expected_list_of_words), str(a_statement.split_to_list_of_words()))

    def test_str_list_of_word_with_true_should_return_true(self):
        list_of_word = ListOfWords()
        list_of_word.append(TrueWord())
        self.assertEqual('true', str(list_of_word))

    def test_str_list_of_word_with_true_false_should_return_true_false(self):
        list_of_word = ListOfWords()
        list_of_word.append(TrueWord())
        list_of_word.append(FalseWord())
        self.assertEqual('true | false', str(list_of_word))

    def test_append_of_non_word_type_should_raise(self):
        list_of_word = ListOfWords()
        with self.assertRaises(InvalidWord):
            list_of_word.append(1)

    def test_append_of_none_should_append_nothing(self):
        list_of_word = ListOfWords()
        list_of_word.append(None)
        self.assertEqual(ListOfWords(), list_of_word)

    def test_not_string_should_return_list_of_word_with_not(self):
        a_statement = Statement('NOT')
        expected_list_of_words = ListOfWords()
        expected_list_of_words.append(NotWord())
        self.assertEqual(str(expected_list_of_words), str(a_statement.split_to_list_of_words()))

    def test_and_string_should_return_list_of_word_with_and(self):
        a_statement = Statement('AND')
        expected_list_of_words = ListOfWords()
        expected_list_of_words.append(AndWord())
        self.assertEqual(str(expected_list_of_words), str(a_statement.split_to_list_of_words()))

    def test_or_string_should_return_list_of_word_with_or(self):
        a_statement = Statement('OR')
        expected_list_of_words = ListOfWords()
        expected_list_of_words.append(OrWord())
        self.assertEqual(str(expected_list_of_words), str(a_statement.split_to_list_of_words()))

    def test_invalid_word_in_statement_should_raise(self):
        a_statement = Statement('TRUC')
        with self.assertRaises(InvalidStatement):
            a_statement.split_to_list_of_words()

    def test_not_true_statement_should_return_false(self):
        a_statement = Statement('NOT TRUE')
        list_of_words = a_statement.split_to_list_of_words()
        a_evaluator = BooleanEvaluator()
        self.assertEqual(False, a_evaluator.evaluate(list_of_words))

    def test_true_and_false_should_return_false_2(self):
        a_statement = Statement('TRUE AND FALSE')
        list_of_words = a_statement.split_to_list_of_words()
        a_evaluator = BooleanEvaluator()
        self.assertEqual(False, a_evaluator.evaluate(list_of_words))

    def test_not_false_and_true_should_return_true(self):
        a_statement = Statement('NOT FALSE AND TRUE')
        list_of_words = a_statement.split_to_list_of_words()
        a_evaluator = BooleanEvaluator()
        self.assertEqual(True, a_evaluator.evaluate(list_of_words))

    def test_true_or_false_should_return_true(self):
        a_statement = Statement('TRUE OR FALSE')
        list_of_words = a_statement.split_to_list_of_words()
        a_evaluator = BooleanEvaluator()
        self.assertEqual(True, a_evaluator.evaluate(list_of_words))

    def test_x(self):
        a_statement = Statement('TRUE OR FALSE')
        list_of_words = a_statement.split_to_list_of_words()
        operator = list_of_words.find_higher_priority_operator()
        self.assertEqual(OrWord(), operator)
