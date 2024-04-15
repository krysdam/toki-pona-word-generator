from functools import lru_cache

from constants import CACHINESS, VOWELS
from utils import edit_distance_adjusted

from syllable import Syllable, SYLLABLES

class Wordform:
    def __init__(self, word:str=None, syllables:list=None):
        """Create a word. If none provided, raise a ValueError."""
        if word is not None:
            self.syllables = Wordform.parse(word)
        elif syllables is not None:
            self.syllables = syllables
        else:
            raise ValueError("Must provide a word or syllables.")

    def parse(word:str):
        """Parse a word from the given string. Return a list of Syllables.
        
        If the given string is not a valid word, raise a ValueError.
        Actually, many illegal words will be accepted, such as wuta or kai.
        This function only checks that the word can be broken into syllables,
        each of which has an optional onset, a vowel, and an optional coda.
        Rules more detailed than that (eg: wuwojiti, nn, mm) are not checked.
        """
        # in a toki pona word,
        # the longest suffix that is a legal syllable
        # is always an actual syllable of the word.
        # so, check if the last 3 letters is a syllable,
        # else 2 letters, else 1 letter.
        # if none of these is a syllable, the word is not legal.
        syllables = []
        if not word:
            raise ValueError(f"Empty word.")
        while word:
            for length in [3, 2, 1, 0]:
                # if we reach the 0 case, the word is not legal.
                if length == 0:
                    raise ValueError(f"Invalid word: {word}")
                # in the other cases, try build the syllable.
                try:
                    syl = Syllable(word[-length:])
                except ValueError:
                    continue
                else:
                    syllables.insert(0, syl)
                    word = word[:-length]
                    break
        return syllables

    @lru_cache(maxsize=CACHINESS)
    def first_sound(self):
        """The first sound (onset or vowel) of the word."""
        return self.syllables[0].first_sound()

    @lru_cache(maxsize=CACHINESS)
    def shape(self):
        """The "shape" of the word.
        
        Onsets become P, vowels become O, final n becomes N.
        Examples: a is O, ma is PO, en is ON, kin is PON.
        kala is POPO, akesi is OPOPO, and sitelen is POPOPON.
        """
        return ''.join([s.shape() for s in self.syllables])

    @lru_cache(maxsize=CACHINESS)
    def inherent_cost(self):
        """The cost of this wordform. Higher is worse.
        
        Difficult words are bad. This is counted in two ways.
        Length: each letter of length of a word counts for 1 cost.
        Starting with a vowel: starting with a vowel costs 0.5.
        In other words, an initial glottal stop counts as 0.5 letters.
        """
        cost = 0
        cost += len(self.spelling())
        if self.first_sound() in VOWELS:
            cost += 0.5
        return cost

    @lru_cache(maxsize=CACHINESS*CACHINESS)
    def similarity_cost(self, other):
        """The cost of the similarity of two wordforms. Higher is more similar.

        Similar words are bad. This is counted in a few ways.
        Prefixes: If one wordform is a prefix of another, that's very bad.
            Add (2 + length of the prefix) to the cost.
        Edit distance: if adjusted edit distance < 0.5, add 1/that to cost.
        Word shape: if shape is the same, add 0.1 to cost.
        First sound: if first sound is the same, add 0.1 to cost.
        """
        cost = 0
        s1, s2 = self.spelling(), other.spelling()
        # if one is a prefix, add 2 + length of the prefix
        if s1.startswith(s2) or s2.startswith(s1):
            cost += 2 + min(len(s1), len(s2))
        # if the wordforms are similar, add 1/dissimilarity
        dissimilarity = edit_distance_adjusted(s1, s2)
        if dissimilarity < 0.5:
            cost += 1 / (dissimilarity)
        # if the shapes are the same, add 0.1
        if self.shape() == other.shape():
            cost += 0.1
        # if the first sound is the same, add 0.1
        if self.first_sound() == other.first_sound():
            cost += 0.1
        return cost

    def __gt__(self, other):
        """Compare two wordforms by their spellings."""
        return self.spelling() > other.spelling()
    
    @lru_cache(maxsize=CACHINESS)
    def spelling(self):
        """The actual letters of the wordform, spelled in order."""
        return ''.join([s.spelling() for s in self.syllables])

    def __repr__(self):
        """An unambiguous string representation of the wordform."""
        return '.'.join([repr(s) for s in self.syllables])
    
    def __str__(self):
        """A simple string representation of the wordform.
        
        Currently, this is the same as the spelling(), but I want the option
        of changing it to something fancier without screwing up everything
        that relies on spelling."""
        return ''.join([str(s) for s in self.syllables])


# all one-syllable words.
WORDFORMS_1SYL = [Wordform(syllables=[s]) for s in SYLLABLES]

# build all two-syllable words.
WORDFORMS_2SYL = []
for s1 in SYLLABLES:
    for s2 in SYLLABLES:
        # can't have onsetless syllable mid-word.
        if s2.onset == '':
            continue
        # can't have n before m or n.
        if s1.coda == 'n' and s2.onset in ['m', 'n']:
            continue
        WORDFORMS_2SYL.append(Wordform(syllables=[s1, s2]))

WORDFORMS = WORDFORMS_1SYL + WORDFORMS_2SYL