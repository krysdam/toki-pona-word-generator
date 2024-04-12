import unittest

from vocabulary import *

class TestVocabulary(unittest.TestCase):
    def test_init_random(self):
        # are initialized random words random?
        # words should be heterogeneous.
        # measure this by looking at the first sounds and shapes of the words.
        vocab = Vocabulary(count=100)
        first_sounds = set()
        shapes = set()
        for w in vocab.words:
            first_sounds.add(w.first_sound())
            shapes.add(w.shape())
        self.assertGreater(len(first_sounds), 1)
        self.assertGreater(len(shapes), 1)

    def test_randomize_random(self):
        # are randomized words random?
        # words should be heterogeneous.
        # measure this by looking at the first sounds and shapes of the words.
        vocab = Vocabulary()
        vocab.randomize(count=100)
        first_sounds = set()
        shapes = set()
        for w in vocab.words:
            first_sounds.add(w.first_sound())
            shapes.add(w.shape())
        self.assertGreater(len(first_sounds), 1)
        self.assertGreater(len(shapes), 1)

    def test_init_legal(self):
        # are initialized random words legal?
        vocab = Vocabulary(count=1000)
        for w in vocab.words:
            self.assertTrue(w.is_legal())

    def test_init_unique(self):
        # are initialized random words unique?
        vocab = Vocabulary(count=1000)
        string_words = {str(w) for w in vocab.words}
        self.assertEqual(len(string_words), 1000)

    def test_init_count(self):
        # does the vocabulary have the right number of words?
        vocab = Vocabulary(count=1)
        self.assertEqual(len(vocab.words), 1)
        vocab = Vocabulary(count=10)
        self.assertEqual(len(vocab.words), 10)
        vocab = Vocabulary(count=100)
        self.assertEqual(len(vocab.words), 100)
        vocab = Vocabulary(count=120)
        self.assertEqual(len(vocab.words), 120)

    def test_init_parse(self):
        # if words are supplied, are they parsed correctly?
        words = ['a', 'ma', 'ni', 'en', 'kin']
        vocab = Vocabulary(words=['a', 'ma', 'ni', 'en', 'kin'])
        string_words = {str(w) for w in vocab.words}
        self.assertEqual(string_words, set(words))

    def test_alter_if_better(self):
        # does altering the vocabulary reduce or maintain the cost?
        for _ in range(100):
            vocab = Vocabulary(count=100)
            cost = vocab.cost()
            vocab.alter_if_better()
            self.assertLessEqual(vocab.cost(), cost)


if __name__ == '__main__':
    unittest.main()