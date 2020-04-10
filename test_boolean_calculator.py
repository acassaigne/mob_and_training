import unittest

def boolean_calculator(boolean_expression):
    return True


class TestStringMethods(unittest.TestCase):

    def test_should_return_true(self):
        self.assertEqual(True, boolean_calculator("TRUE"))




    #TODO: continuer à explorer l'axe and/not
    #TODO: AND > OR