import unittest

from syllable import *

class TestSyllable(unittest.TestCase):
    def test_init_random(self):
        # are initialized random syllables random?
        # onsets, vowels, and codas should be hetereogeneous.
        onsets = set()
        vowels = set()
        codas = set()
        for _ in range(100):
            s = Syllable()
            onsets.add(s.onset)
            vowels.add(s.vowel)
            codas.add(s.coda)
        self.assertGreater(len(onsets), 1)
        self.assertGreater(len(vowels), 1)
        self.assertGreater(len(codas), 1)

    def test_randomize_random(self):
        # are randomized syllables random?
        # onsets, vowels, and codas should be hetereogeneous.
        onsets = set()
        vowels = set()
        codas = set()
        for _ in range(100):
            s = Syllable()
            s.randomize()
            onsets.add(s.onset)
            vowels.add(s.vowel)
            codas.add(s.coda)
        self.assertGreater(len(onsets), 1)
        self.assertGreater(len(vowels), 1)
        self.assertGreater(len(codas), 1)

    def test_randomize_legal(self):
        # are randomized syllables always legal?
        for _ in range(100):
            s = Syllable()
            s.randomize()
            self.assertTrue(s.is_legal())

    def test_init_legal(self):
        # are initialized random syllables legal?
        for _ in range(100):
            s = Syllable()
            self.assertTrue(s.is_legal())

    def test_init_parse(self):
        # are initialized syllables parsed correctly?
        self.assertEqual(str(Syllable('a')), 'a')
        self.assertEqual(str(Syllable('ma')), 'ma')
        self.assertEqual(str(Syllable('en')), 'en')
        self.assertEqual(str(Syllable('kin')), 'kin')

    def test_parse_string(self):
        # are syllables parsed correctly into onset, vowel, and coda?
        s = Syllable()
        s.parse_string('a')
        self.assertEqual(s.onset, '')
        self.assertEqual(s.vowel, 'a')
        self.assertEqual(s.coda, '')
        s.parse_string('ma')
        self.assertEqual(s.onset, 'm')
        self.assertEqual(s.vowel, 'a')
        self.assertEqual(s.coda, '')
        s.parse_string('en')
        self.assertEqual(s.onset, '')
        self.assertEqual(s.vowel, 'e')
        self.assertEqual(s.coda, 'n')
        s.parse_string('kin')
        self.assertEqual(s.onset, 'k')
        self.assertEqual(s.vowel, 'i')
        self.assertEqual(s.coda, 'n')

    def test_is_legal(self):
        # legal syllables are legal
        self.assertTrue(Syllable('a').is_legal())
        self.assertTrue(Syllable('ma').is_legal())
        self.assertTrue(Syllable('ni').is_legal())
        self.assertTrue(Syllable('en').is_legal())
        self.assertTrue(Syllable('kin').is_legal())
        self.assertTrue(Syllable('nun').is_legal())
        # illegal syllables are illegal
        self.assertFalse(Syllable('').is_legal())
        self.assertFalse(Syllable('n').is_legal())
        self.assertFalse(Syllable('k').is_legal())
        self.assertFalse(Syllable('ae').is_legal())
        self.assertFalse(Syllable('ak').is_legal())
        self.assertFalse(Syllable('enn').is_legal())
        self.assertFalse(Syllable('kinn').is_legal())
        self.assertFalse(Syllable('kala').is_legal())

    def test_is_legal_tricky(self):
        # trickier cases
        self.assertFalse(Syllable('wu').is_legal())
        self.assertFalse(Syllable('wo').is_legal())
        self.assertFalse(Syllable('ji').is_legal())
        self.assertFalse(Syllable('ti').is_legal())

    def test_copy(self):
        # does a copied syllable match the original?
        # str, onset, vowel, and coda should all match.
        for _ in range(100):
            s = Syllable()
            c = s.copy()
            self.assertEqual(str(s), str(c))
            self.assertEqual(s.onset, c.onset)
            self.assertEqual(s.vowel, c.vowel)
            self.assertEqual(s.coda, c.coda)

    def test_shape(self):
        self.assertEqual(Syllable('a').shape(), 'O')
        self.assertEqual(Syllable('ma').shape(), 'PO')
        self.assertEqual(Syllable('en').shape(), 'ON')
        self.assertEqual(Syllable('ni').shape(), 'PO')
        self.assertEqual(Syllable('kin').shape(), 'PON')
        self.assertEqual(Syllable('nun').shape(), 'PON')

    def test_first_sound(self):
        self.assertEqual(Syllable('a').first_sound(), 'a')
        self.assertEqual(Syllable('ma').first_sound(), 'm')
        self.assertEqual(Syllable('en').first_sound(), 'e')
        self.assertEqual(Syllable('ni').first_sound(), 'n')
        self.assertEqual(Syllable('kin').first_sound(), 'k')
        self.assertEqual(Syllable('nun').first_sound(), 'n')

    def test_random_variant_matches(self):
        # does a random variant mostly match the original?
        # between onset, vowel, and coda,
        # the words will be identical in exactly two.
        for _ in range(100):
            syllable = Syllable()
            syllable.randomize()
            variant = syllable.random_variant()
            matches = ((variant.onset == syllable.onset) +
                       (variant.vowel == syllable.vowel) +
                       (variant.coda == syllable.coda))
            self.assertEqual(matches, 2)
        
    def test_random_variant_changes(self):
        # is a random variant different from the original?
        for _ in range(100):
            syllable = Syllable()
            syllable.randomize()
            variant = syllable.random_variant()
            self.assertNotEqual(str(syllable), str(variant))

    def test_random_variant_legal(self):
        # are random variants always legal?
        for _ in range(100):
            syllable = Syllable()
            syllable.randomize()
            variant = syllable.random_variant()
            self.assertTrue(variant.is_legal())


if __name__ == '__main__':
    unittest.main()