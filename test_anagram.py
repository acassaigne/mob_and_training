import unittest

class Anagram:
    def compute(self, input_string):
        if len(input_string) == 1:
            return [input_string]
        elif len(input_string) == 2:
            return [input_string,input_string[-1]+input_string[0]]
        else:
            on est mal

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
        self.assertEqual(["abc","acb","bac","bca","cab","cba"], result)