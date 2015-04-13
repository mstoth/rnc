import unittest
from rnc import add

class AdditionTest(unittest.TestCase):

    def test_adding_Is(self):
        self.assertEqual(add('I', 'I'), 'II')
        self.assertEqual(add('I', 'II'), 'III')

    def test_inputs_out_of_scope_raise_exceptions(self):
        with self.assertRaises(ValueError):
            add('I', 2)
        with self.assertRaises(ValueError):
            add('I', 'V')

if __name__ == '__main__':
    unittest.main()
