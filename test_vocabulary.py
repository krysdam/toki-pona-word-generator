import unittest

from vocabulary import *

class TestVocabulary(unittest.TestCase):
    def test_init_from_count(self):
        # does the vocabulary create the right number of words?
        self.assertEqual(len(Vocabulary(count=1).wordforms), 1)
        self.assertEqual(len(Vocabulary(count=10).wordforms), 10)
        self.assertEqual(len(Vocabulary(count=100).wordforms), 100)
        self.assertEqual(len(Vocabulary(count=120).wordforms), 120)
        
    def test_init_from_words(self):
        # does the vocabulary create the right number of words?
        words = [Word() for _ in range(1)]
        self.assertEqual(len(Vocabulary(words=words).wordforms), 1)

        words = [Word() for _ in range(10)]
        self.assertEqual(len(Vocabulary(words=words).wordforms), 10)

        words = [Word() for _ in range(100)]
        self.assertEqual(len(Vocabulary(words=words).wordforms), 100)

        words = [Word() for _ in range(120)]
        self.assertEqual(len(Vocabulary(words=words).wordforms), 120)

    def test_init_is_random(self):
        # are initialized random words actually random?
        # words should be heterogeneous.
        # measure this by looking at the first sounds and shapes of the words.
        vocab = Vocabulary(count=100)
        first_sounds = set()
        shapes = set()
        for w in vocab.wordforms.values():
            first_sounds.add(w.first_sound())
            shapes.add(w.shape())
        self.assertGreater(len(first_sounds), 1)
        self.assertGreater(len(shapes), 1)

    def test_alter_if_better(self):
        # does altering the vocabulary reduce or maintain the cost?
        for _ in range(100):
            vocab = Vocabulary(count=100)
            cost = vocab.cost()
            vocab.alter_if_better()
            self.assertLessEqual(vocab.cost(), cost)


if __name__ == '__main__':
    unittest.main()