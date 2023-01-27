import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

import unittest
from machinetranslation import translator

class TestMyModule(unittest.TestCase):

    def test_english_to_french(self):
        input_case = "Hello"
        expected = "Bonjour"
        self.assertEqual(translator.english_to_french(input_case),expected)

    def test_english_to_french_none(self):
        input_case = None
        expected = "English text required"
        self.assertEqual(translator.english_to_french(input_case),expected)
    
    def test_english_to_french_not(self):
        input_case = "Hello"
        expected = "Hello"
        self.assertNotEqual(translator.french_to_english(input_case),expected)

    def test_french_to_english(self):
        input_case = "Bonjour"
        expected = "Hello"
        self.assertEqual(translator.french_to_english(input_case),expected)

    def test_french_to_english_none(self):
        input_case = None
        expected = "French text required"
        self.assertEqual(translator.french_to_english(input_case),expected)

    def test_french_to_english_not(self):
        input_case = "Bonjour"
        expected = "Bonjour"
        self.assertNotEqual(translator.french_to_english(input_case),expected)


if __name__ == '__main__':
    unittest.main()
