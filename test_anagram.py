import unittest

class Anagram:
    def compute(self, input_string):
        if len(input_string) == 1:
            return [input_string]
        elif len(input_string) == 2:
            return [input_string, input_string[-1]+input_string[0]]
        else:
            result = []
            result_temp = self.compute(input_string[0:2])
            rest_character = input_string[2]
            for word in result_temp:
                result.append(rest_character + word)
                result.append(word + rest_character)
                result.append(word[0] + rest_character + word[1])
            return sorted(result)

class TestStringMethods(unittest.TestCase):

    def test_from_string_a_should_return_list_with_a(self):
        anagram = Anagram()
        result = anagram.compute("a")
        self.assertEqual(["a"], result)

    def test_from_string_ab_should_return_list_with_ab_and_ba(self):
        anagram = Anagram()
        result = anagram.compute("ab")
        self.assertEqual(["ab","ba"], result)

    def test_ouzoief(self):
        anagram = Anagram()
        result = anagram.compute("abc")
        self.assertEqual(sorted(["abc","acb","bac","bca","cab","cba"]), result)