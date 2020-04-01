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


class TestStringMethods(unittest.TestCase):

    def test_from_string_a_should_return_list_with_a(self):
        anagram = Anagram()
        result = anagram.compute("a")
        self.assertEqual(["a"], result)

    def test_from_string_ab_should_return_list_with_ab_and_ba(self):
        anagram = Anagram()
        result = anagram.compute("ab")
        self.assertEqual(["ab","ba"], result)

    def test_from_string_abc_should_return_sorted_all_anagrams(self):
        anagram = Anagram()
        result = anagram.compute("abc")
        self.assertEqual(sorted(["abc","acb","bac","bca","cab","cba"]), result)

    def test_from_string_abcd_should_return_sorted_all_anagrams(self):
