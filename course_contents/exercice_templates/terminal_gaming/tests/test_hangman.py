
import unittest

from termgamelib.hangman import Hangman

class MyHangmanTest( unittest.TestCase ):
 
    def setUp(self):
        # pour initialiser nos ressources pour les tests
        self.generator_no_t = "genera_or"
        self.WORDS = [
            "Danilo",
            "Johnny",
            "Bruno",
            "Vincent",
            "Jonathan",
            "Gerard",
            "Sergey",
        ]
 
    def test_open_underscores(self):

        obtained = Hangman.open_underscores(
            hidden_string=self.generator_no_t,
            letter_occurences=[6],
            user_input="t"
        )

        expected = "generator"

        self.assertEqual(expected, obtained)
        self.assertEqual(expected, obtained)
    
    def test_parity_words(self):
        def is_len_word_odd(word: str) -> bool:
            return len(word) % 2 == 1

        expected = [False, False, True, True, False, False, False]
        obtained = [is_len_word_odd(w) for w in self.WORDS]

        for a, b in zip(expected, obtained):
            self.assertEqual(a, b)
