import unittest

from word import *

class TestWord(unittest.TestCase):
    def test_init_random(self):
        # are initialized random words random?
        # onsets, vowels, and codas should be hetereogeneous.
        onsets = set()
        vowels = set()
        codas = set()
        for _ in range(100):
            w = Word()
            s = w.syllables[0]
            onsets.add(s.onset)
            vowels.add(s.vowel)
            codas.add(s.coda)
        self.assertGreater(len(onsets), 1)
        self.assertGreater(len(vowels), 1)
        self.assertGreater(len(codas), 1)

    def test_randomize_random(self):
        # are randomized words random?
        # onsets, vowels, and codas should be hetereogeneous.
        onsets = set()
        vowels = set()
        codas = set()
        for _ in range(100):
            w = Word()
            s = w.syllables[0]
            onsets.add(s.onset)
            vowels.add(s.vowel)
            codas.add(s.coda)
        self.assertGreater(len(onsets), 1)
        self.assertGreater(len(vowels), 1)
        self.assertGreater(len(codas), 1)

    def test_randomize_legal(self):
        # are randomized words always legal?
        for _ in range(100):
            w = Word()
            w.randomize()
            self.assertTrue(w.is_legal())

    def test_init_legal(self):
        # are initialized random words legal?
        for _ in range(100):
            w = Word()
            self.assertTrue(w.is_legal())

    def test_init_syllable_count(self):
        # are initialized random words the right length?
        for _ in range(100):
            for l in range(1, 6):
                w = Word(syllable_count=l)
                self.assertEqual(len(w.syllables), l)

    def test_init_parse(self):
        # are initialized words parsed correctly?
        # one syllable words
        self.assertEqual(str(Word('a')), 'a')
        self.assertEqual(str(Word('ma')), 'ma')
        self.assertEqual(str(Word('en')), 'en')
        self.assertEqual(str(Word('kin')), 'kin')
        # two syllable words
        self.assertEqual(str(Word('ilo')), 'ilo')
        self.assertEqual(str(Word('esun')), 'esun')
        self.assertEqual(str(Word('kule')), 'kule')
        self.assertEqual(str(Word('kiwen')), 'kiwen')
        self.assertEqual(str(Word('insa')), 'insa')
        self.assertEqual(str(Word('insan')), 'insan')
        # longer words
        self.assertEqual(str(Word('kalijopilale')), 'kalijopilale')
        self.assertEqual(str(Word('kijetesantakalu')), 'kijetesantakalu')

    def test_parse_string(self):
        # are words parsed correctly into syllables?
        w = Word()
        # one syllable words
        w.parse_string('a')
        self.assertEqual(str(w.syllables[0]), 'a')
        w.parse_string('ma')
        self.assertEqual(str(w.syllables[0]), 'ma')
        w.parse_string('en')
        self.assertEqual(str(w.syllables[0]), 'en')
        w.parse_string('kin')
        self.assertEqual(str(w.syllables[0]), 'kin')
        # two syllable words
        w.parse_string('ilo')
        self.assertEqual(str(w.syllables[0]), 'i')
        self.assertEqual(str(w.syllables[1]), 'lo')
        w.parse_string('esun')
        self.assertEqual(str(w.syllables[0]), 'e')
        self.assertEqual(str(w.syllables[1]), 'sun')
        w.parse_string('kule')
        self.assertEqual(str(w.syllables[0]), 'ku')
        self.assertEqual(str(w.syllables[1]), 'le')
        w.parse_string('kiwen')
        self.assertEqual(str(w.syllables[0]), 'ki')
        self.assertEqual(str(w.syllables[1]), 'wen')
        w.parse_string('insa')
        self.assertEqual(str(w.syllables[0]), 'in')
        self.assertEqual(str(w.syllables[1]), 'sa')
        w.parse_string('insan')
        self.assertEqual(str(w.syllables[0]), 'in')
        self.assertEqual(str(w.syllables[1]), 'san')
        # longer words
        w.parse_string('kijetesantakalu')
        self.assertEqual(str(w.syllables[0]), 'ki')
        self.assertEqual(str(w.syllables[1]), 'je')
        self.assertEqual(str(w.syllables[2]), 'te')
        self.assertEqual(str(w.syllables[3]), 'san')
        self.assertEqual(str(w.syllables[4]), 'ta')
        self.assertEqual(str(w.syllables[5]), 'ka')
        self.assertEqual(str(w.syllables[6]), 'lu')

    def test_is_legal(self):
        # legal words are legal
        self.assertTrue(Word('a').is_legal())
        self.assertTrue(Word('ma').is_legal())
        self.assertTrue(Word('ni').is_legal())
        self.assertTrue(Word('en').is_legal())
        self.assertTrue(Word('kin').is_legal())
        self.assertTrue(Word('ilo').is_legal())
        self.assertTrue(Word('esun').is_legal())
        self.assertTrue(Word('kule').is_legal())
        self.assertTrue(Word('kiwen').is_legal())
        self.assertTrue(Word('insa').is_legal())
        self.assertTrue(Word('insan').is_legal())
        self.assertTrue(Word('kijetesantakalu').is_legal())
        # illegal words are illegal
        self.assertFalse(Word('').is_legal())
        self.assertFalse(Word('n').is_legal())
        self.assertFalse(Word('k').is_legal())
        self.assertFalse(Word('ae').is_legal())
        self.assertFalse(Word('ak').is_legal())
        self.assertFalse(Word('enn').is_legal())
        self.assertFalse(Word('kinn').is_legal())
        self.assertFalse(Word('pppp').is_legal())

    def test_is_legal_tricky(self):
        # tricky cases
        # words with illegal substrings
        self.assertFalse(Word('wuta').is_legal())
        self.assertFalse(Word('tewo').is_legal())
        self.assertFalse(Word('majita').is_legal())
        self.assertFalse(Word('mawiti').is_legal())
        self.assertFalse(Word('amni').is_legal())
        self.assertFalse(Word('anni').is_legal())
        # words with open syllables mid-word
        self.assertFalse(Word('kien').is_legal())
        self.assertFalse(Word('aen').is_legal())

    def test_copy(self):
        # does a copied word match the original?
        # str and number of syllables should match.
        for _ in range(100):
            w = Word()
            c = w.copy()
            self.assertEqual(str(w), str(c))
            self.assertEqual(len(w.syllables), len(c.syllables))

    def test_shape(self):
        # one syllable words
        self.assertEqual(Syllable('a').shape(), 'O')
        self.assertEqual(Syllable('ma').shape(), 'PO')
        self.assertEqual(Syllable('en').shape(), 'ON')
        self.assertEqual(Syllable('ni').shape(), 'PO')
        self.assertEqual(Syllable('kin').shape(), 'PON')
        self.assertEqual(Syllable('nun').shape(), 'PON')
        # two syllable words
        self.assertEqual(Word('ilo').shape(), 'OPO')
        self.assertEqual(Word('esun').shape(), 'OPON')
        self.assertEqual(Word('kule').shape(), 'POPO')
        self.assertEqual(Word('kiwen').shape(), 'POPON')
        self.assertEqual(Word('insa').shape(), 'ONPO')
        self.assertEqual(Word('insan').shape(), 'ONPON')
        # longer word
        self.assertEqual(Word('kijetesantakalu').shape(), 'POPOPOPONPOPOPO')

    def test_first_sound(self):
        # one syllable words
        self.assertEqual(Syllable('a').first_sound(), 'a')
        self.assertEqual(Syllable('ma').first_sound(), 'm')
        self.assertEqual(Syllable('en').first_sound(), 'e')
        self.assertEqual(Syllable('ni').first_sound(), 'n')
        self.assertEqual(Syllable('kin').first_sound(), 'k')
        self.assertEqual(Syllable('nun').first_sound(), 'n')
        # two syllable words
        self.assertEqual(Word('ilo').first_sound(), 'i')
        self.assertEqual(Word('esun').first_sound(), 'e')
        self.assertEqual(Word('kule').first_sound(), 'k')
        self.assertEqual(Word('kiwen').first_sound(), 'k')
        self.assertEqual(Word('insa').first_sound(), 'i')
        self.assertEqual(Word('insan').first_sound(), 'i')
        # longer word
        self.assertEqual(Word('kijetesantakalu').first_sound(), 'k')

    def test_random_variant_same_start(self):
        # do random variants usually, but not always,
        # start with the same letter?
        same_count = 0
        for _ in range(1000):
            w = Word(syllable_count=3)
            v = w.random_variant()
            if w.first_sound() == v.first_sound():
                same_count += 1
        self.assertGreater(same_count, 500)
        self.assertLess(same_count, 1000)

    def test_random_variant_same_syllables(self):
        # do random variants usually, but not always,
        # have the same number of syllables?
        same_count = 0
        for _ in range(1000):
            w = Word(syllable_count=3)
            v = w.random_variant()
            if len(w.syllables) == len(v.syllables):
                same_count += 1
        self.assertGreater(same_count, 500)
        self.assertLess(same_count, 1000)

    def test_random_variant_same_letters(self):
        # do random variants often, but not always,
        # have the same length in letters?
        same_count = 0
        for _ in range(1000):
            w = Word(syllable_count=3)
            v = w.random_variant()
            if len(str(w)) == len(str(v)):
                same_count += 1
        self.assertGreater(same_count, 200)
        self.assertLess(same_count, 1000)    

    def test_random_variant_changes(self):
        # does a random variant change the word?
        for _ in range(100):
            w = Word(syllable_count=3)
            v = w.random_variant()
            self.assertNotEqual(str(w), str(v))

    def test_random_variant_legal(self):
        # are random variants always legal?
        for _ in range(100):
            w = Word(syllable_count=3)
            v = w.random_variant()
            self.assertTrue(v.is_legal())

    def test_compare(self):
        # are words compared correctly?
        self.assertLess(Word('a'), Word('e'))
        self.assertLess(Word('a'), Word('ma'))
        self.assertLess(Word('ma'), Word('ni'))
        self.assertLess(Word('ni'), Word('wawa'))


if __name__ == '__main__':
    unittest.main()