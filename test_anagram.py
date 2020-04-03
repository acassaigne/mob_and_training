import unittest

class Anagram:
    def compute(self, input_string):
        if len(input_string) == 1:
            return [input_string]
        elif len(input_string) == 2:
            return [input_string, self.swap(input_string)]
        else:
            result_temp = self.compute(input_string[0:2])
            rest_character = input_string[2]
            result = self.fill_new_letter(result_temp,rest_character)
            return sorted(result)

    def swap(self, input_string):
        return input_string[-1]+input_string[0]

    def fill_new_letter(self, input_string, letter):
        result = []
        for word in input_string:
            result.append(letter + word)
            result.append(word + letter)
            result.append(word[0] + letter + word[1])
        return result


class AnagramRufin:

    def compute(self, input_string):
        if len(input_string) == 1:
            return [input_string]
        else:
            first_letter = input_string[0]
            rest_of_string = input_string[1:]
            anagrams_for_rest_of_string = self.compute(rest_of_string)
            result = self.place_letter_at_all_positions_in_word_list(first_letter, anagrams_for_rest_of_string)
            return sorted(self.remove_duplicate_words(result))

    def remove_duplicate_words(self, word_list):
        return list(set(word_list))

    def place_letter_at_all_positions_in_word_list(self, letter, words):
        result = []
        for word in words:
            generator = WordsGenerators(letter, word)
            new_words = generator.generate_words()
            result = result + new_words
        return result


class WordsGenerators:

    def __init__(self, letter, word):
        self.word = word
        self.letter = letter

    def generate_words(self):
        result = []
        for i in range(len(self.word)+1):
            result.append(self.generate_new_word(i))
        return result

    def generate_new_word(self, position_number):
        return self.word[0:position_number] + self.letter + self.word[position_number:len(self.word)]


class AnagramMax:

    def compute(self, input_string):
        result = self.generate_sub_tuples("", input_string)
        return self.remove_duplicate_words(result)

    #TODO : Rename this function
    def generate_sub_tuples(self, left, rest_of_word):
        if len(rest_of_word) == 1:
            return [left + rest_of_word]
        result = []
        for i in range(len(rest_of_word)):
            other_tuples = self.generate_sub_tuples(left + rest_of_word[i], self.remove_ith_letter(i, rest_of_word))
            result = result + other_tuples
        return result

    def remove_ith_letter(self, i, word):
        return word[0:i] + word[i + 1:]

    def remove_duplicate_words(self, word_list):
        return list(set(word_list))

class TestStringMethods(unittest.TestCase):

    @unittest.skip("first")
    def test_from_string_a_should_return_list_with_a(self):
        anagram = Anagram()
        result = anagram.compute("a")
        self.assertEqual(["a"], result)

    @unittest.skip("wait 2 letters")
    def test_from_string_ab_should_return_list_with_ab_and_ba(self):
        anagram = Anagram()
        result = anagram.compute("ab")
        self.assertEqual(["ab","ba"], result)

    @unittest.skip("wait 3")
    def test_from_string_abc_should_return_sorted_all_anagrams(self):
        anagram = Anagram()
        result = anagram.compute("abc")
        self.assertEqual(sorted(["abc","acb","bac","bca","cab","cba"]), result)

    def test_rufin_one_letter(self):
        anagram = AnagramRufin()
        result = anagram.compute("a")
        self.assertEqual(["a"], result)

    def test_rufin_two_letters(self):
        anagram = AnagramRufin()
        result = anagram.compute("ab")
        self.assertEqual(["ab", "ba"], result)

    def test_rufin_three_letters(self):
        anagram = AnagramRufin()
        result = anagram.compute("abc")
        self.assertEqual(["abc", "acb","bac","bca","cab","cba"], result)

    def test_rufin_with_duplicate_letters(self):
        anagram = AnagramRufin()
        result = anagram.compute("aa")
        self.assertEqual(["aa"], result)

    def test_max_one_letter(self):
        anagram = AnagramMax()
        result = anagram.compute("a")
        self.assertEqual(["a"], result)

    def test_max_two_letters(self):
        anagram = AnagramMax()
        result = anagram.compute("ab")
        self.assertEqual(sorted(["ab", "ba"]), sorted(result))

    def test_max_ith_letter(self):
        anagram = AnagramMax()
        result = anagram.remove_ith_letter(0, "ab")
        self.assertEqual("b", result)

    def test_max_three_letters(self):
        anagram = AnagramMax()
        result = anagram.compute("bca")
        self.assertEqual(sorted(["abc", "acb","bac","bca","cab","cba"]), sorted(result))
