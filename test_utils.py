import unittest

from utils import *

class TestUtils(unittest.TestCase):
    def test_edit_distance_of_zero(self):
        # edit distance for identical strings
        self.assertEqual(edit_distance('a', 'a'), 0)
        self.assertEqual(edit_distance('ab', 'ab'), 0)
        self.assertEqual(edit_distance('abc', 'abc'), 0)
        self.assertEqual(edit_distance('abcd', 'abcd'), 0)
        self.assertEqual(edit_distance('zyxwvutsrqp',
                                       'zyxwvutsrqp'),
                                       0)

    def test_edit_distance_insert(self):
        # insert one character
        self.assertEqual(edit_distance('a', 'ab'), 1)
        self.assertEqual(edit_distance('ab', 'abc'), 1)
        self.assertEqual(edit_distance('ab', 'acb'), 1)
        self.assertEqual(edit_distance('xxxxxx', 'xxxyxxx'), 1)

    def test_edit_distance_delete(self):
        # delete one character
        self.assertEqual(edit_distance('ab', 'a'), 1)
        self.assertEqual(edit_distance('abc', 'ab'), 1)
        self.assertEqual(edit_distance('acb', 'ab'), 1)
        self.assertEqual(edit_distance('xxxyxxx', 'xxxxxx'), 1)

    def test_edit_distance_replace(self):
        # replace one character
        self.assertEqual(edit_distance('a', 'b'), 1)
        self.assertEqual(edit_distance('ab', 'ac'), 1)
        self.assertEqual(edit_distance('ab', 'cb'), 1)
        self.assertEqual(edit_distance('xxxxxx', 'xxyxxx'), 1)

    def test_edit_distance_complex(self):
        # complex cases
        self.assertEqual(edit_distance('abcdefghijk', 'xyabcfghixx'), 6)
        self.assertEqual(edit_distance('contemporary', 'contemptible'), 5)
        self.assertEqual(edit_distance('arithmetic', 'arithmetics'), 1)

    def test_string_dissimilarity(self):
        self.assertAlmostEqual(string_dissimilarity('anpa', 'nanpa'),
                               0.22, places=2)
        self.assertAlmostEqual(string_dissimilarity('kama', 'kala'),
                               0.25, places=2)
        self.assertAlmostEqual(string_dissimilarity('mama', 'wawa'),
                               0.50, places=2)
        self.assertAlmostEqual(string_dissimilarity('tawa', 'kasi'),
                               0.75, places=2)
        self.assertAlmostEqual(string_dissimilarity('telo', 'musi'),
                               1.00, places=2)
        self.assertAlmostEqual(string_dissimilarity('a', 'sitelen'),
                               1.75, places=2)


if __name__ == '__main__':
    unittest.main()