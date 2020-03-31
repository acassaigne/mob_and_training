import unittest

def create_list(input_string):
    return input_string.split(",")

class TestStringMethods(unittest.TestCase):

    def test_x(self):
        self.assertEqual(["1","1"], create_list("1,1"))

    def test_if_create_list_of_empty_string_should_return_empty_list(self):
        self.assertEqual([], create_list(""))
