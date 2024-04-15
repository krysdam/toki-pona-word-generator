import unittest

from wordform import Wordform
from word import Word

class TestWord(unittest.TestCase):
    def test_init(self):
        w = Word(importance=1, source='kalensi')
        self.assertEqual(w.importance, 1)
        self.assertEqual(w.source, 'kalensi')
        w = Word(importance=2, source='sitelen')
        self.assertEqual(w.importance, 2)
        self.assertEqual(w.source, 'sitelen')

    def test_source_cost(self):
        # more similar wordforms should have higher costs.
        # anything more detailed than that is likely to change.
        w = Word(source='kalensi')
        self.assertLess(w.source_cost(Wordform('kalensi')),
                        w.source_cost(Wordform('sitelen')))
        self.assertLess(w.source_cost(Wordform('kalen')),
                        w.source_cost(Wordform('kiwen')))

    def test_gt(self):
        w1 = Word(importance=1)
        w2 = Word(importance=2)
        self.assertTrue(w2 > w1)

    def test_repr(self):
        w = Word(source='kalensi', importance=1)
        self.assertEqual(repr(w), "kalensi(1.000)")

if __name__ == '__main__':
    unittest.main()