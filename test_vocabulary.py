import unittest

from word import Word
from vocabulary import Vocabulary

class TestVocabulary(unittest.TestCase):
    def test_init_from_words(self):
        # does the vocabulary create the right number of words?
        vocab = Vocabulary([Word('') for _ in range(1)])
        self.assertEqual(len(vocab.wordforms), 1)
        vocab = Vocabulary([Word('') for _ in range(10)])
        self.assertEqual(len(vocab.wordforms), 10)
        vocab = Vocabulary([Word('') for _ in range(100)])
        self.assertEqual(len(vocab.wordforms), 100)

    def test_cost(self):
        # cost should be greater than 0.
        vocab = Vocabulary([Word('') for _ in range(100)])
        self.assertGreater(vocab.cost(), 0)

    def test_alter_if_better(self):
        # does altering the vocabulary reduce or maintain the cost?
        for _ in range(10):
            vocab = Vocabulary([Word('') for _ in range(40)])
            cost = vocab.cost()
            vocab.alter_if_better()
            self.assertLessEqual(vocab.cost(), cost)


if __name__ == '__main__':
    unittest.main()