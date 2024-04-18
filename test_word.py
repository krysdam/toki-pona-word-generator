import unittest

from wordform import Wordform
from word import Word

class TestWord(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Word('kalensi').source, 'kalensi')
        self.assertEqual(Word('sitelen').source, 'sitelen')

    def test_source_cost(self):
        # more similar wordforms should have higher costs.
        # anything more detailed than that is likely to change.
        w = Word('kalensi')
        self.assertLess(w.source_cost(Wordform('kalensi')),
                        w.source_cost(Wordform('sitelen')))
        self.assertLess(w.source_cost(Wordform('kalen')),
                        w.source_cost(Wordform('kiwen')))

    def test_repr(self):
        self.assertEqual(str(Word('kalensi')), "Word('kalensi')")

if __name__ == '__main__':
    unittest.main()