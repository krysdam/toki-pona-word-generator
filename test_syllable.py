import unittest

from syllable import *

class TestSyllable(unittest.TestCase):
    def test_init(self):
        # are initialized syllables parsed correctly?
        syl = Syllable('a')
        self.assertEqual(syl.onset, '')
        self.assertEqual(syl.vowel, 'a')
        self.assertEqual(syl.coda, '')
        syl = Syllable('ma')
        self.assertEqual(syl.onset, 'm')
        self.assertEqual(syl.vowel, 'a')
        self.assertEqual(syl.coda, '')
        syl = Syllable('ni')
        self.assertEqual(syl.onset, 'n')
        self.assertEqual(syl.vowel, 'i')
        self.assertEqual(syl.coda, '')
        syl = Syllable('en')
        self.assertEqual(syl.onset, '')
        self.assertEqual(syl.vowel, 'e')
        self.assertEqual(syl.coda, 'n')
        syl = Syllable('kin')
        self.assertEqual(syl.onset, 'k')
        self.assertEqual(syl.vowel, 'i')
        self.assertEqual(syl.coda, 'n')
        syl = Syllable('nun')
        self.assertEqual(syl.onset, 'n')
        self.assertEqual(syl.vowel, 'u')
        self.assertEqual(syl.coda, 'n')

    def test_parse(self):
        # are syllables parsed correctly into onset, vowel, and coda?
        self.assertEqual(Syllable.parse('a'), ('', 'a', ''))
        self.assertEqual(Syllable.parse('ma'), ('m', 'a', ''))
        self.assertEqual(Syllable.parse('ni'), ('n', 'i', ''))
        self.assertEqual(Syllable.parse('en'), ('', 'e', 'n'))
        self.assertEqual(Syllable.parse('kin'), ('k', 'i', 'n'))
        self.assertEqual(Syllable.parse('nun'), ('n', 'u', 'n'))

    def test_parse_illegal(self):
        # does parse raise an error on illegal syllables?
        self.assertRaises(ValueError, Syllable.parse, '')
        self.assertRaises(ValueError, Syllable.parse, 'k')
        self.assertRaises(ValueError, Syllable.parse, 'kli')
        self.assertRaises(ValueError, Syllable.parse, 'kai')
        self.assertRaises(ValueError, Syllable.parse, 'inn')
        self.assertRaises(ValueError, Syllable.parse, 'ik')
        self.assertRaises(ValueError, Syllable.parse, 'kln')

    def test_first_sound(self):
        self.assertEqual(Syllable('a').first_sound(), 'a')
        self.assertEqual(Syllable('ma').first_sound(), 'm')
        self.assertEqual(Syllable('ni').first_sound(), 'n')
        self.assertEqual(Syllable('en').first_sound(), 'e')
        self.assertEqual(Syllable('kin').first_sound(), 'k')
        self.assertEqual(Syllable('nun').first_sound(), 'n')

    def test_shape(self):
        self.assertEqual(Syllable('a').shape(), 'O')
        self.assertEqual(Syllable('ma').shape(), 'PO')
        self.assertEqual(Syllable('ni').shape(), 'PO')
        self.assertEqual(Syllable('en').shape(), 'ON')
        self.assertEqual(Syllable('kin').shape(), 'PON')
        self.assertEqual(Syllable('nun').shape(), 'PON')

    def test_spelling(self):
        self.assertEqual(Syllable('a').spelling(), 'a')
        self.assertEqual(Syllable('ma').spelling(), 'ma')
        self.assertEqual(Syllable('ni').spelling(), 'ni')
        self.assertEqual(Syllable('en').spelling(), 'en')
        self.assertEqual(Syllable('kin').spelling(), 'kin')
        self.assertEqual(Syllable('nun').spelling(), 'nun')

    def test_all_syllables(self):
        # should generate all legal syllables.
        # (10 onsets, 5 vowels, forbid wu wo ji ti, 2 codas)
        self.assertEqual(len(SYLLABLES), (10*5-4)*2)


if __name__ == '__main__':
    unittest.main()