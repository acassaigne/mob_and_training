import unittest

class TestStringMethods(unittest.TestCase):

    def test_(self):
        anagram = Anagram()

        result = anagram.compute()

        self.assertEqual(["a"], result)
