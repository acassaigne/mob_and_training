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
            new_word = self.generate_words(letter, word)
            result = result + new_word
        return result

    def generate_words(self, letter, word):
        result = []
        for i in range(len(word)+1):
             result.append(self.generate_new_word(i, letter, word))
        return result

    def generate_new_word(self, position_number, letter, word):
        return word[0:position_number] + letter + word[position_number:len(word)]

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