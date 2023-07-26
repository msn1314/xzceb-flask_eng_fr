import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"), "Bonjour")
        self.assertEqual(english_to_french("welcome"), "Bienvenue")
        self.assertEqual(english_to_french("love"), "L'amour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hi")
        self.assertEqual(french_to_english("Bienvenue"), "Welcome")
        self.assertEqual(french_to_english("Amour"), "Love")

if __name__ == '__main__':
    unittest.main()
