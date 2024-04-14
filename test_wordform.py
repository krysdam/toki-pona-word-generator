import unittest

from wordform import *

class TestWord(unittest.TestCase):
    def test_init_parse_1syl(self):
        # are initialized wordforms parsed correctly?
        # one syllable wordforms
        wordform = Wordform('a')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['a'])

        wordform = Wordform('ma')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['ma'])

        wordform = Wordform('ni')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['ni'])

        wordform = Wordform('en')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['en'])

        wordform = Wordform('kin')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['kin'])

        wordform = Wordform('nun')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['nun'])

    def test_init_parse_2syl(self):
        # are initialized wordforms parsed correctly?
        # two syllable wordforms
        wordform = Wordform('ilo')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['i', 'lo'])

        wordform = Wordform('esun')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['e', 'sun'])

        wordform = Wordform('kule')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['ku', 'le'])

        wordform = Wordform('kiwen')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['ki', 'wen'])

        wordform = Wordform('insa')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['in', 'sa'])

        wordform = Wordform('insan')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables), ['in', 'san'])

    def test_init_parse_long(self):
        # are initialized wordforms parsed correctly?
        # longer wordforms
        wordform = Wordform('kijetesantakalu')
        syllables = map(Syllable.spelling, wordform.syllables)
        self.assertEqual(list(syllables),
                         ['ki', 'je', 'te', 'san', 'ta', 'ka', 'lu'])
        
    def test_init_parse_illegal(self):
        # does parse raise an error on obviously illegal words?
        # (no error is expected for words are only 'slightly illegal',
        # such as wuta or kai)
        self.assertRaises(ValueError, Wordform, '')
        self.assertRaises(ValueError, Wordform, 'k')
        self.assertRaises(ValueError, Wordform, 'kli')
        self.assertRaises(ValueError, Wordform, 'inn')
        self.assertRaises(ValueError, Wordform, 'ik')
        self.assertRaises(ValueError, Wordform, 'kln')

    def test_init_syllables(self):
        # does init accept a list of Syllables?
        wordform = Wordform(syllables=[Syllable('a')])
        self.assertEqual(wordform.spelling(), 'a')

        wordform = Wordform(syllables=[Syllable('i'), Syllable('lo')])
        self.assertEqual(wordform.spelling(), 'ilo')

        wordform = Wordform(syllables=[Syllable('ki'), Syllable('wen')])
        self.assertEqual(wordform.spelling(), 'kiwen')

        wordform = Wordform(syllables=[Syllable('in'), Syllable('san')])
        self.assertEqual(wordform.spelling(), 'insan')

        wordform = Wordform(syllables=[Syllable('ki'), Syllable('je'),
                                       Syllable('te'), Syllable('san'),
                                       Syllable('ta'), Syllable('ka'),
                                       Syllable('lu')])
        self.assertEqual(wordform.spelling(), 'kijetesantakalu')

    def test_shape(self):
        # one syllable words
        self.assertEqual(Wordform('a').shape(), 'O')
        self.assertEqual(Wordform('ma').shape(), 'PO')
        self.assertEqual(Wordform('en').shape(), 'ON')
        self.assertEqual(Wordform('ni').shape(), 'PO')
        self.assertEqual(Wordform('kin').shape(), 'PON')
        self.assertEqual(Wordform('nun').shape(), 'PON')
        # two syllable words
        self.assertEqual(Wordform('ilo').shape(), 'OPO')
        self.assertEqual(Wordform('esun').shape(), 'OPON')
        self.assertEqual(Wordform('kule').shape(), 'POPO')
        self.assertEqual(Wordform('kiwen').shape(), 'POPON')
        self.assertEqual(Wordform('insa').shape(), 'ONPO')
        self.assertEqual(Wordform('insan').shape(), 'ONPON')
        # longer word
        self.assertEqual(Wordform('kijetesantakalu').shape(),
                         'POPOPOPONPOPOPO')

    def test_first_sound(self):
        # one syllable words
        self.assertEqual(Wordform('a').first_sound(), 'a')
        self.assertEqual(Wordform('ma').first_sound(), 'm')
        self.assertEqual(Wordform('en').first_sound(), 'e')
        self.assertEqual(Wordform('ni').first_sound(), 'n')
        self.assertEqual(Wordform('kin').first_sound(), 'k')
        self.assertEqual(Wordform('nun').first_sound(), 'n')
        # two syllable words
        self.assertEqual(Wordform('ilo').first_sound(), 'i')
        self.assertEqual(Wordform('esun').first_sound(), 'e')
        self.assertEqual(Wordform('kule').first_sound(), 'k')
        self.assertEqual(Wordform('kiwen').first_sound(), 'k')
        self.assertEqual(Wordform('insa').first_sound(), 'i')
        self.assertEqual(Wordform('insan').first_sound(), 'i')
        # longer word
        self.assertEqual(Wordform('kijetesantakalu').first_sound(), 'k')

    def test_spelling(self):
        # one syllable words
        self.assertEqual(Wordform('a').spelling(), 'a')
        self.assertEqual(Wordform('ma').spelling(), 'ma')
        self.assertEqual(Wordform('en').spelling(), 'en')
        self.assertEqual(Wordform('ni').spelling(), 'ni')
        self.assertEqual(Wordform('kin').spelling(), 'kin')
        self.assertEqual(Wordform('nun').spelling(), 'nun')
        # two syllable words
        self.assertEqual(Wordform('ilo').spelling(), 'ilo')
        self.assertEqual(Wordform('esun').spelling(), 'esun')
        self.assertEqual(Wordform('kule').spelling(), 'kule')
        self.assertEqual(Wordform('kiwen').spelling(), 'kiwen')
        self.assertEqual(Wordform('insa').spelling(), 'insa')
        self.assertEqual(Wordform('insan').spelling(), 'insan')
        # longer word
        self.assertEqual(Wordform('kijetesantakalu').spelling(),
                         'kijetesantakalu')

    def test_inherent_cost(self):
        # more cumbersome word-forms should have higher costs.
        # anything more detailed than that is likely to change.
        self.assertGreater(Wordform('len').inherent_cost(),
                           Wordform('a').inherent_cost())
        self.assertGreater(Wordform('kipisi').inherent_cost(),
                           Wordform('len').inherent_cost())
        self.assertGreater(Wordform('kijetesantakalu').inherent_cost(),
                           Wordform('kipisi').inherent_cost())
        
    def test_similarity_cost(self):
        # more similar wordforms should have higher costs.
        # anything more detailed than that is likely to change.
        self.assertGreater(Wordform('kala')
                           .similarity_cost(Wordform('kalama')),
                           Wordform('kule')
                           .similarity_cost(Wordform('kalama')))
        self.assertGreater(Wordform('anpa').similarity_cost(Wordform('nanpa')),
                           Wordform('anpa').similarity_cost(Wordform('monsi')))
        self.assertGreater(Wordform('telo').similarity_cost(Wordform('wawa')),
                           Wordform('telo').similarity_cost(Wordform('wawan')))
        self.assertGreater(Wordform('taso').similarity_cost(Wordform('tu')),
                           Wordform('taso').similarity_cost(Wordform('mu')))

    def test_similarity_cost_symmetric(self):
        # similarity cost should be symmetric
        self.assertEqual(Wordform('kala').similarity_cost(Wordform('kalama')),
                         Wordform('kalama').similarity_cost(Wordform('kala')))
        self.assertEqual(Wordform('anpa').similarity_cost(Wordform('nanpa')),
                         Wordform('nanpa').similarity_cost(Wordform('anpa')))
        self.assertEqual(Wordform('telo').similarity_cost(Wordform('wawa')),
                         Wordform('wawa').similarity_cost(Wordform('telo')))
        self.assertEqual(Wordform('taso').similarity_cost(Wordform('tu')),
                         Wordform('tu').similarity_cost(Wordform('telo')))

    def test_compare(self):
        # are wordforms compared correctly?
        self.assertLess(Wordform('a'), Wordform('e'))
        self.assertLess(Wordform('a'), Wordform('ma'))
        self.assertLess(Wordform('ma'), Wordform('ni'))
        self.assertLess(Wordform('ni'), Wordform('wawa'))

    def test_all_wordforms(self):
        # certain properties that the WORDFORM list constants should have.
        self.assertEqual(len(WORDFORMS_1SYL), 92)
        self.assertEqual(len(WORDFORMS_2SYL), 6624)
        self.assertEqual(len(WORDFORMS), 92 + 6624)

if __name__ == '__main__':
    unittest.main()