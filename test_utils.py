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

    def test_longest_common_subsequence_of_zero(self):
        # longest common subsequence for no common characters
        self.assertEqual(longest_common_subsequence('a', 'b'), 0)
        self.assertEqual(longest_common_subsequence('ab', 'cd'), 0)
        self.assertEqual(longest_common_subsequence('abc', 'def'), 0)
        self.assertEqual(longest_common_subsequence('abcd', 'efgh'), 0)

    def test_longest_common_subsequence_other(self):
        # other cases
        self.assertEqual(longest_common_subsequence('abc', 'abc'), 3)
        self.assertEqual(longest_common_subsequence('abc', 'abx'), 2)
        self.assertEqual(longest_common_subsequence('abc', 'xbc'), 2)
        self.assertEqual(longest_common_subsequence('abc', 'axc'), 2)

    def test_similarity(self):
        self.assertAlmostEqual(similarity('sitelen', 'sitelen'), 1)
        self.assertAlmostEqual(similarity('sitelen', 'sitewen'), (6/7)**2)
        self.assertAlmostEqual(similarity('kala', 'kama'), (3/4)**2)
        self.assertAlmostEqual(similarity('kala', 'ala'), (3/4)**2)
        self.assertAlmostEqual(similarity('ala', 'ale'), (2/3)**2)
        self.assertAlmostEqual(similarity('sitelen', 'kepeken'), (3/7)**2)
        self.assertAlmostEqual(similarity('musi', 'sitelen'), (2/7)**2)
        self.assertAlmostEqual(similarity('a', 'musi'), 0)



if __name__ == '__main__':
    unittest.main()