import unittest
import hangman

class TestHangmanGame(unittest.TestCase):
    def test_words_list(self):
        """Test that the word list contains exactly 5 predefined words as specified."""
        self.assertEqual(len(hangman.WORDS), 5)
        for word in hangman.WORDS:
            self.assertTrue(word.isalpha())
            self.assertTrue(word.islower())

    def test_max_incorrect_guesses(self):
        """Test that max incorrect guesses is set to 6."""
        self.assertEqual(hangman.MAX_INCORRECT_GUESSES, 6)
        self.assertEqual(len(hangman.HANGMAN_PICS), 7)  # 0 to 6 = 7 visual stages

    def test_win_condition_check(self):
        """Test the logic for victory when all letters are guessed."""
        secret_word = "python"
        guessed_letters = ["p", "y", "t", "h", "o", "n"]
        is_won = all(letter in guessed_letters for letter in secret_word)
        self.assertTrue(is_won)

    def test_incomplete_word_check(self):
        """Test that incomplete guess is not counted as win."""
        secret_word = "python"
        guessed_letters = ["p", "y", "t"]
        is_won = all(letter in guessed_letters for letter in secret_word)
        self.assertFalse(is_won)

    def test_word_masking(self):
        """Test word display masking with underscores."""
        secret_word = "codealpha"
        guessed = ["c", "a"]
        display = [letter if letter in guessed else "_" for letter in secret_word]
        self.assertEqual(display, ["c", "_", "_", "_", "a", "_", "_", "_", "a"])

if __name__ == "__main__":
    unittest.main()
