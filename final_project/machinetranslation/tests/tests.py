import unittest

from translator import english_to_french, french_to_english


class testTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertNotEqual(english_to_french("welcome"), "bon")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bienvenue"), "nice")


if __name__ == "__main__":
    unittest.main()
